import argparse
import numpy as np
import json
RATING_FILE_NAME = dict({'movie': 'ratings.txt',
                         'book': 'BX-Book-Ratings.csv',
                         'music': 'user_artists.dat'})
SEP = dict({'movie': '::', 'book': ';', 'music': '\t'})
THRESHOLD = dict({'movie': 4, 'book': 0, 'music': 0})

def read_item_index_to_entity_id_file():
    file = './data/' + DATASET + '/item_index2entity_id.txt'
    print('reading item index to entity id file: ' + file + ' ...')
    i = 0
    for line in open(file, encoding='utf-8').readlines():
        item_index = line.strip().split('\t')[0]
        satori_id = line.strip().split('\t')[1]
        if item_index not in item_index_old2new.keys():
            item_index_old2new[item_index] = i
        entity_id2index[satori_id] = i
        i += 1

def convert_rating():
    file = './data/' + DATASET + '/' + RATING_FILE_NAME[DATASET]

    print('reading rating file ...')
    item_set = set(item_index_old2new.values())

    user_pos_ratings = dict()
    user_neg_ratings = dict()

    for line in open(file, encoding='utf-8').readlines()[1:]:
        array = line.strip().split(SEP[DATASET])

        item_index_old = array[1]
        if item_index_old not in item_index_old2new:  # the item is not in the final item set
            continue
        item_index = item_index_old2new[item_index_old]

        user_index_old = int(array[0])

        rating = float(array[2])
        if rating >= THRESHOLD[DATASET]:
            if user_index_old not in user_pos_ratings:
                user_pos_ratings[user_index_old] = set()
            user_pos_ratings[user_index_old].add(item_index)
        else:
            if user_index_old not in user_neg_ratings:
                user_neg_ratings[user_index_old] = set()
            user_neg_ratings[user_index_old].add(item_index)

    print('converting rating file ...')
    writer = open('./data/' + DATASET + '/ratings_final.txt', 'w', encoding='utf-8')
    index_user_writer=open('./data/' + DATASET + '/index_user_id.json', 'w', encoding='utf-8')
    index_user={}
    user_cnt = 0
    user_index_old2new = dict()
    for user_index_old, pos_item_set in user_pos_ratings.items():
        if user_index_old not in user_index_old2new:
            index_user[user_cnt] = user_index_old
            user_index_old2new[user_index_old] = user_cnt
            user_cnt += 1
        user_index = user_index_old2new[user_index_old]

        for item in pos_item_set:
            writer.write('%d\t%d\t1\n' % (user_index, item))
        unwatched_set = item_set - pos_item_set
        if user_index_old in user_neg_ratings:
            unwatched_set -= user_neg_ratings[user_index_old]
        for item in np.random.choice(list(unwatched_set), size=len(pos_item_set), replace=False):
            writer.write('%d\t%d\t0\n' % (user_index, item))
    writer.close()
    index_user_writer.write(json.dumps(index_user))
    index_user_writer.close()
    print('number of users: %d' % user_cnt)
    print('number of items: %d' % len(item_set))


def convert_kg():
    print('converting kg.txt file ...')
    entity_cnt = len(entity_id2index)
    print(entity_cnt)
    relation_cnt = 0
    count=0
    #实体索引对应kg文件的头节点
    writer = open('./data/' + DATASET + '/kg_final.txt', 'w', encoding='utf-8')
    file = open('./data/' + DATASET + '/kg.txt', encoding='utf-8')
    for line in file:
        array = line.strip().split('\t')
        head_old = array[0]
        relation_old = array[1]     # relation
        tail_old = array[2]

        if head_old not in entity_id2index: # Ignore erroneous data
            continue
        head = entity_id2index[head_old]

        if tail_old not in entity_id2index:
            entity_id2index[tail_old] = entity_cnt
            entity_cnt += 1
        tail = entity_id2index[tail_old]

        if relation_old not in relation_id2index:
            relation_id2index[relation_old] = relation_cnt
            relation_cnt += 1
        relation = relation_id2index[relation_old]
        # print(head_old,count)
        # count+=1
        writer.write('%d\t%d\t%d\n' % (head, relation, tail))

    writer.close()
    print('number of entities (containing items): %d' % entity_cnt)
    print('number of relations: %d' % relation_cnt)

# def convert_kg():
#     print('converting kg.txt file ...')
#     entity_cnt = len(entity_id2index)
#     relation_cnt = 0
#
#     writer = open('../data/' + DATASET + '/kg_final.txt', 'w', encoding='utf-8')
#     file = open('../data/' + DATASET + '/kg.txt', encoding='utf-8')
#
#     for line in file:
#         array = line.strip().split('\t')
#         head_old = array[0]
#         relation_old = array[1]
#         tail_old = array[2]
#
#         if head_old not in entity_id2index:
#             continue
#         head = entity_id2index[head_old]
#
#         if tail_old not in entity_id2index:
#             print(tail_old)
#             print('tianzhkaishabi')
#             exit()
#             entity_id2index[tail_old] = entity_cnt
#             entity_cnt += 1
#         tail = entity_id2index[tail_old]
#
#         if relation_old not in relation_id2index:
#             relation_id2index[relation_old] = relation_cnt
#             relation_cnt += 1
#         relation = relation_id2index[relation_old]
#
#         writer.write('%d\t%d\t%d\n' % (head, relation, tail))
#
#     writer.close()
#     print('number of entities (containing items): %d' % entity_cnt)
#     print('number of relations: %d' % relation_cnt)


if __name__ == '__main__':
    np.random.seed(555)

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, default='music', help='which dataset to preprocess')
    args = parser.parse_args()
    DATASET = args.d

    entity_id2index = dict()
    relation_id2index = dict()
    item_index_old2new = dict()

    read_item_index_to_entity_id_file()
    convert_rating()
    convert_kg()

    print('done')

