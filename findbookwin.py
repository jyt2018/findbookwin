from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from bs4 import BeautifulSoup
import os
import time
# PySide6-uic demo.ui -o ui_demo.py
#
from findbooklib import *
from ui_findbookmain import Ui_MainWindow
from getbookmenulist import get_domain_by_urllib, GetMenuHtml

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.band()

    def band(self):
        self.ui.pb_anay.clicked.connect(self.anay_click)
        self.ui.pb_retrieve.clicked.connect(self.retr_click)

    def anay_click(self):
        menuurl = self.ui.le_url.text()
        self.ui.listWidget.clear()
        urldomain = get_domain_by_urllib(menuurl)  # 获取域名前段部分(http[s]://aaa.com 没有最后的/), 文件名, 扩展名
        u = menuurl.split('/')[-2]  # url最后的那串数字

        ret = GetMenuHtml(menuurl)  # return bookname, author, listDict, bookcoverurl

        self.ui.le_bookname.setText(ret[0]) # 这里应该再处理一下去掉路径不支持的字符
        self.ui.le_author.setText(str(ret[1]))
        self.ui.lb_status.setText(self.ui.lb_status.text() + u + ret[0])
        localpath = self.ui.lb_status.text()
        if not(os.path.exists(localpath)):
            os.makedirs(localpath, exist_ok=True)  # 递归创建
            # should use try ...
        coverimgurl = ret[3]
        self.ui.te_remove.setText(coverimgurl)  # book cover img url
        ext = get_domain_by_urllib(coverimgurl)
        print(ext)
        if ext[2][1] in ['.jpg', '.png']:
            retu = tryurl_bin(coverimgurl)
            if retu[0] == 200:
                with open(self.ui.lb_status.text()+'\\'+ext[1], 'wb') as f_bin:
                    f_bin.write(retu[1])
                    # 显示一下封面图像
                    pixmap = QtGui.QPixmap(self.ui.lb_status.text()+'\\'+ext[1])
                    self.ui.label_5.setPixmap(pixmap)
                    self.ui.label_5.setScaledContents(True)  # 图片自适应
        i = 1
        for key in ret[2]:
            self.ui.listWidget.addItem(urldomain[0] + key + '|' + ret[2][key])
            i = i + 1
        self.ui.groupBox.setTitle('Total: ' + str(self.ui.listWidget.count()))

    def retr_click(self):
        startln = int(self.ui.le_retriveln.text())
        basedir = self.ui.lb_status.text()
        bookindex = self.ui.le_url.text()
        count = self.ui.listWidget.count()
        contentid = self.ui.le_conid.text()
        basepath = self.ui.lb_status.text()
        for i in range(startln, count):
            time.sleep(1.0)
            self.ui.listWidget.setCurrentItem(self.ui.listWidget.item(i))
            # read one line from listwidget, get url & title
            currentline = self.ui.listWidget.item(i).text().split("|")
            currenturl = currentline[0]
            currenttitle = currentline[1].strip()  # [0:len(currentline[1])-1] #NOT inliude CR/LF
            print('line:' + str(i), end=' ')
            single_chapter_content = tryurl_txt(currenturl)
            if single_chapter_content[0] == 200:
                soup = BeautifulSoup(single_chapter_content[1], 'lxml')
                contentPart = soup.find(id=contentid)
                contentPart.p.extract()  # extract 返回值是清除的部分，contentPart 是留下的部分
                print('√', end=', ')
                fixedtxt = fixtxt(contentPart.text)
                h, f = htmlhead(currenttitle)
                stxt = h + "<h2>" + currenttitle + "</h2>\r" + fixedtxt + f
                pathfilename = basepath + '\\' + os.path.basename(currenturl)
                saveHtml(pathfilename, stxt)
            else:
                print(str(i))
                print(": " + single_chapter_content[1])
if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()
    app.exec()
