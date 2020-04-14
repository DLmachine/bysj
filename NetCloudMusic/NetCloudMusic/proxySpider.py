import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='xiciip',
    port=3306
)
cursor = conn.cursor()

def crawl_ips():
    #爬取西刺网代理ip
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    }
    for i in range(1,100):
        print("==================",i)
        re = requests.get("http://www.xicidaili.com/nn/{0}".format(i),headers=headers)
        text = re.text
        soup = BeautifulSoup(text)
        tr_list = soup.select("tr")
        tr_list = tr_list[1:]
        for td_list in tr_list:
            td_ip = td_list.select("td")[1].get_text()
            td_port = td_list.select("td")[2].get_text()
            http_type = td_list.select("td")[5].get_text()
            speed = float((td_list.select("td")[6].div.get('title'))[:-1])
            if speed > 1:
                continue
            print(http_type,td_ip,td_port,speed)
            insert_sql = """insert into iplist(http_type,ip,port,speed) values(%s,%s,%s,%s)"""
            cursor.execute(insert_sql,((http_type,td_ip,td_port,speed)))
            conn.commit()
            print(td_ip)
    conn.close()


class GetIP(object):
    def delete_ip(self,ip):
        #从数据库中删除无效的ip
        delete_sql = """delete from iplist where ip=%s"""
        cursor.execute(delete_sql,(ip))
        conn.commit()
        return True

    def judge_ip(self,http_type,ip,port):
        #判断ip是否可用
        http_url = "http://www.baidu.com"
        proxy_url = "{0}://{1}:{1}".format(http_type,ip,port)
        try:
            proxy = {'http_type': ip+":"+str(port)}
            response = requests.get(http_url,proxies=proxy)
        except Exception as e:
            print("Invalid ip and port")
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print('effective ip')
                return True
            else:
                print("Invalid ip and port")
                self.delete_ip(ip)
                return False

    def get_random_ip(self):
        #从数据库随机取一个可用ip
        random_sql = """
        select http_type,ip,port from iplist order by rand() limit 1
        """
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            http_type = ip_info[0]
            ip = ip_info[1]
            port = ip_info[2]

            judge_re = self.judge_ip(http_type,ip,port)
            if judge_re:
                return http_type+"://"+ip+":"+str(port)
            else:
                return self.get_random_ip()

if __name__ == "__main__":
    crawl_ips()
    getip = GetIP()
    print(getip.get_random_ip())