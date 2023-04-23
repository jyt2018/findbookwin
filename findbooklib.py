# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:12:29 2022

@author: sqlsam@126.com
"""
import os
import re
import requests


#for sigil use, create epub file, this func create a chapter divider string. sigil F6
def chapdiv():
    return '\n\n' + '<hr class="sigil_split_marker" />' + '\n\n'


#returen a html head and foot. include title
def htmlhead(title):
    h = '''<!DOCTYPE html>
<html dir="ltr" lang="zh" xml:lang="zh" xmlns="http://www.w3.org/1999/xhtml" xmlns:Web="http://schemas.live.com/Web/">
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<head>
<title>''' + title + "</title></head>\n<body>\n"

    # print(h)
    f = "\n</body>\n</html>\n"
    return h, f

#结构化的文本文件转换为dict, 输入为一个本地文件，每行两列信息；输出为dict
# for use of read menu file into a dict
def file2dict(filepath):
    listDict = dict()
    os.chdir(".")
    with open(filepath, encoding='utf-8') as f_menulist:
        try:
            lines = f_menulist.readlines()   #读取全部内容 ，并以列表方式返回  
            filesum = len(lines)    #一共有多少章，即目录文件有多少行
            print("Total: " + str(filesum) + " links in menulist")
    
            #读取全部或者一定的行数
            linesToRead = filesum
            #linesToRead = 13 #一次性会读取几章（menulist列表里多少行）行号相减再+1
            linesStart = 0 #从哪一行开始读取。从第一行开始则写0. 
            for i in range(linesStart, linesStart+linesToRead):  #linesToRead
                #获取网址和每章标题
                currentline = lines[i].split("|")
                currenturl = currentline[0]
                currenttitle = currentline[1].strip() # [0:len(currentline[1])-1] #NOT inliude CR/LF
                listDict[currenturl] = currenttitle
        finally:
            f_menulist.close()

    return listDict

#save string to a txt file https://www.cnblogs.com/themost/p/6603409.html
def saveHtml(file_name, file_content):
    # 注意windows文件命名的禁用符，比如 /
    with open(file_name, "a", encoding='utf-8') as f: #a追加模式
        f.write(file_content)

# 通过一个url返回html内容


def tryurl_txt(url):
    requests.packages.urllib3.disable_warnings()
    # disable https warnings see:https://blog.csdn.net/memory_qianxiao/article/details/82011282
    myheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
                'Connection': 'close'}
    # {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    # Chrome/91.0.4472.114 Safari/537.36'}
    response = requests.get(url, headers=myheader, verify=False)
    # (url=url, params={'param':'1'}, headers={'Connection':'close'})
    # https://blog.csdn.net/qq_33446100/article/details/118113121

    # 如果服务器有反爬虫就加上这个 see:https://blog.csdn.net/win_turn/article/details/77142100

    # get and set charset 第一行是实际得到的字符集，第二行是head里读出来的
    # print("Encoding: ", response.encoding, "ApparentEncoding: ", response.apparent_encoding)
    if response.status_code != 200:
        # print("Error! Return from server: %s", returncode)
        return response.status_code, "findbooklib-tryurl_txt() error: " + url
    else:
        html_encoding = response.apparent_encoding
        if html_encoding == 'GB2312':
            html_encoding = 'GBK'

        response.encoding = html_encoding
        html_content = response.text  # content.decode(htmlEncoding)

        return response.status_code, html_content

# 根据url返回二进制 比如image video


def tryurl_bin(url):
    requests.packages.urllib3.disable_warnings()
    # disable https warnings see:https://blog.csdn.net/memory_qianxiao/article/details/82011282
    myheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
                'Connection': 'close'}
    # {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    # Chrome/91.0.4472.114 Safari/537.36'}
    response = requests.get(url, headers=myheader, verify=False)
    # (url=url, params={'param':'1'}, headers={'Connection':'close'})
    # https://blog.csdn.net/qq_33446100/article/details/118113121

    # 如果服务器有反爬虫就加上这个 see:https://blog.csdn.net/win_turn/article/details/77142100

    # get and set charset 第一行是实际得到的字符集，第二行是head里读出来的
    # print("Encoding: ", response.encoding, "ApparentEncoding: ", response.apparent_encoding)

    if response.status_code != 200:
        # print("Error! Return from server: %s", returncode)
        return response.status_code, "findbooklib tryurl_bin() error: " + url
    else:
        binfile = response.content  # for download picture. see: https://zhuanlan.zhihu.com/p/149422113
        # with open(file_path, 'wb') as f:
        #     f.write()
        return response.status_code, binfile



# 用于清理文本的正则表达式
def fixtxt(data):
    # pattern1 = re.compile(r'(ps：.+)', re.MULTILINE)  # 匹配含有ps的那一段
    pattern2 = re.compile(r'(.*)(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))*)',
                          re.M)  # 匹配url模式
    pattern3 = re.compile(r'([.。]+\))', re.M)
    pattern4 = re.compile(r'(^[ |　]+)', re.M) # 段首空格
    pattern5 = re.compile(r'(^请收藏本站：https://www+)', re.M)

    # patterns = []
    # patterns.append( re.compile(r"<script>.+script>"))
    # patterns.append( re.compile(r"\d.+?>")) #关闭贪婪模式
    # print("patterns: " + patterns)

    # bad chars to remove
    newdata = data.replace(u'\xc2', "").replace(u'\xa0', "")  # 去掉奇怪的c2a0
    newdata = newdata.replace("　　请收藏本站：https://www.shuquge9.com。笔趣阁手机版：https://m.shuquge9.com", "")
    newdata = newdata.replace("天才一秒记住本站地址：.。顶点手机版阅读网址：m.", "")
    newdata = newdata.replace('　　', "<br />\r\n")  # 去掉全角空格e38080. 空格变回车
    # newdata = newdata.replace('\r ', "<br />\r")  # 0d 0A
    newdata = newdata.replace('手机用户请到阅读。\)\r\n', "")
    newdata = newdata.replace("7017k", "")

    # newdata = re.sub(pattern1, "", newdata)
    newdata = re.sub(pattern2, "", newdata)

    newdata = newdata.replace('\r    ', "<br />\n")  # 去掉4空格
    newdata = newdata.replace('https:', "")  #
    # newdata = re.sub('[ ]+', "</p><p>", newdata) #去掉段首空格

    newdata = re.sub(pattern3, "", newdata)
    newdata = re.sub(pattern4, "", newdata)
    newdata = re.sub(pattern5, "", newdata)
    # print(url)
    return newdata
