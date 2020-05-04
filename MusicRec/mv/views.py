from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
import requests,json
from .getComments import CommentCrawlClass
def mv_url(request):
    id=request.GET.get('id')
    url=f'https://api.imjad.cn/cloudmusic/?type=mv&id={id}'
    data=json.loads(requests.get(url=url).text)
    res={
        "code": 200,
        "data": {
            "id": int(id),
            "url": data['data']['brs']['240'],
        }
    }
    return JsonResponse(res)

def mv_detail(request):
    id = request.GET.get('mvid')
    url = f'https://api.imjad.cn/cloudmusic/?type=mv&id={id}'
    data = json.loads(requests.get(url=url).text)

    return JsonResponse(data)

def comment(request):
    id=request.GET.get('id')
    limit=request.GET.get('limit')
    offset=request.GET.get('offset')
    comment_url = 'http://music.163.com/weapi/v1/resource/comments/R_MV_5_%s?csrf_token=' % id
    res=CommentCrawlClass(comment_url).get_album_comment(20)
    return JsonResponse(res[0])

def video_url(request):
    pass

def video_detail(request):
    pass