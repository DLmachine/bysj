# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.conf import settings
from NetCloudMusic.items import NetCloudMusicSongItem,NetCloudMusicAlbumListItem,NetCloudMusicAlbumItem,NetCloudMusicArtistItem,NetCloudMusicPlaylistItem


class NetCloudMusicPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient(
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']
        )
        db_name = settings['MONGODB_DBNAME']
        self.db = client[db_name]
        self.artist = self.db[settings['MONGODB_COL_ARTIST']]
        # 不能同时生成多个，只能通过isinstance的方法判断
        # self.album = db[settings['MONGODB_COL_ALBUM']]
        # self.album_list = db[settings['MONGODB_COL_ALBUMLIST']]
        # self.song = db[settings['MONGODB_COL_SONG']]

    def process_item(self, item, spider):
        '''不同的item类型，放入不同的集合中，

        分为四块：Items - col - dict - desc ：
            NetCloudMusicArtistItem - > self.aritst - > artist_infos -> 所有的歌手列表
            NetCloudMusicAlbumItem - > self.ablum - > album_infos - > 每个歌手的所有专辑列表
            NetCloudMusicAlbumListItem - > self.album_list - > album_list_infos - > 每张专辑内的所有歌曲列表
            NetCloudMusicSongItem - > self.song -> song_infos -> 每首歌曲的信息
        '''
        if isinstance(item, NetCloudMusicArtistItem):
            artist_infos = dict(item)
            self.artist.insert_one(artist_infos)
            print('NetCloudMusicArtistItem - > success')

        if isinstance(item, NetCloudMusicAlbumItem):
            album_infos = dict(item)
            self.artist = self.db[settings['MONGODB_COL_ALBUM']]
            self.artist.insert_one(album_infos)
            print('NetCloudMusicAlbumItem - > success')

        if isinstance(item, NetCloudMusicAlbumListItem):
            album_list_infos = dict(item)
            self.artist = self.db[settings['MONGODB_COL_ALBUMLIST']]
            self.artist.insert_one(album_list_infos)
            print('NetCloudMusicAlbumListItem - > success')

        if isinstance(item, NetCloudMusicSongItem):
            song_infos = dict(item)
            self.artist = self.db[settings['MONGODB_COL_SONG']]
            self.artist.insert_one(song_infos)
            print('NetCloudMusicSongItem - > success')

        return item



class NetCloudMusicPlaylistPipeline(object):

    def __init__(self):
        client = pymongo.MongoClient(
            settings['MONGODB_HOST'],
            settings['MONGODB_PORT']
        )
        db_name = settings['MONGODB_DBNAME']
        self.db = client[db_name]
        self.playlist = self.db[settings['MONGODB_COL_PLAYLIST']]

    def process_item(self, item, spider):
        flag=self.playlist.find_one({"playlist_id":item['playlist_id']})
        print(flag,item['playlist_id'])
        if isinstance(item, NetCloudMusicPlaylistItem) and not flag:
            playlist_infos = dict(item)
            self.playlist.insert_one(playlist_infos)
            print('NetCloudMusicPlaylistItem - > success')

        return item
