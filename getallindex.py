#书趣阁 www.shuquge.com 获取其所有的小说名称、作者、分类信息

import urllib.request
import requests
import urllib.parse
# import time
#import w3lib.html
import re
from bs4 import BeautifulSoup
import threading
import findbooklib

def get_file_by_urllib(u): #such as https://123.com
    return urllib.parse.urlparse(u).path


#用于清理文本的正则表达式
def fixtxt(data):
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))*')    # 匹配url模式

    #patterns = []
    #patterns.append( re.compile(r"<script>.+script>"))
    #patterns.append( re.compile(r"\d.+?>")) #关闭贪婪模式
    #print("patterns: " + patterns)
    
    #bad chars to remove
    newdata = data.replace(u'\xc2',"").replace(u'\xa0',"") #去掉奇怪的c2a0
    newdata = newdata.replace('　　',"") #去掉全角空格e38080
    newdata = newdata.replace("请记住本书首发域名：www.shuquge.com。书趣阁_笔趣阁手机版阅读网址：wap.shuquge.com", "")
    newdata = newdata.replace("天才一秒记住本站地址：.。顶点手机版阅读网址：m.", "")
    newdata = re.sub(pattern, "", newdata)
    # newdata = newdata.replace('     ',"<br/>\n") #去掉4空格
    newdata = newdata.replace('https:',"") #
    newdata = re.sub('[ ]+', "<br/>", newdata) #去掉段首空格
    #newdata = data.replace('\r', '').replace('\n\n', '<br />\n') #连续2个空行变成<br/>
    
    
    # print(url)
    return newdata



#通过一个url返回html内容
def tryurl(url):
    requests.packages.urllib3.disable_warnings() #disable https warnings see:https://blog.csdn.net/memory_qianxiao/article/details/82011282
    myheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko','Connection':'close'}
    #{'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    response = requests.get(url, headers=myheader, verify=False)
    #(url=url, params={'param':'1'}, headers={'Connection':'close'}) #https://blog.csdn.net/qq_33446100/article/details/118113121
    
    #如果服务器有反爬虫就加上这个 see:https://blog.csdn.net/win_turn/article/details/77142100

    #get and set charset 第一行是实际得到的字符集，第二行是head里读出来的
    # print("Encoding: ", response.encoding, "ApparentEncoding: ", response.apparent_encoding)
    retcode = response.status_code
    if retcode!=200:
        print("Error! Return from server: s%", retcode)
        return (retcode, "error|"+url)

    htmlEncoding = response.apparent_encoding
    if htmlEncoding=='GB2312':
        htmlEncoding='GBK'
    response.encoding = htmlEncoding
    # print("Get charset: " + htmlEncoding)
    StatusCode = response.status_code
    # print("\nHTTP return: " + str(StatusCode))
    htmlcontent = response.text #content.decode(htmlEncoding)
    return StatusCode, htmlcontent

def threadSave(rangeu, amount):
    rangeu = rangeu #上限
    rangeb = rangeu + amount #下限 这个文件也会被处理
    allresult = ""
    dic = dict()
    for i in range(rangeu, rangeb):
        thisurl = baseurl + str(i) + "/index.html"
        print("\n", i, "/", rangeb-1, " ", thisurl, end=' ')
        ret = tryurl(thisurl)
        print(ret[0])
        if ret[0]==200:
            soup = BeautifulSoup(ret[1], 'lxml')
            metaPart = soup.find(class_='info')
            bookname = metaPart.h2.string
            # print("bookname:", bookname)
            author = metaPart.find(class_='small').contents[1].string.split("：")[1]
            # print("author:", author)
            booktype = metaPart.find(class_='small').contents[3].string.split("：")[1]
            # print("booktype:", booktype)
            dic[i] = bookname+"|"+author+"|"+booktype
            allresult = allresult + str(i)+"|"+dic[i] + "\n"
            print(str(i)+"|"+dic[i])
        else:
            allresult = allresult + str(i)+"|"+ret[1] + "\n" #如果报错则返回err串
    findbooklib.saveHtml(str(rangeu)+'_'+str(rangeu+amount-1)+'.txt', allresult)
    return allresult



if __name__ == '__main__':
    baseurl = "https://www.shuquge.com/txt/"

    # allresult = threadSave(5001, 1000)
    t1 = threading.Thread(target=threadSave, args=(10001,1000))
    t2 = threading.Thread(target=threadSave, args=(11001,1000))
    t3 = threading.Thread(target=threadSave, args=(12001,1000))
    t4 = threading.Thread(target=threadSave, args=(13001,1000))
    t5 = threading.Thread(target=threadSave, args=(14001,1000))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    h,f = findbooklib.htmlhead("书趣阁 www.shuquge.com")
    
