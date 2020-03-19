# -*-coding:utf-8-*-
from __future__ import absolute_import
import os
import json
import base64
import requests
import binascii
import hashlib
from Crypto.Cipher import AES

class CommentCrawlClass(object):

    def __init__(self,comment_url):
        self.comment_url = comment_url
        self.headers = {
            "Referer":"http://music.163.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3067.6 Safari/537.36",
        }

    def createSecretKey(self,size):
        '''生成长度为16的随机字符串作为密钥secKey
        '''
        # print(self.createSecretKey)
        return binascii.hexlify(os.urandom(size))[:16]


    def AES_encrypt(self,text, secKey):
        '''进行AES加密
        '''
        pad = 16 - len(text) % 16
        text = text + chr(pad) * pad
        encryptor = AES.new(secKey.encode('utf-8'), AES.MODE_CBC, b'0102030405060708')
        ciphertext = encryptor.encrypt(text.encode('utf-8'))
        ciphertext = base64.b64encode(ciphertext).decode('utf-8')
        return ciphertext

    def rsaEncrypt(self, text, pubKey, modulus):
        '''进行RSA加密
        '''
        text = text[::-1]
        rs = pow(int(binascii.hexlify(text), 16), int(pubKey, 16), int(modulus, 16))
        return format(rs, 'x').zfill(256)

    def encrypted_request(self, text):
        '''将明文text进行两次AES加密获得密文encText,
        因为secKey是在客户端上生成的，所以还需要对其进行RSA加密再传给服务端。
        '''
        pubKey = '010001'
        modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        nonce = '0CoJUm6Qyw8W8jud'

        text = json.dumps(text)
        secKey = self.createSecretKey(16)
        encText = self.AES_encrypt(self.AES_encrypt(text, nonce), secKey.decode('utf-8'))
        encSecKey = self.rsaEncrypt(secKey, pubKey, modulus)
        data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        return data

    def get_post_req(self, url, data):
        try:
            req = requests.post(url, headers=self.headers, data=data)
        except Exception as e:
            with open('D:\\error_post_url.txt','a+') as f:
                f.write(url+'\n')
            print(url,e)
            # return None
        return req.json()

    def get_offset(self, offset=0):
        '''偏移量
        '''
        if offset == 0:
            text = {'rid':'', 'offset':'0', 'total':'true', 'limit':'20', 'csrf_token':''}
        else:
            text = {'rid':'', 'offset':'%s' % offset, 'total':'false', 'limit':'20', 'csrf_token':''}
        return text

    def get_json_data(self,url,offset):
        '''json 格式的评论
        '''
        text = self.get_offset(offset)
        data = self.encrypted_request(text)
        json_text = self.get_post_req(url, data)
        return json_text

    def get_song_comment(self):
        '''某首歌下全部评论
        '''
        comment_info = []
        data = self.get_json_data(self.comment_url,offset=0)
        comment_count = data['total']
        if comment_count:
            comment_info.append(data)
            if comment_count > 20:
                for offset in range(20,int(comment_count),20):
                    comment = self.get_json_data(self.comment_url,offset=offset)
                    comment_info.append(comment)
        return comment_info

    def get_album_comment(self,comment_count):
        '''某专辑下全部评论
        '''
        album_comment_info = []
        if comment_count:
            for offset in range(0,int(comment_count),20):
                comment = self.get_json_data(self.comment_url,offset=offset)
                album_comment_info.append(comment)
        return album_comment_info