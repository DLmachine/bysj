import tensorflow as tf
import argparse
import os

signature_key = "crt_scores"

def pre_scores():
    with tf.Session() as sess:
        meta_graph_def = tf.saved_model.loader.load(sess, [tf.saved_model.tag_constants.SERVING],
                                                    './model/' + DATASET + '/result/' + restore_path)
        signature = meta_graph_def.signature_def

        user_id = sess.graph.get_tensor_by_name(signature[signature_key].inputs["user_id"].name)
        item_id = sess.graph.get_tensor_by_name(signature[signature_key].inputs["item_id"].name)
        head_id = sess.graph.get_tensor_by_name(signature[signature_key].inputs["head_id"].name)
        is_dropout = sess.graph.get_tensor_by_name(signature[signature_key].inputs["is_dropout"].name)

        pred_all = sess.graph.get_tensor_by_name(signature[signature_key].outputs["ctr_predict"].name)

        # userid, itemid in ratings_final.txt
        item_id_data = head_id_data = [i for i in range(1000)]
        user_id_data = [0] * len(item_id_data)

        pre_score = sess.run([pred_all],
                             feed_dict={user_id: user_id_data,
                                        item_id: item_id_data,
                                        head_id: head_id_data,
                                        is_dropout: 0.0})[0]

        neg_item_index = list(zip(item_id_data, pre_score))

        print(sorted(neg_item_index,reverse=True,key=lambda x:x[1])[:20])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, default='music', help='which dataset to preprocess')
    parser.add_argument('-result', '--result', type=str, default='result', help='model pd result path')

    args = parser.parse_args()
    DATASET = args.d

    try:
        restore_path = max(os.listdir('./model/' + DATASET + '/' + args.result))
    except:
        restore_path = None

    pre_scores()