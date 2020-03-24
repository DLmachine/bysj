# -*- coding: utf-8 -*-
import scrapy,requests
from NetCloudMusic.items import NetCloudMusicPlaylistItem
from NetCloudMusic.spiders.getComments import CommentCrawlClass
class GetplaylistSpider(scrapy.Spider):
    name = 'getPlaylist'
    allowed_domains = ['music.163.com/',]
    start_urls = ['http://music.163.com/',]
    params='?order=hot&cat=全部&limit=35&offset='
    headers = {
        "Referer": "http://music.163.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3067.6 Safari/537.36",
    }
    def start_requests(self):
        for i in range(0,1296,35):
            url='http://music.163.com/discover/playlist/'+self.params+str(i)
            yield scrapy.Request(url=url, method='GET', callback=self.parse)

    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        lis=response.selector.xpath('/html/body/div[3]/div/ul/li')
        data=dict()
        count=1
        for li in lis:
            title=li.xpath(f'//*[@id="m-pl-container"]/li[{count}]/div/a/@title').extract()[0]
            href=li.xpath(f'//*[@id="m-pl-container"]/li[{count}]/div/a/@href').extract()[0][13:]
            count+=1
            #https://music.163.com/#/playlist?id=4901758294
            url='https://music.163.com/playlist?id='+href
            data[href]=[title,url]
        for k,v in data.items():
            yield scrapy.Request(url=v[1],method='GET',headers=self.headers,callback=self.parse_playlist,meta={'playlist_name':v[0],'playlist_id':k,'playlist_url':v[1]},dont_filter=True)

    def parse_playlist(self,response):
        print('*'*123)
        """
        回调函数不执行是因为requets不在 allowed_domains 列表中，一种方法是allowed_domains添加，还有就是Request加入dont_filter=True
        playlist_id = scrapy.Field()
        playlist_name = scrapy.Field()
        playlist_url = scrapy.Field()
        playlist_info = scrapy.Field()
        playlist_comments = scrapy.Field()
        playlist_comment_count = scrapy.Field()
        :param response:
        :return:
        """
        item=NetCloudMusicPlaylistItem()
        item['playlist_id']=response.meta['playlist_id']
        comment_url = 'http://music.163.com/weapi/v1/resource/comments/A_PL_0_%s?csrf_token=' % item['playlist_id']
        item['playlist_name']=response.meta['playlist_name']
        item['playlist_url']=response.meta['playlist_url']
        import json
        playlist_info=json.loads(requests.get(url='https://api.imjad.cn/cloudmusic/?type=playlist&id='+str(item['playlist_id']),headers=self.headers).text)
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        item['playlist_info']=playlist_info
        playlist_comment_count=playlist_info['playlist']['commentCount']
        item['playlist_comment_count']=playlist_comment_count
        item['playlist_comments'] = CommentCrawlClass(comment_url).get_playlist_comment(playlist_comment_count)
        return item
