#从一个目录页里，把各个章节的列表下载下来
#适合各个章节的url不连续的情况，从列表menulist.txt里读取每篇文章的地址，
# txt format : utf8-nobom

import urllib.request
import requests
import urllib.parse
import os
from bs4 import BeautifulSoup


os.chdir(".")


def get_domain_by_urllib(url): # such as https://123.com/a/b 拆分url
    usche = urllib.parse.urlparse(url).scheme  #https
    unetl = urllib.parse.urlparse(url).netloc  # www.123.com
    upath = urllib.parse.urlparse(url).path  # /2134/45/a.html
    uname = os.path.basename(upath)  # a.html
    suffix = os.path.splitext(uname)  # 'a','.html' 返回列表2个值。
    # 如果结尾不是.aaa 而是路径/结尾则返回空串, 如果是/aaaa 结尾则返回aaaa, ''
    # https://blog.csdn.net/u014603907/article/details/98881984
    # 返回suffix主要是用于判断是不是要下载一个文件，例如图片或者视频
    return usche + "://" + unetl, uname, suffix


# 返回整理后的目录列表

def GetMenuHtml(url):
    myheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',}
    requests.packages.urllib3.disable_warnings()  # disable https warnings
    # see:https://blog.csdn.net/memory_qianxiao/article/details/82011282
    response = requests.get(url, headers=myheader, verify=False)
    #如果服务器有反爬虫就加上这个 see:https://blog.csdn.net/win_turn/article/details/77142100
    # print("Encoding: ", response.encoding, "ApparentEncoding: ", response.apparent_encoding)
    
    retcode = response.status_code
    if retcode!=200:
        print("Error! Return from server: s%", retcode)
        return ("Error s%", retcode)

    htmlEncoding = response.apparent_encoding    
    response.encoding = htmlEncoding
    # print(htmlEncoding)
    data = response.text
    
    # print(data[100:200], "=======")

    # get bookname、author info
    bookid = 'book'

    # 目录页面-查看源代码里正文菜单的区段 例如 <div id="list"> 则输入list
    divId = "listmain" #input("Please input the div-id of list: ")
    
    # 指定编码：当html为其他类型编码（非utf-8和asc ii），比如GB2312的话，则需要指定相应的字符编码，BeautifulSoup才能正确解析。
    # see https://blog.csdn.net/love666666shen/article/details/77512353
    soup = BeautifulSoup(data, 'lxml')  # https://www.qbiqu.com/7_7289/ #, from_encoding='gbk')
    # soup.prettify() #并不能去除排版用的空格缩进
    # listPart = soup.find(id=divId) #div用id
    bookinfo = soup.find(class_=bookid)
    # if bookinfo != None: #这里应该有严谨的判断
    bookinfo2 = bookinfo.find(class_='info')
    bookcoverurl = bookinfo.find('img').attrs['src']  # 封面图像

    bookname = bookinfo2.h1.text
    author = bookinfo.find(class_='small').span.text[3:]

    listPart = soup.find(class_=divId)  # div用class https://blog.csdn.net/dmxbb/article/details/109481444
    firstDD = listPart.dl

    listDict = dict()  # use dict to remove duplicateed lines
    #listDict[firstDD.a.attrs['href']] = firstDD.string
    #print(listDict.items())
    #input("Press Enter to continue, ctrl+c to stop!")

    for child in firstDD.descendants:  # dl 下的子孙节点，包括dt dd span
        # str = str.join(sibling.string)
        # if str.strip()!="":
        # https: // blog.csdn.net / haoxun05 / article / details / 104398259
        #print(type(sibling))
        if child.name == "dd":  #remove dt and spaces
            ddc = child.get('class')
            if ddc == None:
                # print(sibling.text)
                listDict[child.a.attrs['href']] = child.string

            #str = str + urldomain + sibling.a.attrs['href'] + "|" + sibling.string + "\n" #整合成 string 模式
            #print(str)

    return bookname, author, listDict, bookcoverurl


def saveTxt2File(file_name, file_content_dict, domainstr=''): #https://www.cnblogs.com/themost/p/6603409.html
    # 注意windows文件命名的禁用符，比如 \
    str = ""
    with open(file_name, "a", encoding='utf-8') as f: #a追加模式
        for key in file_content_dict.keys():
            str = str + domainstr + key + '|' +file_content_dict.get(key) + "\n"
        #print(str)
        f.write(str)



if __name__ == '__main__':
    menuurl = input("Please input the url of bookmenu file:\n")
    if menuurl=="":
        os._exit(0)
        
    urldomain = get_domain_by_urllib(menuurl)
    print("domain:", urldomain)

    menuDict = GetMenuHtml(menuurl)
    print(menuDict)
    for key in menuDict:
        i = key.find("/")
        print(i)
        if i>=0: #url contain /
            print("have / at ", i)
            saveTxt2File(".\\menulist.txt", menuDict, urldomain)
        else: #dont contain /, add domain and path left
            print("No /")
            pp = os.path.split(menuurl)
            print(pp)
            # input()
            uu = os.path.split(menuurl)[0]+"/"
            print(uu)
            # input()
            saveTxt2File(".\\shuquge\\menulist.txt", menuDict, uu)
        break
    