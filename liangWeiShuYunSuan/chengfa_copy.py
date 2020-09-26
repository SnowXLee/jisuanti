import random

def random_int_list(start, stop, length):
  start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  length = int(abs(length)) if length else 0
  random_list = []
  for i in range(length):
    random_list.append(random.randint(start, stop))
  return random_list

#基础两位数乘法——基础两位数乘
def jclwsc(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bcsL = random_int_list(10, 99, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  csL = random_int_list(10, 99, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  #获得题与答案
  for i in range(n):
    dsL.append(bcsL[i] * csL[i])
    ystL.append(str(bcsL[i]) + '×' + str(csL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#十位相同个位互补的两位数相乘——十同个补
def stgb(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  swsL = random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  gwsL = random_int_list(0, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  
  #获得十位相同个位互补的乘数与被乘数的题的列表；以及获得得数列表
  for i in range(n):
    dsL.append((swsL[i] * 10 + gwsL[i]) * (swsL[i] * 10 + (10 - gwsL[i])))
    ystL.append(str((swsL[i] * 10 + gwsL[i])) + '×' + str((swsL[i] * 10 + (10 - gwsL[i]))))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#个位相同十位互补的两位数相乘——个同十补
def gtsb(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  gwsL = random_int_list(0, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  swsL = random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  
  #获得个位相同十位互补的乘数与被乘数的题的列表；以及获得得数列表
  for i in range(n):
    dsL.append((swsL[i] * 10 + gwsL[i]) * ((10 - swsL[i]) * 10 + gwsL[i]))
    ystL.append(str(swsL[i] * 10 + gwsL[i]) + '×' + str((10 - swsL[i]) * 10 + gwsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#十位相同的两位数相乘——十位相同
def swxt(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  swsL = random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  gwsL = random_int_list(0, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表

  #获得十位相同的两位数的乘数与被乘数的题的列表；以及获得得数列表
  for i in range(n):
    dsL.append((swsL[i] * 10 + random.randint(0, 9)) * (swsL[i] * 10 + random.randint(0, 9)))
    ystL.append(str((swsL[i] * 10 + random.randint(0, 9))) + '×' + str(swsL[i] * 10 + random.randint(0, 9)))
  tk.append(ystL)
  tk.append(dsL)
  return tk


#