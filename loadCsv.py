import pandas as pd
import os
import base64
import uuid
import pandas as pd
import os
from phone import Phone
from pyecharts import Pie
from detect import CardRecognition
def create_all_dada_csv_file():
    f = open("all_data.csv", 'w')
    f.close()
    df = pd.DataFrame(columns=(
        "ID", "base64_data_path", "code", "result", "name", "title", "mobile", "tel", "degree", "dept", "comp", "web",
        "post", "addr", "fax", "other",
        "numOther", "extTel", "mbox", "htel", "email", "im"))
    df.to_csv("all_data.csv", sep=',')

# 用于拆分字符串
def split_list(str):
    lists = str.split(',')
    for i in range(len(lists)):
        if "[" in lists[i]:
            lists[i] = lists[i].replace("[", "")
        if "]" in lists[i]:
            lists[i] = lists[i].replace("]", "")
        if "'" in lists[i]:
            lists[i] = lists[i].replace("'", "")
        lists[i] = lists[i].strip()
    return lists

# 用于将接口返回的结果转换成字典
def toDic(row):
    dic = {}
    dic['ID'] = row['ID']
    dic['base64_data_path'] = row['base64_data_path']
    dic['code'] = row['code']
    dic['result'] = row['result']
    dic['name'] = split_list(str(row['name']))
    dic['title'] = split_list(str(row['title']))
    dic['mobile'] = split_list(str(row['mobile']))
    dic['tel'] = split_list(str(row['tel']))
    dic['degree'] = split_list(str(row['degree']))
    dic['dept'] = split_list(str(row['dept']))
    dic['comp'] = split_list(str(row['comp']))
    dic['web'] = split_list(str(row['web']))
    dic['post'] = split_list(str(row['post']))
    dic['addr'] = split_list(str(row['addr']))
    dic['fax'] = split_list(str(row['fax']))
    dic['other'] = split_list(str(row['other']))
    dic['numOther'] = split_list(str(row['numOther']))
    dic['extTel'] = split_list(str(row['extTel']))
    dic['mbox'] = split_list(str(row['mbox']))
    dic['htel'] = split_list(str(row['htel']))
    dic['email'] = split_list(str(row['email']))
    dic['im'] = split_list(str(row['im']))
    return dic

def num():
    p=['1','what']
    print(type(p))

# 输入姓名关键字，搜索符合条件的信息。返回一个列表，列表里面是字典
# 字典中，ID，base64_data_path，code，result是字符串类型，其它元素都是列表类型
def search_information(keyword=""):
    if (os.path.exists("all_data.csv") == False):
        create_all_dada_csv_file()
    data = pd.read_csv("all_data.csv", index_col=0)
    result = []
    for i in range(data.shape[0]):
        temp = data.iloc[i]
        if keyword in temp['name'] or keyword in temp['ID']:
            result.append(toDic(temp))
    return result

# 给出ID，从本地删除指定的信息
def delet_specified_data(ID=""):
    if (os.path.exists("all_data.csv") == False):
        create_all_dada_csv_file()
    data = pd.read_csv("all_data.csv", index_col=0)
    base64_data_path = ID + ".txt"
    if os.path.exists(base64_data_path):
        os.remove(base64_data_path)
    data.drop(ID, inplace=True)
    data.to_csv("all_data.csv", sep=',')

def edit_data(theDIct):
    ID=theDIct['ID']
    name=theDIct['name']
    title=theDIct['title']
    mobile=theDIct['mobile']
    tel=theDIct['tel']
    degree=theDIct['degree']
    dept=theDIct['dept']
    comp=theDIct['comp']
    web=theDIct['web']
    post=theDIct['post']
    addr=theDIct['addr']
    fax=theDIct['fax']
    other=theDIct['other']
    numOther=theDIct['numOther']
    extTel=theDIct['extTel']
    mbox=theDIct['mbox']
    htel=theDIct['htel']
    email=theDIct['email']
    im=theDIct['im']
    if (os.path.exists("all_data.csv") == False):
        create_all_dada_csv_file()
    data = pd.read_csv("all_data.csv", index_col=0)
    if (len(name) != 0):
        data.loc[ID, 'name'] = str(name)
    if (len(title) != 0):
        data.loc[ID, 'title'] = str(title)
    if (len(mobile) != 0):
        data.loc[ID, 'mobile'] = str(mobile)
    if (len(tel) != 0):
        data.loc[ID, 'tel'] = str(tel)
    if (len(degree) != 0):
        data.loc[ID, 'degree'] = str(degree)
    if (len(dept) != 0):
        data.loc[ID, 'dept'] = str(dept)
    if (len(comp) != 0):
        data.loc[ID, 'comp'] = str(comp)
    if (len(web) != 0):
        data.loc[ID, 'web'] = str(web)
    if (len(post) != 0):
        data.loc[ID, 'post'] = str(post)
    if (len(addr) != 0):
        data.loc[ID, 'addr'] = str(addr)
    if (len(fax) != 0):
        data.loc[ID, 'fax'] = str(fax)
    if (len(other) != 0):
        data.loc[ID, 'other'] = str(other)
    if (len(numOther) != 0):
        data.loc[ID, 'numOther'] = str(numOther)
    if (len(extTel) != 0):
        data.loc[ID, 'extTel'] = str(extTel)
    if (len(mbox) != 0):
        data.loc[ID, 'mbox'] = str(mbox)
    if (len(htel) != 0):
        data.loc[ID, 'htel'] = str(htel)
    if (len(email) != 0):
        data.loc[ID, 'email'] = str(email)
    if (len(im) != 0):
        data.loc[ID, 'im'] = str(im)
    data.to_csv("all_data.csv", sep=',')
    return toDic(data.loc[ID])

# 将图片转换为base64编码
def picture_to_base64(img):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data


# 将base64编码转化为图片temp.png
def base64_to_picture(base64_data_path):
    with open(base64_data_path, "rb") as f:
        base64_data = f.read()
    imgdata = base64.b64decode(base64_data)
    with open("temp.png", 'wb') as f:
        f.write(imgdata)

# 手动添加联系人信息并存储在本地，执行成功后返回一个字典
# 调用示例：manually_enter_information(name=["赵昊"],mobile=['15184319620','13508197752'],comp=['UESTC'],email=['3481344335@qq.com'])
# 输入参数类型都是列表
def manually_enter_information(theDIct):

    ID = theDIct['ID']
    name=theDIct['name']
    title=theDIct['title']
    mobile=theDIct['mobile']
    tel=theDIct['tel']
    degree=theDIct['degree']
    dept=theDIct['dept']
    comp=theDIct['comp']
    web=theDIct['web']
    post=theDIct['post']
    addr=theDIct['addr']
    fax=theDIct['fax']
    other=theDIct['other']
    numOther=theDIct['numOther']
    extTel=theDIct['extTel']
    mbox=theDIct['mbox']
    htel=theDIct['htel']
    email=theDIct['email']
    im=theDIct['im']

    base64_data_path = ""
    code = ""
    result = ""
    if (os.path.exists("all_data.csv") == False):
        create_all_dada_csv_file()
    data = pd.read_csv("all_data.csv", index_col=0)
    data.loc[ID] = [ID, base64_data_path, code, result, name, title, mobile, tel, degree, dept, comp,
                    web, post, addr, fax, other, numOther, extTel, mbox, htel, email, im]
    data.to_csv("all_data.csv", sep=',')
    dic = toDic(data.loc[ID])
    return dic

# 创建或更新饼图
def update_graph():
    data = pd.read_csv("all_data.csv", index_col=0)
    phone_numbers = data['mobile']
    phone_list = []
    for i in range(len(phone_numbers)):
        temp_list = split_list(phone_numbers[i])
        for i in range(len(temp_list)):
            phone_list.append(temp_list[i])
    print(phone_list)
    province_list = []
    quantity_list = []
    for p in phone_list:
        if len(p) > 11 or len(p) < 7:
            continue
        p_info = Phone().find(p)
        if p_info is None:
            continue
        if p_info['province'] in province_list:
            quantity_list[province_list.index(p_info['province'])] += 1
        else:
            province_list.append(p_info['province'])
            quantity_list.append(1)
    pie = Pie("分布省份饼图", title_pos='center')

    pie.add(
        "",
        province_list,
        quantity_list,
        radius=[40, 75],
        label_text_color=None,
        is_label_show=True,
        is_more_utils=True,
        legend_orient="vertical",
        legend_pos="left"
    )
    pie.render(path="graph.html")

# 识别图片，返回一个字典。如果识别失败，会直接返回一个空字典
# 返回的字典中，ID，base64_data_path，code，result是字符串类型，其它元素都是列表类型
def identify_card(img_path=""):
    dic = {}
    r = CardRecognition()
    content = r.get_info(img_path)
    ID = uuid.uuid1()  # 每个名片信息在存入本地时，都会分配一个独有的ID，可以根据该ID检索名片信息
    base64_data = picture_to_base64(img_path)
    base64_data_path = str(ID) + ".txt"
    f = open(base64_data_path, "wb")
    f.write(base64_data)
    f.close()
    if (os.path.exists("all_data.csv") == False):
        create_all_dada_csv_file()
    data = pd.read_csv("all_data.csv", index_col=0)
    data.loc[ID] = [ID, base64_data_path, content["code"], content["result"], content["name"],
                    content["title"],
                    content["mobile"],
                    content["tel"], content["degree"], content["dept"], content["comp"],
                    content["web"], content["post"], content["addr"], content["fax"], content["other"],
                    content["numOther"], content["extTel"], content["mbox"], content["htel"],
                    content["email"],
                    content["im"]]
    data.to_csv("all_data.csv", sep=',')
    dic = toDic(data.loc[ID])
    return dic

def get_all_data():
    df = pd.read_csv("all_data.csv")
    rows=df.shape[0]

    res=[]

    for i in range(rows):
        das= df.iloc[i]
        theRes=toDic(das)
        res.append(theRes)


    return res

