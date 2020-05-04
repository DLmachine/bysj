import requests
from bs4 import BeautifulSoup
import json
rs=requests.session()
user='学号'
passwd='网关登录密码'
login_url='https://pass.neu.edu.cn/tpass/login'
daka_url='https://e-report.neu.edu.cn/'
daka_post_url='https://e-report.neu.edu.cn/api/notes'
data_api_url=f'https://e-report.neu.edu.cn/api/profiles/{user}?xingming='
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
data=rs.get(url=login_url,headers=headers).text
soup=BeautifulSoup(data,'html.parser')
lt=soup.find(attrs={'id':'lt'})['value']
execution=soup.find(attrs={'name':'execution'})['value']
_eventId=soup.find(attrs={'name':'_eventId'})['value']
post_data={
    'rsa':user+passwd+lt,
    'ul':len(user),
    'pl':len(passwd),
    'lt':lt,
    '_eventId':_eventId,
    'execution':execution
}
rs.post(url=login_url,data=post_data,headers=headers)
data=rs.get(url=daka_url,headers=headers).text
soup=BeautifulSoup(data,'html.parser')
_token=soup.find(attrs={'name':'_token'})['value']
xingming=str(soup.find(attrs={'id':'navbarDropdown'}).get_text()).strip().split('：')[1]
student_data=json.loads(rs.get(url=data_api_url+xingming,headers=headers).text)
data={
    '_token':_token,
    'jibenxinxi_shifoubenrenshangbao': '1',
    'profile[xuegonghao]': student_data['data'].get('xuegonghao'),
    'profile[xingming]': student_data['data'].get('xingming'),
    'profile[suoshubanji]': student_data['data'].get('suoshubanji'),
    'jiankangxinxi_muqianshentizhuangkuang': '正常',
    'xingchengxinxi_weizhishifouyoubianhua': '0',
    'qitashixiang_qitaxuyaoshuomingdeshixiang': None
}
res=rs.post(url=daka_post_url,data=data,headers=headers).text

