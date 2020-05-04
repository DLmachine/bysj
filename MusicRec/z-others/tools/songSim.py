# -*- coding:utf-8 -*-

import os,django
# os.environ['DJANGO_SETTINGS_MODULE'] = 'MusicRec.settings'
# django.setup()
import json

from MusicRec.MusicRec.settings import PlaylistInfo
class SongSim:
    def __init__(self):
        self.writer = open("./data/song_tag.txt", "w", encoding="utf-8")
        self.writeSongTags()
        self.songTags = self.getSongTags()
        print(self.songTags)
        self.sim = self.getSongSim()

        print(self.sim)
    def writeSongTags(self):

        for item in PlaylistInfo.find():
            tags=item['playlist_info']['playlist']['tags']
            tracks=item['playlist_info']['playlist']['tracks']
            for track in tracks:
                id=track['id']
                for tag in tags:
                    content=str(id)+','+tag+'\n'
                    self.writer.write(content)
        self.writer.close()
    def getSongTags(self):
        songTagsDict = dict()
        for line in open("./data/song_tag.txt","r",encoding="utf-8"):
            songId, tag = line.strip().split(",")
            songTagsDict.setdefault(songId,set())
            songTagsDict[songId].add(tag)
        return songTagsDict

    def getSongSim(self):
        sim = dict()
        if os.path.exists("./data/song_sim.json"):
                sim = json.load(open("./data/song_sim.json","r",encoding="utf-8"))
        else:
            i = 0
            for song1 in self.songTags.keys():
                sim[song1] = dict()
                for song2 in self.songTags.keys():
                    if song1 != song2:
                        j_len = len (self.songTags[song1] & self.songTags[song2] )
                        if j_len !=0:
                            result = j_len / len(self.songTags[song1] | self.songTags[song2])
                            if sim[song1].__len__() < 20 or result > 0.8:
                                sim[song1][song2] = result
                            else:
                                # 找到最小值 并删除
                                minkey = min(sim[song1], key=sim[song1].get)
                                del sim[song1][minkey]
                i += 1
                print(str(i) + "\t" + song1)
            json.dump(sim, open("./data/song_sim.json","w",encoding="utf-8"))
        print("歌曲相似度计算完毕！")
        return sim

    def transform(self):
        fw = open("./data/song_sim.txt", "a", encoding="utf-8")
        for s1 in self.sim.keys():
            for s2 in self.sim[s1].keys():
                fw.write(s1 + "," + s2 + "," + str(self.sim[s1][s2]) + "\n")
        fw.close()
        print("Over!")

if __name__ == "__main__":
    song = SongSim()
    song.transform()