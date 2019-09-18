# Data of Database Application course

>    大连海事大学-SQL SERVER 数据库应用技术 实验内容和实验报告可以用到的数据

## 使用

1.  安装python3→[官网](https://www.python.org/downloads/)
2.  安装requests库：`pip install requests`
3.  将`create_data.py`下载或克隆到本地
4.  进入python文件的目录下，打开命令提示符，输入`python create_data.py `
5.  会在同级目录下生成4个文本文件，里面是用于数据库`insert`语句插入表的值

---

SQL SERVER 数据库应用技术
实验内容和实验报告要求


一．实验内容
1.	基础单项训练
教材第2章~第10章的【例题】
2.	综合实验训练
具体见下一页的实验报告内容，即【杂志订购数据库综合实验】。

二．实验报告提交要求
1.	提交时间
最后一次上机提交（第8周周一5-6节）。
2.	提交内容
	1)	实验报告纸质版
	(1)	封面信息填全打印，严禁手写
	(2)	更新目录，使目录内容页号必须至与正文内容页号一致
	(3)	所有页眉的“选课序号、姓名、学号、班级”必须打印，严禁手写
	(4)	实验步骤3.2、3.3.1、3.3.2和3.3.3的程序脚本必须手写（A4纸预留出足够空白页手写程序），打印无效；其余内容可以打印。
	2)	实验报告电子版
将以下三个文件压缩成[选课序号]_[姓名].rar文件
	（1）	实验报告word电子稿，文件名为[选课序号]_[姓名].doc
	（2）	数据库文件（OrderDb.mdf和OrderDb.ldf）
	（3）	功能实现的T-SQL脚本，文件名为[选课序号]_[姓名].sql


SQL SERVER 数据库应用技术

目    录

1.实验目的	1
2.实验内容	1
2.1 创建使用数据库（杂志订购数据库OrderDB）和表	1
2.2 T-SQL查询	1
2.3 存储过程、自定义函数和触发器编程	2
2.3.1存储过程实验	2
2.3.2自定义函数实验	2
2.3.3触发器实验	2
3.实验步骤	3
3.1 创建使用数据库（杂志订购数据库OrderDB）和表	3
3.2 T-SQL查询	3
3.3 存储过程、自定义函数和触发器编程	4
3.3.1存储过程实验	4
3.3.2自定义函数实验	5
3.3.3触发器实验	6
4.总结与体会	7



1.实验目的
（1）	创建与使用数据库。了解数据库及其各类逻辑对象、数据库的文件与文件组的概念；实践数据库的设计、创建、查看和维护等操作。
（2）	T-SQL查询。掌握SELECT查询命令，INSERT、UPDATE和DELETE等更新命令，及T-SQL对查询与更新命令的增强功能操作。
（3）	自定义函数、存储过程与触发器。实践练习自定义函数、存储过程和触发器的使用方法。
2.实验内容
完成一个杂志订购数据库综合实验，具体包括创建使用数据库（杂志订购数据库OrderDB）及其数据表、T-SQL查询、存储过程编程、自定义函数编程和触发器编程等实验内容。
2.1 创建使用数据库（杂志订购数据库OrderDB）和表
以下各表中的代码或编号列为char(6)，名称或类别列为varchar(20)，单价或金额列为numeric(10,2)，数量列为int，订购日期为日期类型datetime，所在城市列为varchar(16)。
（1）	杂志表Magazine(杂志代码Mno，杂志名称Mname，杂志类别Mtype，出版商所在城市Mcity，进货单价Miprice，订购单价Moprice)，其中，订购价格>进货价格，杂志类别：文学类、历史类、科技类等。主键为（杂志代码Mno）。
（2）	客户（杂志的订购单位信息）表Customer(客户代码Cno，客户名称Cname，客户所在城市Ccity，上级主管单位代码Sno，客户类别Ctype)，客户（单位）类别：政府单位、事业单位、企业单位等。主键为（客户代码Cno）。
（3）	杂志订购情况主表OrderH（订单编号Ono，客户代码Cno，订购日期Odate，订单货款金额合计OMsum，订单盈利金额合计OPsum)，主键为订单编号Ono。
（4）	杂志订购情况明细表OrderList（订单编号Ono，杂志代码Mno，订购数量Onum，进货单价Miprice，订购单价Moprice，订购金额Omoney，盈利金额Oprofit)，主键为(订单编号Ono，杂志代码Mno)，订购金额=订购单价×订购数量，盈利金额=（订购单价-进货单价）×订购数量。
2.2 T-SQL查询
实现如下查询功能前，请向所有数据表添加足够多的演示数据。求年份的函数为year( )，返回类型为int，年份=year（订购日期Odate）。
（1）	使用WITH公用表表达式查看客户名称为’珠江航运公司’在广州市的所有上级主管单位代码和单位名称。
（2）	查询客户名称为’天空网络公司’在2016年所订购的大于其最小订购数量的2倍的杂志代码、杂志名称及订购数量。
（3）	使用TOP和查询结果集别名表达式，查询杂志名称为’读者’、2016年订购数量为第4-10名的客户代码、客户名称和订购数量（设’读者’的订购客户数>=10）。 
（4）	用游标编程，求大连市的杂志在2019年的平均订购数量和总订购数量的功能，不能用COUNT、AVG和SUM函数。

2.3 存储过程、自定义函数和触发器编程
2.3.1存储过程实验
（1）	设计存储过程pGetMoney，实现统计某年份给定客户类别的订购金额合计的功能，输入参数是统计年份和客户类别，输出参数是订购金额合计。
（2）	编写一段T-SQL程序调用存储过程pGetMoney，输出2019年客户类别为’企业单位’的订购金额合计。
2.3.2自定义函数实验
（1）	设计自定义函数fGetProfit，实现统计某年份给定杂志类别的盈利金额合计的功能，输入参数是统计年份和杂志类别，输出参数是盈利金额合计。
（2）	编写一段T-SQL程序调用函数fGetProfit，输出2018年杂志类别为’科技类’的盈利金额合计。
2.3.3触发器实验
（1）	为杂志订购情况明细表OrderList定义一个【AFTER】触发器tr_after_OrderList，每插入一条订购情况明细记录（订单编号Ono，杂志代码Mno，订购数量Onum），自动根据杂志代码从杂志表获取该杂志的进货单价Miprice、订购单价Moprice，计算其订购金额Omoney和盈利金额Oprofit，同时自动计算订购情况主表OrderH的订单货款金额合计OMsum和订单盈利金额合计OPsum。其中，订购情况明细表OrderList的订购金额=订购单价×订购数量，盈利金额=（订购单价-进货单价）×订购数量
（2）	编写insert语句示例，验证触发器tr_after_OrderList效果。
（3）	禁用触发器tr_after_OrderList，再为杂志订购情况明细表OrderList设计一个【INSTEAD OF】触发器tr_instead_OrderList，完成（1）的同样功能。
（4）	编写insert语句示例，验证触发器tr_instead_OrderList效果。

3.实验步骤
按以上实验内容的要求，给出实验步骤，包括功能实现过程的简要文字说明、T-SQL语句、SQL Server Management Studio的运行结果截图等。
3.1 创建使用数据库（杂志订购数据库OrderDB）和表
{实验步骤}

3.2 T-SQL查询
{实验步骤}（A4纸预留出足够空白页手写程序）




3.3 存储过程、自定义函数和触发器编程
3.3.1存储过程实验
{实验步骤}（A4纸预留出足够空白页手写程序）

 

3.3.2自定义函数实验
{实验步骤}（A4纸预留出足够空白页手写程序）


3.3.3触发器实验
{实验步骤}（A4纸预留出足够空白页手写程序）

4.总结与体会
（总结实验对自己更透彻理解理论知识的作用，程序设计遇到的难题及解决方案，不足之处）