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
from user.models import User,UserTag,UserSim,UserUserRec,UserSingRec,UserPlayListRec,UserSongRec
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
    user = models.CharField(blank=True, max_length=64, verbose_name="用户ID")
    related = models.CharField(blank=True, max_length=64, verbose_name="用户ID")
    sim = models.FloatField(blank=True,verbose_name="相似度")
    """

    def UserUserRecToMySQL(self):
        for line in open("./data/user_user_prefer.txt","r",encoding="utf-8"):
            _list = line.split(",")
            if _list.__len__() == 3:
                user,related,sim= line.split(",")
                s = UserUserRec(
                    user = user,
                    related = related,
                    sim = sim
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(user)
                    pass
            else:
                print(line)
        print("Over!")


    """
        user = models.CharField(blank=True, max_length=64, verbose_name="用户ID")
        related = models.CharField(blank=True, max_length=64, verbose_name="歌手ID")
        sim = models.FloatField(blank=True,verbose_name="相似度")
    """
    def UserSingRecToMySQL(self):
        for line in open("./data/user_singer_prefer.txt","r",encoding="utf-8"):
            _list = line.split(",")
            if _list.__len__() == 3:
                user,related,sim= line.split(",")
                s = UserSingRec(
                    user = user,
                    related = related,
                    sim = sim
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(user)
                    pass
            else:
                print(line)
        print("Over!")

    """
        user = models.CharField(blank=True, max_length=64, verbose_name="用户ID")
        related = models.CharField(blank=True, max_length=64, verbose_name="用户ID")
        sim = models.FloatField(blank=True,verbose_name="相似度")
    """
    def UserSongRecToMySQL(self):
        for line in open("./data/user_song_prefer.txt","r",encoding="utf-8"):
            _list = line.split(",")
            if _list.__len__() == 3:
                user,related,sim= line.split(",")
                s = UserSongRec(
                    user = user,
                    related = related,
                    sim = sim
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(user)
                    pass
            else:
                print(line)
        print("Over!")

    def UserPlayListRecToMySQL(self):
        for line in open("./data/user_playlist_prefer.txt","r",encoding="utf-8"):
            _list = line.split(",")
            if _list.__len__() == 3:
                user,related,sim= line.split(",")
                s = UserPlayListRec(
                    user = user,
                    related = related,
                    sim = sim
                )
                try:
                    s.save()
                except Exception as e:
                    print(e)
                    print(user)
                    pass
            else:
                print(line)
        print("Over!")

if __name__ == "__main__":
    tomysql = ToMySQL()
    tomysql.UserUserRecToMySQL()
    tomysql.UserSingRecToMySQL()
    tomysql.UserSongRecToMySQL()
    tomysql.UserPlayListRecToMySQL()

