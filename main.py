import sys

from PyQt5 import QtWidgets,QtWebEngineWidgets
import os
import uuid
from PyQt5.QtCore import QUrl,pyqtSignal

from what import Windows
import loadCsv


class Main_Windows(Windows):
    def __init__(self):
        super(Windows, self).__init__()
        self.setupUi(self)
        self.add(loadCsv.get_all_data())
        self.editplace()
        self.model = True
        print("欢迎进入该名片识别系统\n"
              "请在使用本系统时，不要打开all_data.csv文件，否则会有冲突")
        self.onclick()


    def onclick(self):
        self.html.clicked.connect(self.popWindow)
        #打开HTML图
        self.searchB.clicked.connect(self.search)
        #实现搜索功能
        self.putUp.clicked.connect(self.edit)

        self.commit.clicked.connect(self.commmit_onclick)
        self.addNew.clicked.connect(self.loadToExcel)
        self.WriteNew.clicked.connect(self.write)
        self.listWidget.itemClicked.connect(self.show_select_item)
        self.listWidget.itemDoubleClicked.connect(self.delete)

    def show_select_item(self):
        item=self.listWidget.currentItem()
        widget = self.listWidget.itemWidget(item)
        keyword=widget.objectName()
        print(str(keyword))
        res=loadCsv.search_information(keyword)
        print(res)
        if len(res) != 0:
            self.theDict = res
            self.draglabel.setHidden(True)
            self.putUp.setText("添加")
            self.commit.setHidden(False)
            self.model = False
            self.Update(res[0])
        else:
            print("搜索失误")


    def delete(self):
        recCode=QtWidgets.QMessageBox.question(self,"删除","你确定要删除吗",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if recCode == 65536:
            print("取消删除")
        else:
            item=self.listWidget.currentItem()
            widget = self.listWidget.itemWidget(item)
            keyword = widget.objectName()
            loadCsv.delet_specified_data(keyword)
            self.listWidget.takeItem(self.listWidget.row(item))

    def write(self):
        self.draglabel.setHidden(True)
        self.putUp.setText("添加")
        self.commit.setHidden(False)
        self.model = False
        self.theDict={'ID': '', 'base64_data_path': '', 'code': 0.0, 'result': '', 'name': [''], 'title': [''], 'mobile': [''], 'tel': [''], 'degree': [''], 'dept': [''], 'comp': [''], 'web': [''], 'post': [''], 'addr': [''], 'fax': [''], 'other': [''], 'numOther': [''], 'extTel': [''], 'mbox': [''], 'htel': [''], 'email': [''], 'im': ['']}
        self.Update(self.theDict)

    def loadToExcel(self):
        if self.draglabel.model==False:
            print("请拖入图片至框内")
        else:
            if len(self.draglabel.dictV)!=0:
                self.draglabel.model=False
                self.draglabel.setPixmap(self.pixel)
                print(self.draglabel.dictV)
                self.add(loadCsv.get_all_data())

    def commmit_onclick(self):

        if self.theDict['ID'] == self.Pid.text():
            self.theDict['ID']=self.Pid.text()
            self.theDict['name'] = self.Pname.text()
            self.theDict['mobile'] = self.Pmobile.text()
            self.theDict['title'] = self.Ptitle.text()
            self.theDict['tel'] = self.Ptel.text()
            self.theDict['degree'] = self.Pdegree.text()
            self.theDict['dept'] = self.Pdept.text()
            self.theDict['comp'] = self.Pcomp.text()
            self.theDict['web'] = self.Pweb.text()
            self.theDict['post'] = self.Ppost.text()
            self.theDict['addr'] = self.Paddr.text()
            self.theDict['fax'] = self.Pfax.text()
            self.theDict['im'] = self.Pim.text()
            self.theDict['email'] = self.Pemail.text()
            loadCsv.edit_data(self.theDict)

            self.add(loadCsv.get_all_data())
        elif self.theDict['ID']=='' or self.theDict['ID'] != self.Pid.text():
            self.theDict['ID']=str(uuid.uuid1())
            self.theDict['name'] = self.Pname.text()
            self.theDict['mobile'] = self.Pmobile.text()
            self.theDict['title'] = self.Ptitle.text()
            self.theDict['tel'] = self.Ptel.text()
            self.theDict['degree'] = self.Pdegree.text()
            self.theDict['dept'] = self.Pdept.text()
            self.theDict['comp'] = self.Pcomp.text()
            self.theDict['web'] = self.Pweb.text()
            self.theDict['post'] = self.Ppost.text()
            self.theDict['addr'] = self.Paddr.text()
            self.theDict['fax'] = self.Pfax.text()
            self.theDict['im'] = self.Pim.text()
            self.theDict['email'] = self.Pemail.text()
            loadCsv.manually_enter_information(theDIct=self.theDict)
            self.add(loadCsv.get_all_data())


    def edit(self):
        if self.model:
            #如果进入手动模式
            self.draglabel.setHidden(True)
            self.putUp.setText("返回图片上传模式")
            print("进入手动编辑模式")
            self.WriteNew.setHidden(False)
            self.commit.setHidden(False)
            self.model=False
        else:
            #图片上传模式
            print("进入图片上传模式")
            self.draglabel.setHidden(False)
            self.WriteNew.setHidden(True)
            self.putUp.setText("进入手动编辑模式")
            self.commit.setHidden(True)
            self.model=True

    def popWindow(self):
        loadCsv.update_graph()
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.browser.resize(800,600)
        # 指定打开界面的 URL
        self.browser.load(QUrl.fromLocalFile(os.path.abspath('.') + "/graph.html"))
        self.browser.show()
    def search(self):
        keyword=self.searchline.text()
        print(keyword)
        if keyword == "":
            print("请输入关键字")
        else:
            res=loadCsv.search_information(keyword)
            if len(res)!=0:
                self.theDict=res
                self.draglabel.setHidden(True)
                self.putUp.setText("添加")
                self.commit.setHidden(False)
                self.model = False
                self.Update(res[0])
            else:
                print("搜索失误")











app = QtWidgets.QApplication(sys.argv)
windows = Main_Windows()
windows.setWindowTitle("名片识别系统")
windows.show()
sys.exit(app.exec_())