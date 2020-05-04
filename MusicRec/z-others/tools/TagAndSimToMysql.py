# -*- coding: utf-8 -*-
"""
    Author: Thinkgamer
    Desc:
        代码12-3  把数据写入数据库
"""
import os,django
os.environ["DJANGO_SETTINGS_MODULE"]="MusicRec.settings"
django.setup()
"""
 上边import 解决错误：
 django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not 
 django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.
"""

import pymysql
import time
import json
from MusicRec.settings import DB_HOST,DB_PORT,DB_USER,DB_PASSWD,DB_NAME
from playlist.models import PlayListToSongs,PlayListToTag,PlayList
from song.models import SongLysic,Song,SongTag,SongSim
from user.models import User,UserTag,UserSim
from sing.models import Sing,SingTag,SingSim


class ToMySQL:
    def __init__(self):
        self.db = self.__connect()
        self.cursor = self.db.cursor()

    # 连接mysql数据库
    def __connect(self):
        db = pymysql.Connect(DB_HOST, DB_USER, DB_PASSWD, DB_NAME, DB_PORT, charset='utf8')
        return db
    """
    song_id = models.CharField(blank=True, max_length=64, verbose_name="歌曲ID")
    sim_song_id = models.CharField(blank=True, max_length=64, verbose_name="相似歌曲ID")
    sim = models.FloatField(blank=True, verbose_name="相似度")
    """

    def SongSimToMySQL(self):
        for line in open("./data/song_sim.txt","r",encoding="utf-8"):
            _list = line.split(",")
            if _list.__len__() == 3:
                song_id,sim_song_id,sim= line.split(",")
                s = SongSim(
                    song_id = song_id,
                    sim_song_id = sim_song_id,
                    sim = sim
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(song_id)
                    pass
            else:
                print(line)
        print("Over!")


    """
        sing_id = models.CharField(blank=True, max_length=64, verbose_name="歌手ID")
        sim_sing_id = models.CharField(blank=True, max_length=64, verbose_name="相似歌手ID")
        sim = models.FloatField(blank=True,verbose_name="相似度")
    """
    def SingSimToMySQL(self):
        for line in open("./data/sing_sim.txt","r",encoding="utf-8"):
            _list = line.split(",")
            if _list.__len__() == 3:
                sing_id,sim_sing_id,sim= line.split(",")
                s = SingSim(
                    sing_id = sing_id,
                    sim_sing_id = sim_sing_id,
                    sim = sim
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(sing_id)
                    pass
            else:
                print(line)
        print("Over!")

    # 歌手信息写入数据库 ok
    """
       user_id = models.CharField(blank=True, max_length=64, verbose_name="用户ID")
    sim_user_id = models.CharField(blank=True, max_length=64, verbose_name="相似用户ID")
    sim = models.FloatField(blank=True, verbose_name="用户相似度")
    """
    def UserSimToMySQL(self):
        for line in open("./data/user_sim.txt","r",encoding="utf-8"):
            _list = line.split(",")
            if _list.__len__() == 3:
                user_id,sim_user_id,sim= line.split(",")
                s = UserSim(
                    user_id = user_id,
                    sim_user_id = sim_user_id,
                    sim = sim
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(user_id)
                    pass
            else:
                print(line)
        print("Over!")


    """
       song_id = models.CharField(blank=False, max_length=64, verbose_name="歌曲ID")
    tag = models.CharField(blank=True, max_length=64, verbose_name="歌曲标签")
    """
    def SongTagToMySQL(self):
        for line in open("./data/song_tag.txt","r",encoding="utf-8"):
            _list = line.split(",")
            if _list.__len__() == 2:
                song_id,tag= line.split(",")
                s = SongTag(
                    song_id = song_id,
                    tag = tag
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(song_id)
                    pass
            else:
                print(line)
        print("Over!")

    """
    sing_id = models.CharField(blank=False, max_length=64, verbose_name="歌手ID")
    tag = models.CharField(blank=True, max_length=64, verbose_name="歌手标签")
    """
    def SingTagToMySQL(self):
        for line in open("./data/sing_tag.txt","r",encoding="utf-8"):
            _list = line.split(",")
            if _list.__len__() == 2:
                sing_id,tag= line.split(",")
                s = SingTag(
                    sing_id = sing_id,
                    tag = tag
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(sing_id)
                    pass
            else:
                print(line)
        print("Over!")


if __name__ == "__main__":
    tomysql = ToMySQL()
    # tomysql.SingTagToMySQL()
    # tomysql.SongTagToMySQL()
    # # tomysql.UserSimToMySQL()
    # tomysql.SingSimToMySQL()
    tomysql.SongSimToMySQL()
