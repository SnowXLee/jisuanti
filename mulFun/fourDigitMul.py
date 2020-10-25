import random
import sys
sys.path.append(r'..')
from generalFun import general

#四位数与两位数相乘——four two mul
def foTwMul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  foL = general.random_int_list(1000, 9999, n)  #四位数列表，有n个四位数
  twL = general.random_int_list(10, 99, n)  #两位数列表，有n个两位数
  
  #获得题与答案
  for i in range(n):
    #随机数等于0数四位数“×”前面，随机数等于1两位数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(foL[i]) + '×' + str(twL[i]))
    else:
      ystL.append(str(twL[i]) + '×' + str(foL[i]))
    dsL.append(str(foL[i] * twL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#四位数乘以三位数——four three mul
def foThMul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  foL = general.random_int_list(1000, 9999, n)  #四位数列表，有n个四位数
  thL = general.random_int_list(100, 999, n)  #三位数列表，有n个三位数
  
  #获得题与答案
  for i in range(n):
    #随机数等于0数四位数“×”前面，随机数等于1三位数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(foL[i]) + '×' + str(thL[i]))
    else:
      ystL.append(str(thL[i]) + '×' + str(foL[i]))
    dsL.append(str(foL[i] * thL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#四位数乘四位数——four four mul
def foFoM(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bcsL = general.random_int_list(1000, 9999, n)  #四位数列表，有n个四位数
  csL = general.random_int_list(1000, 9999, n)  #四位数列表，有n个四位数
  #获得题与答案
  for i in range(n):
    dsL.append(str(bcsL[i] * csL[i]))
    ystL.append(str(bcsL[i]) + '×' + str(csL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk