import tensorflow as tf
import argparse
import os
import json
import random
signature_key = "crt_scores"

def pre_scores(userId):
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
        item_id_data = head_id_data = random.sample([i for i in range(133186)],13186)
        user_id_data = [userId] * len(item_id_data)

        pre_score = sess.run([pred_all],
                             feed_dict={user_id: user_id_data,
                                        item_id: item_id_data,
                                        head_id: head_id_data,
                                        is_dropout: 0.0})[0]

        neg_item_index = list(zip(item_id_data, pre_score))

        res=map(lambda x:(index_music_id[str(x[0])],x[1]),sorted(neg_item_index,reverse=True,key=lambda x:x[1])[:15])
        for item,score in list(res):
            writer.write(str(index_user_id[str(userId)])+','+str(item)+','+str(score)+'\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, default='music', help='which dataset to preprocess')
    parser.add_argument('-result', '--result', type=str, default='result', help='model pd result path')

    args = parser.parse_args()
    DATASET = args.d
    index_music_id = json.load(open('./data/' + DATASET + '/' + 'entity_music.json'))
    index_user_id=json.load(open(r'D:\bysj\MKR\data\music\index_user_id.json'))
    writer=open(r'D:\bysj\MusicRec\z-others\rec\data\user_song_prefer.txt','a+',encoding='utf8')
    # print(index_user_id)
    try:
        restore_path = max(os.listdir('./model/' + DATASET + '/' + args.result))
    except:
        restore_path = None
        #400之前
    for i in range(2400,2500):
        print(i)
        pre_scores(i)
    writer.close()