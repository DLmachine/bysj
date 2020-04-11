import numpy as np
import tensorflow as tf
from sklearn.metrics import roc_auc_score
from layers import Dense, CrossCompressUnit

class MKR(object):
    def __init__(self, args, n_users, n_items, n_entities, n_relations, restore_path=None):
        self._parse_args(n_users, n_items, n_entities, n_relations, restore_path)
        self._build_inputs()
        self._build_model(args)
        self._build_loss(args)
        self._build_train(args)

    def _parse_args(self, n_users, n_items, n_entities, n_relations, restore_path):
        self.n_user = n_users
        self.n_item = n_items
        self.n_entity = n_entities
        self.n_relation = n_relations
        self.restore_path = restore_path

        # for computing l2 loss
        self.vars_rs = []
        self.vars_kge = []

    def _build_inputs(self):
        self.user_indices = tf.placeholder(tf.int32, [None], 'user_indices')
        self.item_indices = tf.placeholder(tf.int32, [None], 'item_indices')
        self.labels = tf.placeholder(tf.float32, [None], 'labels')
        self.head_indices = tf.placeholder(tf.int32, [None], 'head_indices')
        self.tail_indices = tf.placeholder(tf.int32, [None], 'tail_indices')
        self.relation_indices = tf.placeholder(tf.int32, [None], 'relation_indices')
        self.dropout_param = tf.placeholder(tf.float32, None, 'dropout_param')

    def _build_model(self, args):
        self._build_low_layers(args)
        self._build_high_layers(args)

    def _build_low_layers(self, args):
        if self.restore_path is None:
            self.user_emb_matrix = tf.get_variable('user_emb_matrix', [self.n_user, args.dim])
            self.item_emb_matrix = tf.get_variable('item_emb_matrix', [self.n_item, args.dim])
            self.entity_emb_matrix = tf.get_variable('entity_emb_matrix', [self.n_entity, args.dim])
            self.relation_emb_matrix = tf.get_variable('relation_emb_matrix', [self.n_relation, args.dim])
        else:
            self.user_emb = tf.placeholder(tf.float32, [None, args.dim], 'user_emb')
            self.item_emb = tf.placeholder(tf.float32, [None, args.dim], 'item_emb')
            self.entity_emb = tf.placeholder(tf.float32, [None, args.dim], 'entity_emb')
            self.relation_emb = tf.placeholder(tf.float32, [None, args.dim], 'relation_emb')

            self.user_emb_matrix = tf.Variable(tf.truncated_normal([self.n_user, args.dim]), name='user_emb_matrix', trainable=True)
            self.item_emb_matrix = tf.Variable(tf.truncated_normal([self.n_item, args.dim]), name='item_emb_matrix', trainable=True)
            self.entity_emb_matrix = tf.Variable(tf.truncated_normal([self.n_entity, args.dim]), name='entity_emb_matrix', trainable=True)
            self.relation_emb_matrix = tf.Variable(tf.truncated_normal([self.n_relation, args.dim]), name='relation_emb_matrix', trainable=True)

            self.user_emb_init = self.user_emb_matrix.assign(self.user_emb)
            self.item_emb_init = self.item_emb_matrix.assign(self.item_emb)
            self.entity_emb_init = self.entity_emb_matrix.assign(self.entity_emb)
            self.relation_emb_init = self.relation_emb_matrix.assign(self.relation_emb)

        # [batch_size, dim]
        self.user_embeddings = tf.nn.embedding_lookup(self.user_emb_matrix, self.user_indices)

        self.item_embeddings = tf.nn.embedding_lookup(self.item_emb_matrix, self.item_indices)
        self.head_embeddings = tf.nn.embedding_lookup(self.entity_emb_matrix, self.head_indices)

        self.relation_embeddings = tf.nn.embedding_lookup(self.relation_emb_matrix, self.relation_indices)
        self.tail_embeddings = tf.nn.embedding_lookup(self.entity_emb_matrix, self.tail_indices)

        for _ in range(args.L):
            user_mlp = Dense(input_dim=args.dim, output_dim=args.dim, dropout=self.dropout_param)
            tail_mlp = Dense(input_dim=args.dim, output_dim=args.dim, dropout=self.dropout_param)
            cc_unit = CrossCompressUnit(args.dim)
            self.user_embeddings = user_mlp(self.user_embeddings)
            self.item_embeddings, self.head_embeddings = cc_unit([self.item_embeddings, self.head_embeddings])
            self.tail_embeddings = tail_mlp(self.tail_embeddings)

            self.vars_rs.extend(user_mlp.vars)
            self.vars_rs.extend(cc_unit.vars)
            self.vars_kge.extend(tail_mlp.vars)
            self.vars_kge.extend(cc_unit.vars)

    def _build_high_layers(self, args):
        # RS
        use_inner_product = True
        if use_inner_product:
            # [batch_size]
            self.scores = tf.reduce_sum(self.user_embeddings * self.item_embeddings, axis=1)
        else:
            # [batch_size, dim * 2]
            self.user_item_concat = tf.concat([self.user_embeddings, self.item_embeddings], axis=1)
            for _ in range(args.H - 1):
                rs_mlp = Dense(input_dim=args.dim * 2, output_dim=args.dim * 2, dropout=self.dropout_param)
                # [batch_size, dim * 2]
                self.user_item_concat = rs_mlp(self.user_item_concat)
                self.vars_rs.extend(rs_mlp.vars)

            rs_pred_mlp = Dense(input_dim=args.dim * 2, output_dim=1, dropout=self.dropout_param)
            # [batch_size]
            self.scores = tf.squeeze(rs_pred_mlp(self.user_item_concat))
            self.vars_rs.extend(rs_pred_mlp.vars)
        self.scores_normalized = tf.nn.sigmoid(self.scores)

        # KGE
        # [batch_size, dim * 2]
        self.head_relation_concat = tf.concat([self.head_embeddings, self.relation_embeddings], axis=1)
        for _ in range(args.H - 1):
            kge_mlp = Dense(input_dim=args.dim * 2, output_dim=args.dim * 2, dropout=self.dropout_param)
            # [batch_size, dim]
            self.head_relation_concat = kge_mlp(self.head_relation_concat)
            self.vars_kge.extend(kge_mlp.vars)

        kge_pred_mlp = Dense(input_dim=args.dim * 2, output_dim=args.dim, dropout=self.dropout_param)
        # [batch_size, 1]
        self.tail_pred = kge_pred_mlp(self.head_relation_concat)
        self.vars_kge.extend(kge_pred_mlp.vars)
        self.tail_pred = tf.nn.sigmoid(self.tail_pred)

        self.scores_kge = tf.nn.sigmoid(tf.reduce_sum(self.tail_embeddings * self.tail_pred, axis=1))
        # self.rmse = tf.reduce_mean(
        #     tf.sqrt(tf.reduce_sum(tf.square(self.tail_embeddings - self.tail_pred), axis=1) / args.dim))

    def _build_loss(self, args):
        # RS
        self.base_loss_rs = tf.reduce_mean(
            tf.nn.sigmoid_cross_entropy_with_logits(labels=self.labels, logits=self.scores))
        self.l2_loss_rs = tf.nn.l2_loss(self.user_embeddings) + tf.nn.l2_loss(self.item_embeddings)
        for var in self.vars_rs:
            self.l2_loss_rs += tf.nn.l2_loss(var)
        self.loss_rs = self.base_loss_rs + self.l2_loss_rs * args.l2_weight

        # KGE
        self.base_loss_kge = -self.scores_kge
        self.l2_loss_kge = tf.nn.l2_loss(self.head_embeddings) + tf.nn.l2_loss(self.tail_embeddings)
        for var in self.vars_kge:
            self.l2_loss_kge += tf.nn.l2_loss(var)
        self.loss_kge = self.base_loss_kge + self.l2_loss_kge * args.l2_weight

    def _build_train(self, args):
        self.optimizer_rs = tf.train.AdamOptimizer(args.lr_rs).minimize(self.loss_rs)
        self.optimizer_kge = tf.train.AdamOptimizer(args.lr_kge).minimize(self.loss_kge)

    def train_rs(self, sess, feed_dict):
        return sess.run([self.optimizer_rs, self.loss_rs], feed_dict)

    def train_kge(self, sess, feed_dict):
        return sess.run([self.optimizer_kge, self.loss_kge], feed_dict)

    def eval(self, sess, feed_dict):
        labels, scores = sess.run([self.labels, self.scores_normalized], feed_dict)
        auc = roc_auc_score(y_true=labels, y_score=scores)
        predictions = [1 if i >= 0.5 else 0 for i in scores]
        acc = np.mean(np.equal(predictions, labels))
        return auc, acc

    def get_scores(self, sess, feed_dict):
        return sess.run([self.item_indices, self.scores_normalized], feed_dict)

    def init_embeding(self, sess, feed_dict):
        sess.run([self.user_emb_init, self.item_emb_init, self.entity_emb_init, self.relation_emb_init], feed_dict)