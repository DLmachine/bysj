import requests
from NetCloudMusic.spiders import getComments
from lxml import etree
headers = {
        "Referer": "http://music.163.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3067.6 Safari/537.36",
    }
start_url='http://music.163.com/api/song/detail/?id=1375813167&ids=[1375813167]'
comment_url='http://music.163.com/api/v1/resource/comments/R_SO_4_1375813167'
record=' https://music.163.com/weapi/v1/play/record?csrf_token=73491ff8ec022e7bc5d7c9f3db6ca13a'
# http://music.163.com/api/v1/resource/comments/R_SO_4_516997458
# r=requests.get(url=start_url,headers=headers).text
# data=etree.HTML(r)
# lis = data.xpath('//ul[@id="m-artist-box"]/li')
# def parse(lis):
#     for li in lis[0]:
#         post_urls = li.xpath('//a[@class="nm nm-icn f-thide s-fc0"]/@href')
#         for post_url in post_urls:
#             p_url = post_url.lstrip()
#             album_url_split = p_url.split('?')
#             album_url = 'http://music.163.com' + album_url_split[0] + '/album?' + album_url_split[1]
#             r=requests.get(url=album_url,headers=headers).text
#             yield r
# def get_album():

# data=getComments.CommentCrawlClass(comment_url).get_song_comment()
# print(data)
import json
data=requests.get(url=start_url,headers=headers).text
print(data)