# -*- coding:utf-8 -*-
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from index.models import Cate
from user.models import User,UserBrowse
from song.models import Song
from sing.models import Sing
from playlist.models import PlayList

from playlist.views import all as allPlayList
from song.views import all as allSongs
from sing.views import all as allSings
from user.views import all as allUsers,wirteBrowse,getLocalTime
from index.indexTag import GetRecTags
from index.ranking import rankResult
from index import recRight as rec_right

from MusicRec.settings import PlayListCatlist,UserInfo,SongDetail,PlaylistInfo
import json,os

def status(request):
    data={
        "code": 200,
        "profile": {
            "userId": 0,
            "nickname": "",
            "avatarUrl": ""
        }
    }

    if not request.session.get('uid'):
        return JsonResponse({"code": 400})
    data['profile']['userId'] = request.session.get('uid')
    data['profile']['nickname'] =request.session.get('nickname')
    data['profile']['avatarUrl'] =request.session.get('avatarUrl')
    return JsonResponse(data)
#登录，查表，返回数据
def login(request):

    data={
        "loginType": 1,
        "code": 200,
        "account": {
            "id": 0,
            "type": 1,
            "status": 0,
            "whitelistAuthority": 0,
            "createTime": 1481346154864,
            "salt": "[B@200e29e9",
            "tokenVersion": 0,
            "ban": 0,
            "baoyueVersion": 0,
            "donateVersion": 0,
            "vipType": 0,
            "viptypeVersion": 0,
            "anonimousUser": False
        }
    }
    user_id=request.GET.get('phone')
    userinfo=UserInfo.find_one({'userId':int(user_id)})
    print(userinfo)
    if userinfo == None:
        return JsonResponse({
            "msg": "密码错误",
            "code": 502,
            "message": "密码错误"
        })
    data['id']=int(user_id)
    request.session['uid']=userinfo['userId']
    request.session['nickname']=userinfo['nickname']
    request.session['avatarUrl']=userinfo['avatarUrl']
    return JsonResponse(data)

#退出
def logout(request):
    data={
        "code": 200
    }
    # del request.session['uid']
    # del request.session['nickname']
    # del request.session['avatarUrl']
    return JsonResponse(data)

#获取banner内容
def banner(request):
    data=json.load(open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/index/data/banner.json','r',encoding='utf8'))
    return JsonResponse(data)

#获取首页推荐歌单
def personalized(request):
    data={}

    if(request.COOKIES.get('sessionid')):
        data=rec_right.rec_right_playlist(request)
        return JsonResponse(data)
    data = {"code": 200, "recommend": []}
    for item in PlaylistInfo.find({}).limit(15).skip(1250):
        one = {}

        one['id'] = item['playlist_id']
        one['name'] = item['playlist_info']['playlist']['name']
        one['picUrl'] = item['playlist_info']['playlist']['coverImgUrl']
            # one['creator']=item['playlist_info']['playlist']['creator']
        data['recommend'].append(one)
    return JsonResponse(data)

#获取首页推荐电台，写死，主要是音乐的推荐
def djprogram(request):
    data=json.load(open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/index/data/djprogram.json','r',encoding='utf8'))
    return JsonResponse(data)

#获取首页推荐新歌
def newsong(request):
    data=json.load(open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/index/data/newsong.json','r',encoding='utf8'))
    return JsonResponse(data)

#首页Mv推荐,写死
def mv(request):
    data=json.load(open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/index/data/mv.json','r',encoding='utf8'))
    return JsonResponse(data)


# 我的足迹
def myBrowse(request):
    # 接口传入的page参数
    _page_id = int(request.GET.get("page"))
    _uname = request.session.get("username")
    result = dict()
    result["code"] = 1
    result["data"] = dict()
    _list = list()
    browses = UserBrowse.objects.filter(user_name=_uname).order_by("user_click_time")
    total = browses.__len__()
    value = ""
    for one in browses[(_page_id -1 ) * 30: _page_id * 30]:
        if one.click_cate == "2":
            value = PlayList.objects.filter(pl_id=one.click_id)[0].pl_name
        elif one.click_cate == "3":
            value = Song.objects.filter(song_id=one.click_id)[0].song_name
        elif one.click_cate == "4":
            if "12797496" in one.click_id:
                value = Sing.objects.filter(sing_id__endswith="12797496")[0].sing_name
            else:
                value = Sing.objects.filter(sing_id=one.click_id)[0].sing_name
        elif one.click_cate == "5":
            value = User.objects.filter(u_id=one.click_id)[0].u_name
        _list.append({
            "username": request.GET.get("username"),
            "time": one.user_click_time,
            "desc": one.desc,
            "name": value
        })
    result["data"]["click"] = _list
    result["data"]["total"] = total
    return result

# 歌单、歌曲模块的推荐部分

def recplaylist(request):
    result = rec_right.rec_right_playlist(request)
    return JsonResponse(result)

def recmusic(request):
    result = rec_right.rec_right_song(request)
    return JsonResponse(result)
