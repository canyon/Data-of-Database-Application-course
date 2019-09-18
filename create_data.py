
'''
以下各表中的代码或编号列为char(6)，名称或类别列为varchar(20)，单价或金额列为numeric(10,2)，数量列为int，订购日期为日期类型datetime，所在城市列为varchar(16)。
（1）	杂志表Magazine(杂志代码Mno，杂志名称Mname，杂志类别Mtype，出版商所在城市Mcity，进货单价Miprice，订购单价Moprice)，其中，订购价格>进货价格，杂志类别：文学类、历史类、科技类等。主键为（杂志代码Mno）。
（2）	客户（杂志的订购单位信息）表Customer(客户代码Cno，客户名称Cname，客户所在城市Ccity，上级主管单位代码Sno，客户类别Ctype)，客户（单位）类别：政府单位、事业单位、企业单位等。主键为（客户代码Cno）。
（3）	杂志订购情况主表OrderH（订单编号Ono，客户代码Cno，订购日期Odate，订单货款金额合计OMsum，订单盈利金额合计OPsum)，主键为订单编号Ono。
（4）	杂志订购情况明细表OrderList（订单编号Ono，杂志代码Mno，订购数量Onum，进货单价Miprice，订购单价Moprice，订购金额Omoney，盈利金额Oprofit)，主键为(订单编号Ono，杂志代码Mno)，订购金额=订购单价×订购数量，盈利金额=（订购单价-进货单价）×订购数量。
'''
from bs4 import BeautifulSoup
import requests
import random

# Magazine
class Magazine:
    def __init__(self, mno, mname, mtype, mcity, miprice, moprice):
        self.mno = mno
        self.mname = mname
        self.mtype = mtype
        self.mcity = mcity
        self.miprice = miprice
        self.moprice = moprice
class OrderList:
    def __init__(self, olno, mno, onum, miproce, moprice, omoney, oprofit):
        self.olno = olno
        self.mno = mno
        self.onum = onum
        self.miproce = miproce
        self.moprice = moprice
        self.omoney = omoney
        self.oprofit = oprofit
        
def create_magazine():
    mno = []
    mname = []
    mtype = ['文学类', '历史类', '科技类']
    mcity = []
    miprice = []
    moprice = []

    for i in range(1, 24 * 5 + 1):
        tmp = ''
        if i < 10:
            tmp = 'M00' + str(i)
        elif i >= 10 and i < 100:
            tmp = 'M0' + str(i)
        else:
            tmp = 'M' + str(i)
        mno.append(tmp)

    url = ['https://www.zazhi.com.cn/qikan/', 
            'https://www.zazhi.com.cn/qikan/s0l0l0l0l0l0l0l0l0l002.html', 
            'https://www.zazhi.com.cn/qikan/s0l0l0l0l0l0l0l0l0l003.html',
            'https://www.zazhi.com.cn/qikan/s0l0l0l0l0l0l0l0l0l004.html',
            'https://www.zazhi.com.cn/qikan/s0l0l0l0l0l0l0l0l0l005.html',
        ]
    for i in url:
        re = requests.get(i)
        re.encoding = 'utf-8'
        html = re.text
        soup = BeautifulSoup(html, 'lxml')

        mname += soup.find_all('h4')
        for div in soup.find_all('div', {'class' : 'list-c'}):
            div_ul_li = div.find('ul').find_all('li')
            mtype.append(div_ul_li[2].find_all('a')[0].text + '类')
            mcity.append(div_ul_li[3].find('a').text)
            tmp = div_ul_li[8].contents[1]
            moprice.append(tmp)
            miprice.append(int(float(tmp)) - random.randint(50, 200))
        #print(len(mname), len(mcity))
    mtype = list(set(mtype))

    magazines = []
    with open('magazine.txt', 'w') as f:
        for i in range(len(mno)):
            f.write('(\'' + mno[i] + '\',' + 
                    '\'' + mname[i].text[:10] + '\',' + 
                    '\'' + random.choice(mtype) + '\',' + 
                    '\'' + mcity[i] + '\',' + 
                    str(round(float(miprice[i]), 2)) + ',' + 
                    str(round(float(moprice[i]), 2)) + '),\n'
                )
            magazines.append(Magazine(mno[i], mname[i], random.choice(mtype), mcity[i], miprice[i], moprice[i]))

    return miprice, moprice

def create_Customer():
    cno = []
    cname = []
    ccity = []
    sno = []
    ctype = ['政府单位', '事业单位', '企业单位']

    for i in range(1, 24 * 5 + 1):
        tmp = ''
        if i < 10:
            tmp = 'C00' + str(i)
        elif i >= 10 and i < 100:
            tmp = 'C0' + str(i)
        else:
            tmp = 'C' + str(i)
        cno.append(tmp)
    sno = cno[::-1]
    
    url = ['https://www.zazhi.com.cn/qikan/', 
            'https://www.zazhi.com.cn/qikan/s0l0l0l0l0l0l0l0l0l002.html', 
            'https://www.zazhi.com.cn/qikan/s0l0l0l0l0l0l0l0l0l003.html',
            'https://www.zazhi.com.cn/qikan/s0l0l0l0l0l0l0l0l0l004.html',
            'https://www.zazhi.com.cn/qikan/s0l0l0l0l0l0l0l0l0l005.html',
        ]
    for i in url:
        re = requests.get(i)
        re.encoding = 'utf-8'
        html = re.text
        soup = BeautifulSoup(html, 'lxml')
        
        for div in soup.find_all('div', {'class' : 'list-c'}):
            div_ul_li = div.find('ul').find_all('li')
            cname.append(div_ul_li[1].find('a').text[:10])
            ccity.append(div_ul_li[3].find('a').text)
    
    ccity = ccity[::-1]
    magazines = []
    with open('customer.txt', 'a') as f:
        for i in range(len(cno)):
            f.write('(\'' + cno[i] + '\',' + 
                    '\'' + cname[i] + '\',' + 
                    '\'' + ccity[i] + '\',' + 
                    '\'' + sno[i] + '\',' + 
                    '\'' + random.choice(ctype) + '\'),\n'
                )
            # magazines.append(Magazine(mno[i], mname[i], random.choice(mtype), mcity[i], miprice[i], moprice[i]))

def create_OrderH_OrderList():
    olno = []
    cno = []
    odate = []

    year = range(2012, 2020)
    month = range(1, 13)
    day = range(1, 31)
    hour = range(25)
    minute = range(61)
    second = range(61)

    mno = list(range(120))
    onum = range(1, 101)
    ip, op = create_magazine()

    # 订单编号Ono && 客户代码Cno
    for i in range(1, 24 * 5 + 1):
        tmp = ''
        tmp1 = ''
        if i < 10:
            tmp = 'C00' + str(i)
            tmp1 = 'o00' + str(i)
        elif i >= 10 and i < 100:
            tmp = 'C0' + str(i)
            tmp1 = 'o0' + str(i)
        else:
            tmp = 'C' + str(i)
            tmp1 = 'o' + str(i)
        cno.append(tmp)
        olno.append(tmp1)

        # 订购日期Odate
        tmp_Y = random.choice(year)
        tmp_M = random.choice(month)
        tmp_D = random.choice(day)
        tmp_h = random.choice(hour)
        tmp_m = random.choice(minute)
        tmp_s = random.choice(second)
        
        if tmp_M < 10:
            tmp_M = '0' + str(tmp_M)
        if tmp_D < 10:
            tmp_D = '0' + str(tmp_D)
        if tmp_h < 10:
            tmp_h = '0' + str(tmp_h)
        if tmp_m < 10:
            tmp_m = '0' + str(tmp_m)
        if tmp_s < 10:
            tmp_s = '0' + str(tmp_s)
        odate.append(str(tmp_Y) + '-' + str(tmp_M) + '-' + str(tmp_D) + ' ' + str(tmp_h) + ':' + str(tmp_m) + ':' + str(tmp_s))
        
    # 创建子订单
    order_list = open('order_list.txt', 'w')
    sub_list = []
    for i in range(len(olno)):
        # 杂志代码Mno
        Mno = ''
        tmp_Mno = random.choice(mno)
        mno.pop(mno.index(tmp_Mno))

        if tmp_Mno < 10:
            Mno = 'M00' + str(tmp_Mno)
        elif tmp_Mno < 100 and tmp_Mno >= 10:
            Mno = 'M0' + str(tmp_Mno)
        else:
            Mno = 'M' + str(tmp_Mno)
        
        # 订购数量Onum && 价格
        Onum = random.choice(onum)

        miprice = float(ip[tmp_Mno])
        moprice = float(op[tmp_Mno])

        omoney = Onum * moprice

        oprofit = omoney - (Onum * miprice)

        tmp_olno = random.choice(olno)
        sub_list.append(OrderList(tmp_olno, Mno, Onum, miprice, moprice, omoney, oprofit))

        order_list.write('(\'' + tmp_olno + '\',' +
                    '\'' + Mno + '\',' +
                    str(Onum) + ', ' +
                    str(miprice) + ', ' +
                    str(moprice) + ', ' +
                    str(round(omoney, 3)) + ', ' +
                    str(round(oprofit, 3)) + '),\n'
                )
    order_list.close()

    # 创建总订单
    order_h = open('order_h.txt', 'w')
    for i in olno:
        omsum = 0
        opsum = 0
        flag = False
        for sub in sub_list:
            if sub.olno == i:
                flag = True
                omsum += sub.omoney
                opsum += sub.oprofit
        if flag:
            order_h.write('(\'' + i + '\',' +
                            '\'' + random.choice(cno) + '\',' +
                            '\'' + random.choice(odate) + '\',' +
                            str(round(omsum, 3)) + ', ' +
                            str(round(opsum, 3)) + '),\n'
                        )
        else:
            continue

    order_h.close()
    
    # 写入文件
    
create_Customer()
create_OrderH_OrderList()
