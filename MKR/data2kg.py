from pymongo import MongoClient
import random


class convertKG(object):
    """docstring for convertKG"""

    def __init__(self):
        super(convertKG, self).__init__()
        # 连接数据库
        self.conn = MongoClient('127.0.0.1', 27017)
        self.db = self.conn.NetCloudMusic
        self.my_collection = self.db.PlaylistInfo
        # 歌曲和歌手对应
        self.song_sing = {}
        # 存放标签
        self.tags = {}
        self.tags_index = 0
        # 音乐id
        self.musics = {}
        self.music_index = 0
        # 文件操作
        self.writer_entity = open('./data/music/item_index2entity_id.txt', 'w',encoding='utf8')
        self.writer_u_i = open('./data/music/user_artists.dat', 'w',encoding='utf8')
        self.writer_relations = open('./data/music/kg.txt', 'w',encoding='utf8')
        # 拿到row
        self.get_data()

    def get_data(self):
        self.data = self.my_collection.find({})

    def add_tag(self, tags):
        for tag in tags:
            if (self.tags.get(tag)):
                continue
            self.tags[tag] = self.tags_index
            self.tags_index += 1

    def convert(self, data):
        # 获得userId
        userId = data['playlist_info']['playlist']['creator']['userId']
        # 该歌单得tags传递给所有歌曲（取前十）
        tags = data['playlist_info']['playlist']['tags']
        self.add_tag(tags)
        # 获得tracks下所有的music id，以及它的popularity
        tracks = data['playlist_info']['playlist']['tracks']
        # print(tracks)
        for item in tracks:
            if (self.musics.get(item['id']) != None):
                continue
            self.musics[item['id']] = self.music_index
            self.writer_entity.write('{}\t{}\n'.format(item['id'], self.musics[item['id']]))

            self.writer_u_i.write('{}\t{}\t{}\n'.format(userId, item['id'], int(item['pop'])))
            # 构建music.track_id.artist_id
            # print(item['ar'][0]['id'])
            self.writer_relations.write(
                '{}\t{}\t{}\n'.format(self.musics[item['id']], 'music.track_id.artist_id', item['ar'][0]['id']))
            self.music_index += 1
            # 构建music.track_id.tag_id
            # 构建music.artist_id.tag_id
            # 构建msuic.track_id.genre
            for tag in tags:
                self.writer_relations.write(
                    '{}\t{}\t{}\n'.format(self.musics[item['id']], 'music.track_id.' + tag, self.tags[tag]))
            # self.writer_relations.write('{}\t{}\t{}\n'.format(item['ar'][0]['id'],'music.artist_id.tag_id',self.tags[tag]))
        # if tags:
        # 	self.writer_relations.write('{}\t{}\t{}\n'.format(item['id'],'music.track_id.tag_id',self.tags[random.choice(tags)]))

    def main(self):
        for item in self.data:
            self.convert(item)


test = convertKG()
test.main()

