# -*- coding:utf-8 -*-
from django.http import JsonResponse

from song.models import Song,SongLysic,SongTag,SongSim
from sing.models import Sing
from user.views import wirteBrowse,getLocalTime
from MusicRec.settings import SongDetail,SongUrl,SongLyric,SongAvailable,SongComment,SongSim
def all(request):
    # 接口传入的tag参数
    tag = request.GET.get("tag")
    # 接口传入的page参数
    _page_id = int(request.GET.get("page"))
    print("Tag : %s,page_id: %s" % (tag,_page_id))
    _list = list()
    # 全部歌曲
    if tag == "all":
        song_tags_list = Song.objects.all().values("song_id","song_name","song_publish_time").order_by("-song_publish_time")
        # 拼接歌曲信息
        for one in song_tags_list[(_page_id-1) * 30:_page_id * 30]:
            _list.append({
                "song_id": one["song_id"],
                "song_name": one["song_name"],
                "song_publish_time": one["song_publish_time"]
            })
    # 指定标签下的歌曲
    else:
        song_tags_list = SongTag.objects.filter(tag=tag).values("song_id").order_by("song_id")
        song_ids = [song["song_id"] for song in song_tags_list[(_page_id-1) * 30:_page_id * 30] ]
        songs_list = Song.objects.filter(song_id__in=song_ids).values("song_id","song_name","song_publish_time")
        for one in songs_list:
            _list.append({
                "song_id": one["song_id"],
                "song_name": one["song_name"],
                "song_publish_time": one["song_publish_time"]
            })
    total = song_tags_list.__len__()
    return {"code": 1,
            "data": {
                "total": total,
                "songs": _list,
                "tags": getAllSongTags()
            }
        }

def getAllSongTags():
    tags = set()
    for one in SongTag.objects.all().values("tag").distinct().order_by("song_id"):
        tags.add(one["tag"])
    return list(tags)

def one(request):
    song_id = request.GET.get("id")
    song = Song.objects.filter(song_id=song_id)[0]
    s_name = list()
    if song.song_sing_id.__contains__("#"):
        for s_one in song.song_sing_id.split("#"):
            s_name.append(Sing.objects.filter(sing_id=s_one)[0].sing_name)
    else:
        s_name.append(Sing.objects.filter(sing_id= song.song_sing_id)[0].sing_name)
    song_lysic = SongLysic.objects.filter(song_id=song_id)[0]
    wirteBrowse(user_name=request.GET.get("username"),click_id=song_id,click_cate="3", user_click_time=getLocalTime(), desc="查看歌曲")
    return JsonResponse({
        "code":1,
        "data":[
            {
                "song_id": song.song_id,
                "song_name": song.song_name,
                "song_playlist": song.song_pl_id,
                "song_publish_time": song.song_publish_time,
                "song_sing":" / ".join(s_name),
                "song_total_comments": song.song_total_comments,
                "song_hot_comments": song.song_hot_comments,
                "song_url":song.song_url,
                "song_lysic": song_lysic.song_lysic,
                "song_rec": getRecBasedOne(song_id)
            }
        ]
    })

# 获取单首歌曲的推荐
def getRecBasedOne(song_id):
    result = list()
    songs = SongSim.objects.filter(song_id= song_id).order_by("-sim").values("sim_song_id")[:10]
    for song in songs:
        one = Song.objects.filter(song_id=song["sim_song_id"])[0]
        result.append({
            "id": one.song_id,
            "name": one.song_name,
            "publish_time": one.song_publish_time,
            "url":one.song_url,
            "cate":"3"

        })
    return result


def check(request):
    id = request.GET.get('id')
    res={}
    data=SongAvailable.find({'id':int(id)})
    for item in data:
        res['success']=item['success']
        res['message']=item['message']
    return JsonResponse(res)

def songurl(request):
    id=request.GET.get('id')
    data=SongUrl.find({'id':int(id)})
    res={}
    for item in data:
        res=item
    res.pop('_id')
    return JsonResponse(res)

def detail(request):
    ids=request.GET.get('ids')
    ids_list=ids.split(',')
    res = {}
    if len(ids_list)==1:
        data=SongDetail.find({'id':int(ids)})
        for item in data:
            res=item
        res.pop('_id')
    else:
        res['songs']=[]
        for id in ids_list:
            data = SongDetail.find({'id': int(id)})
            for item in data:
                item.pop('_id')
                res['songs'].append(item)
    return JsonResponse(res)

def comment(request):
    ids=request.GET.get('id')
    limit=request.GET.get('limit')
    data=SongComment.find({'id':int(ids)}).limit(int(limit))
    res={}
    for item in data:
        res=item
    res.pop('_id')
    print(res)
    return JsonResponse(res)

def lyric(request):
    ids = request.GET.get('id')
    data = SongLyric.find({'id': int(ids)})
    res={}
    for item in data:
        res = item
    res.pop('_id')
    return JsonResponse(res)

def sim(request):
    ids = request.GET.get('id')
    data = SongSim.find({'id': int(ids)})
    res = {}
    for item in data:
        res = item
    res.pop('_id')
    return JsonResponse(res)