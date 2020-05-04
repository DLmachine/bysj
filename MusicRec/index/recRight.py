# -*- coding:utf-8 -*-
from playlist.models import PlayList
from django.http import JsonResponse
from song.models import Song
from sing.models import Sing
from user.models import User,UserSongRec,UserPlayListRec
from MusicRec.settings import PlaylistInfo,SongDetail
def rec_right_playlist(request):
    # print(request.GET.items())
    u_id = request.session.get("uid")
    rec_all = UserPlayListRec.objects.filter(user=u_id).order_by("-sim")[:15]

    res={"code": 200,"recommend":[]}
    for rec in rec_all:
        data=PlaylistInfo.find({
            'playlist_id':rec.related
        })
        one={}
        for item in data:
            one['id']=item['playlist_id']
            one['name']=item['playlist_info']['playlist']['name']
            one['picUrl']=item['playlist_info']['playlist']['coverImgUrl']
            # one['creator']=item['playlist_info']['playlist']['creator']
        res['recommend'].append(one)
    return res


def rec_right_song(request):
    u_id = request.session.get("uid")
    rec_all = UserSongRec.objects.filter(user=u_id)
    res = {"code": 200, "recommend": []}
    for rec in rec_all:
        print(rec==None)
        data = SongDetail.find({
            'id': int(rec.related)
        })
        one = {}
        for item in data:
            one['id'] = item['id']
            one['name'] = item['songs'][0]['name']
            one['artists'] = item['songs'][0]['ar']
            one['album']=item['songs'][0]['al']
        res['recommend'].append(one)
    return res