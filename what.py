import sys
import os
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import loadCsv

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class DragLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(None, parent)
        self.setAcceptDrops(True)
        self.model = False

    def dragEnterEvent(self,e):
        # e = QDragEnterEvent()  # type:QDragEnterEvent

        path = e.mimeData().text()
        self.path = path[8:]
        pixel = QPixmap(self.path)
        self.setPixmap(pixel)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        res = loadCsv.identify_card(img_path=self.path)
        if res == {}:
            print("识别失败")
        else:
            self.dictV = res
            self.model = True
            print("识别成功")


class Ui_MainWindow(object):
    """
    自动生成的代码, 请不要修改
    """

    def addOne(self, theDict):
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1150, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(25, 70, 500, 500))
        self.listWidget.setObjectName("listWidget")
        self.searchline = QtWidgets.QLineEdit(self.centralwidget)
        self.searchline.setGeometry(QtCore.QRect(25, 10, 500, 30))

        self.searchB = QtWidgets.QPushButton(self.centralwidget)
        self.searchB.setGeometry(QtCore.QRect(535, 10, 60, 60))

        self.html = QtWidgets.QPushButton(self.centralwidget)
        self.html.setGeometry(QtCore.QRect(535, 70, 60, 60))

        self.addNew = QPushButton(self.centralwidget)
        self.addNew.setGeometry(QtCore.QRect(535, 130, 60, 60))

        self.commit = QPushButton(self.centralwidget)
        self.commit.setGeometry(QtCore.QRect(535, 190, 60, 60))

        self.WriteNew = QPushButton(self.centralwidget)
        self.WriteNew.setGeometry(QtCore.QRect(535, 250, 60, 60))


        self.putUp = QPushButton(self.centralwidget)
        self.putUp.setGeometry(QtCore.QRect(600, 10, 200, 30))


        self.grid = QWidget(self.centralwidget)
        self.grid.setGeometry(QtCore.QRect(610, 70, 500, 500))

        self.gridlayout = QGridLayout(self.grid)

        self.draglabel = DragLabel(self.centralwidget)
        self.draglabel.setGeometry(QtCore.QRect(600, 70, 500, 500))
        self.pixel = QPixmap('./tt.png').scaled(500, 500)
        self.background=QPalette()
        self.background.setBrush(QPalette.Background,QBrush(QPixmap("./back.png")))
        # self.label=QLabel()
        # self.label.setPixmap(self.pixel)
        MainWindow.setPalette(self.background)
        self.draglabel.setPixmap(self.pixel)


        # self.palette = QPalette()
        # self.palette.setBrush(QPalette.Background, QBrush(QPixmap("./tt.jpg")))

        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(600, 10, 81, 31))
        # self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchB.setText("搜索")
        self.html.setText("地区\n可视化")
        self.commit.setText("提交")
        self.commit.setHidden(True)
        self.putUp.setText("编辑")
        self.WriteNew.setText("新增")
        self.WriteNew.setHidden(True)
        self.addNew.setText("载入至\nExcel")

        # self.other.setPalette(self.palette)


class Windows(QMainWindow, Ui_MainWindow):
    def get_item_wight(e, data):
        idFont = QFont("Microsoft YaHei")
        idFont.setPointSize(5)

        def getEditPart(data):
            # data

            layout_detail = QGridLayout()
            layout_detail.addWidget(QLabel(data[0]), 0, 0)
            layout_detail.addWidget(QLabel(data[1]), 0, 1)
            return layout_detail

        # # 读取属性

        # 总Widget
        # 左侧部分的设置
        wight = QWidget()
        layout_main = QGridLayout()

        layout_leftPart = QGridLayout()
        # 姓名这里是唯一的，不存在多个
        layout_leftPart.addWidget(QLabel(data['name'][0]), 0, 0)
        # 手机号存在多个可能，需要修改
        layout_leftPart.addWidget(QLabel(','.join(data['mobile'])), 1, 0)
        idQ = QLabel(str(data['ID']))
        idQ.setFont(idFont)
        layout_leftPart.addWidget(idQ, 2, 0)
        #
        # # 左侧部分在上面
        layoutDetail = QGridLayout()
        e.Eemail = getEditPart(["Email", ','.join(data['email'])])
        layoutDetail.addLayout(e.Eemail, 0, 0)
        e.Eaddr = getEditPart(["Address", ','.join(data['addr'])])
        layoutDetail.addLayout(e.Eaddr, 1, 0)
        e.Eim = getEditPart(["QQ", ','.join(data['im'])])
        layoutDetail.addLayout(e.Eim, 2, 0)

        layout_main.addLayout(layout_leftPart, 0, 0)
        layout_main.addLayout(layoutDetail, 0, 1)

        wight.setLayout(layout_main)  # 布局给wight
        wight.setObjectName(data['ID'])

        return wight  # 返回wight

    def editplace(self):
        self.gridlayout.addWidget(QLabel("姓名"), 0, 0)
        self.Pname = QLineEdit()
        self.gridlayout.addWidget(self.Pname, 0, 1)

        self.gridlayout.addWidget(QLabel("ID"), 1, 0)
        self.Pid = QLineEdit()
        self.Pid.setFocusPolicy(QtCore.Qt.NoFocus)  # 设置不可编辑
        self.gridlayout.addWidget(self.Pid, 1, 1, 1, 3)

        self.gridlayout.addWidget(QLabel("头衔"), 2, 0)
        self.Ptitle = QLineEdit()
        self.gridlayout.addWidget(self.Ptitle, 2, 1)

        self.gridlayout.addWidget(QLabel("手机"), 3, 0)
        self.Pmobile = QLineEdit()
        self.gridlayout.addWidget(self.Pmobile, 3, 1)

        self.gridlayout.addWidget(QLabel("电话"), 3, 2)
        self.Ptel = QLineEdit()
        self.gridlayout.addWidget(self.Ptel, 3, 3)

        self.gridlayout.addWidget(QLabel("学历"), 4, 0)
        self.Pdegree = QLineEdit()
        self.gridlayout.addWidget(self.Pdegree, 4, 1)

        self.gridlayout.addWidget(QLabel("部门"), 5, 2)
        self.Pdept = QLineEdit()
        self.gridlayout.addWidget(self.Pdept, 5, 3)

        self.gridlayout.addWidget(QLabel("公司"), 5, 0)
        self.Pcomp = QLineEdit()
        self.gridlayout.addWidget(self.Pcomp, 5, 1)

        self.gridlayout.addWidget(QLabel("网址"), 4, 2)
        self.Pweb = QLineEdit()
        self.gridlayout.addWidget(self.Pweb, 4, 3)

        self.gridlayout.addWidget(QLabel("邮编"), 6, 0)
        self.Ppost = QLineEdit()
        self.gridlayout.addWidget(self.Ppost, 6, 1)

        self.gridlayout.addWidget(QLabel("地址"), 7, 0)
        self.Paddr = QLineEdit()
        self.gridlayout.addWidget(self.Paddr, 7, 1, 1, 3)

        self.gridlayout.addWidget(QLabel("传真"), 6, 2)
        self.Pfax = QLineEdit()
        self.gridlayout.addWidget(self.Pfax, 6, 3)

        self.gridlayout.addWidget(QLabel("IM"), 0, 2)
        self.Pim = QLineEdit()
        self.gridlayout.addWidget(self.Pim, 0, 3)

        self.gridlayout.addWidget(QLabel("邮件"), 8, 0)
        self.Pemail = QLineEdit()
        self.gridlayout.addWidget(self.Pemail, 8, 1, 1, 3)

    def Update(self, theDict):  # 更新右侧的文本框

        self.theDict = theDict

        self.Pname.setText(''.join(theDict['name']))

        self.Pid.setText(''.join(theDict['ID']))

        self.Ptitle.setText(''.join(theDict['title']))

        self.Pmobile.setText(''.join(theDict['mobile']))

        self.Ptel.setText(''.join(theDict['tel']))

        self.Pdegree.setText(''.join(theDict['degree']))

        self.Pdept.setText(''.join(theDict['dept']))

        self.Pcomp.setText(''.join(theDict['comp']))

        self.Pweb.setText(''.join(theDict['web']))

        self.Ppost.setText(''.join(theDict['post']))

        self.Paddr.setText(''.join(theDict['addr']))

        self.Pfax.setText(''.join(theDict['fax']))

        self.Pim.setText(''.join(theDict['im']))

        self.Pemail.setText(''.join(theDict['email']))

    def __init__(self, data):
        super(Windows, self).__init__()
        self.setupUi(self)

    def add(self, data):
        length = len(data)
        self.listWidget.clear()
        for i in range(length):
            item = QListWidgetItem()  # 创建QListWidgetItem对象
            item.setSizeHint(QSize(200, 150))  # 设置QListWidgetItem大小
            widget = self.get_item_wight(data[i])  # 调用上面的函数获取对应
            self.listWidget.addItem(item)  # 添加item
            self.listWidget.setItemWidget(item, widget)  # 为item设置widget

    def addOne(self, theDict):
        item = QListWidgetItem()  # 创建QListWidgetItem对象
        item.setSizeHint(QSize(200, 150))  # 设置QListWidgetItem大小
        widget = self.get_item_wight(theDict)  # 调用上面的函数获取对应
        self.listWidget.addItem(item)  # 添加item
        self.listWidget.setItemWidget(item, widget)  # 为item设置widget

# data=[]
# app = QtWidgets.QApplication(sys.argv)
# windows = Windows(data)
# windows.show()
# sys.exit(app.exec_())
