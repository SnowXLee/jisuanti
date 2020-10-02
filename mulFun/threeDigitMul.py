import random
import sys
sys.path.append(r'..')
from generalFun import general

#三位以上的数字与11相乘——three 11 mul
def th11Mul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  thDigL = general.random_int_list(100, 999, n)  #三位数列表
  
  #获得三位数乘11的计算题列表；以及获得得数列表
  for i in range(n):
    #随机数等于0数11“×”前面，随机数等于1三位数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(thDigL[i]) + '×' + str(11))
    else:
      ystL.append(str(11) + '×' + str(thDigL[i]))
    dsL.append(str(11 * thDigL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#三位以上的数字与111相乘——three 111 mul
def th111Mul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  thDigL = general.random_int_list(100, 999, n)  #三位数列表
  
  #获得三位数乘11的计算题列表；以及获得得数列表
  for i in range(n):
    #随机数等于0数111“×”前面，随机数等于1三位数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(thDigL[i]) + '×' + str(111))
    else:
      ystL.append(str(111) + '×' + str(thDigL[i]))
    dsL.append(str(111 * thDigL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#接近两百的数字相乘——接近200相乘
def jj200Mul(n):
  print("思考何为接近200的数，什么范围的数更适合这个方法")
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bcsL = general.random_int_list(180, 220, n)  #被乘数列表——生成一个存储180~220范围内的一个长度n的列表
  csL = general.random_int_list(180, 220, n)  #乘数列表——生成一个存储180~220范围内的一个长度n的列表
  
  #获得两个接近接近200的数相乘的列表；以及获得得数列表
  for i in range(n):
    ystL.append(str(bcsL[i]) + '×' + str(csL[i]))
    dsL.append(str(bcsL[i] * csL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#100~110中的整数相乘——mul 100 110
def mul100_110(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bcsL = general.random_int_list(100, 110, n)  #被乘数列表——生成一个存储100~110范围内的一个长度n的列表
  csL = general.random_int_list(100, 110, n)  #乘数列表——生成一个存储100~110范围内的一个长度n的列表
  
  #获得两个接近接近100的数相乘的列表；以及获得得数列表
  for i in range(n):
    ystL.append(str(bcsL[i]) + '×' + str(csL[i]))
    dsL.append(str(bcsL[i] * csL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#三位数与两位数相乘——three two mul
def thTwMul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  thL = general.random_int_list(100, 999, n)  #三位数列表，有n个三位数
  twL = general.random_int_list(10, 99, n)  #两位数列表，有n个两位数
  #获得题与答案
  for i in range(n):
    #随机数等于0数三位数“×”前面，随机数等于1两位数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(thL[i]) + '×' + str(twL[i]))
    else:
      ystL.append(str(twL[i]) + '×' + str(thL[i]))
    dsL.append(str(thL[i] * twL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#三位数乘以三位数——three three mul
def thThMul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bcsL = general.random_int_list(100, 999, n)  #三位数列表，有n个三位数
  csL = general.random_int_list(100, 999, n)  #三位数列表，有n个三位数
  #获得题与答案
  for i in range(n):
    dsL.append(str(bcsL[i] * csL[i]))
    ystL.append(str(bcsL[i]) + '×' + str(csL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk