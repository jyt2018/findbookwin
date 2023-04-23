# 适合各个章节的url不连续的情况，从外部文件 menulist.txt里读取每篇文章的地址

import urllib.request
import requests
import urllib.parse
import time
import os
#import w3lib.html
import re
from bs4 import BeautifulSoup
import findbooklib
import json


#结构化的文本文件转换为dict
def get_file_by_urllib(u): #such as https://123.com
    return urllib.parse.urlparse(u).path




#save string to a txt file https://www.cnblogs.com/themost/p/6603409.html

# =============================================================================
# def fixtxt(txtcontent, badchar, patterns):
#     soup = BeautifulSoup(txtcontent, features="lxml")
#     for k in soup.find_all('div', id_="content") :
#         #a = k.find_all()       #在每个对应li标签下找a标签
#         print(k.text)        #获取a标签下的第一个字符串
#         
#         #del soup.a['target','title']
#         #del soup.img['class']
# 
#         txtcontent = soup.text
#         print(soup)
# 
#     txtcontent = txtcontent.replace("<br/><br/>", "\n")
#     txtcontent = txtcontent.strip()
# 
# 
#     for t in badchar: #badchar from ini file
#         print("XX: "+t)
#         txtcontent = txtcontent.replace(t, "")
# 
#                     #print(txtcontent)
# 
#     for pattern in patterns: #patterns from ini file
#         print(str(pattern))
#         text = re.findall(pattern, txtcontent)
#         if text:
#             print("match: " + str(text))
#             for j in text:
#                 txtcontent = txtcontent.replace(j, "")
# 
#         txtcontent = soup.text       
#         return txtcontent #print(txtcontent)
# 
# 
# myheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',}
# 
# allchap = "" #几个章节合并成一个文件用
# =============================================================================

# =============================================================================
# def fixtitle(str):
#     ts = str.find("第",0,1)
#     #标题不是以第字开头
#     if ts==-1 :
#         str = "第"+str
#         te = str.find("章")
#         if te==-1:
#            a=1
#     else:
#         a=1
#         
# #main
# for i in range(linesStart, linesStart+linesToRead):  #linesToRead
#     #获取网址和标题
#     currentline = lines[i].split("|")
#     currenturl = currentline[0]
#     currenttitle = currentline[1].strip()#[0:len(currentline[1])-1] #NOT inliude cr/lf
#     
#     print("Line:"+str(i+1) + "***hacking: " + currenturl)
# 
#     StatusCode, htmlcontent = tryurl(currenturl)
#     #print(type(htmlcontent))
#     
#     j = 1.2 #计数器，返回非200，则sleep增加0.2秒，上限为2秒
#     while not(StatusCode==200): #get return correctly
#         if j>3:
#             sys.exit()
#         else:
#             j = j + 0.2
#             print(str(j) + " " + str(StatusCode))
#             time.sleep(0.8+j)
#             
#             StatusCode, htmlcontent = tryurl(currenturl)
#         
#     htmlcontent = htmlcontent.replace("<br/>", "\r\n")
#     htmlcontent = htmlcontent.replace("&nbsp;", "")
#     htmlcontent = htmlcontent.replace("<!--go-->","")
#     htmlcontent = htmlcontent.replace("<!--over-->","")
#     #saveHtml("1", htmlcontent)
#     soup = BeautifulSoup(htmlcontent, features="lxml")
#         
#         #htmlcontent = soup.prettify()
#         
# 
#     print('Finish：' + currenttitle + "\n") #print the title of chapter
# 
# 
#         #开始提取正文
#     txtcontent = ""
#     allli = ""
#     results = soup.select('#content')
#         #print("len:"+str(len(results)))
# 
#             #print(type(t))
#     allli = allli + currenttitle + "\n" + results[0].text + "\n"
#         #print(showsinthistype)
#         #print(showsinthistype)
#         
#         #saveHtml("2", showsinthistype)
#         #remove BOM if exist
# 
# 
#         # txtcontent = fixtxt(txtcontent, bc, patterns)
#         #     print(txtcontent)
#         #save current chapter to file
#     thischap = allli + "\n\n"
#         #保存单独的文章成一个文件
#     saveHtml(author+"_"+bookname+"_"+str(linesStart+1)+"-"+str(linesStart+linesToRead), thischap)
# 
#         #allchap = allchap + (esulstle+"\n\n"+thischap).encode('utf-8')
#         #allchap = allchap + thischap
#     time.sleep(1)
#     
#     #所有文章合并在一起并保存成文件
#     #allchap = allchap + "\n\n"
#     #saveHtml(author+"_"+bookname+"_"+str(linesStart+1)+"-"+str(linesStart+linesToRead), allchap)
# 
#     
# print("Done!")
# start_directory = r'.'
# os.startfile(start_directory)
# 
# =============================================================================


if __name__ == '__main__':
    basedir = "f:\\project\\"
    j = input("start line, default=1: ")
    lendic = input("total download, default=all: ")
    if j=="":
        j=1
    else:
        j = int(j)
    #lendic = len(listDict) #这里也可以指定一个数字，表示只读取n行就停止
    # read config file
    with open(basedir+"cfg.json", "rt", encoding="utf-8") as cfgfile:
        try:
            jsonfile = cfgfile.read()
            cfgobj = json.loads(jsonfile)
            
            bookname = cfgobj["bookname"]
            bookauth = cfgobj["bookauth"]
            #menuurl = cfgobj["menuurl"]
            menufile = cfgobj["menufile"]
            
        finally:
            cfgfile.close()
        
    listDict = file2dict(basedir + menufile)
    # print(listDict)
    if lendic=="":
        lendic = len(listDict) #一共处理的行数
    else:
        lendic = int(lendic)
    errcache = ""

    htmltitle = bookname + "-" + bookauth
    
    i = 0

    firstchap = 1
    for key,value in listDict.items(): #成功的写下文件，失败的列出列表
        i = i + 1

        if i<j:
            print("pass" + str(i), end=" ")
        else:
            print()
            singlecontent = findbooklib.tryurl_txt(key)
            uf = get_file_by_urllib(key) #以url的文件名作为落地文件名
            uf = os.path.basename(uf)
            #print(uf)
            
            if singlecontent[0]==200:
                print(i, "/", lendic+j-1, "-----------", uf, "-------------")
                # print(singlecontent[1][100:250], "\n")
                soup = BeautifulSoup(singlecontent[1], 'lxml')
                contentPart = soup.find(id='content')
                # print(contentPart.text)
                fixedtxt = fixtxt(contentPart.text)
                    # print(fixedtxt)
                stxt = "<h2>" + value + "</h2>\n" + fixedtxt
                h,f = htmlhead(htmltitle)
                if firstchap==1:
                    saveHtml(basedir+'out.xhtml', h)
                    firstchap = 0
                
                if i==lendic+j-1: #最后一章
                    saveHtml(basedir+'out.xhtml', stxt)
                    saveHtml(basedir+"out.xhtml", f)
                else:
                    saveHtml(basedir+'out.xhtml', stxt+findbooklib.chapdiv() )    #chapdiv是sigil的章节分割标识
            else:
                errcache = errcache + key + "|" + value + "\n"
                print("XXXXXXXXXXX", singlecontent[1], "XXXXXXXXXXXXX")
                time.sleep(1.0)# Don't access website so frecquently
            if i==lendic+j-1: #include 55th line in listfile
                print(errcache)
                break
# =============================================================================
#     menuDict = GetMenuHtml(myheader, menuurl)
#     saveTxt2File("menulist.txt", menuDict, urldomain)
# =============================================================================
