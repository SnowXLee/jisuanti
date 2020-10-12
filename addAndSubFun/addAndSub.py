import random
import sys
sys.path.append(r'..')
from generalFun import general

#两位数加法运算题——两位数加法two add two
def twATw(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11+12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(11, 99, n)  #被加数的两位数列表
  jsL = general.random_int_list(11, 99, n)  #加数的两位数列表
  #获得题与答案
  for i in range(n):
    dsL.append(str(bjsL[i] + jsL[i]))
    ystL.append(str(bjsL[i]) + '+' + str(jsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#三位数加两位数——three add three
def thATw(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11+12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = general.random_int_list(100, 999, n)  #被加数的三位数列表
  jsL = general.random_int_list(11, 99, n)  #加数的两位数列表
  #获得题与答案
  for i in range(n):
    #随机数等于0更高位数的在“+”前面，随机数等于1更高位数的在“+”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(jsL[i]) + '+' + str(bjsL[i]))
    else:
      ystL.append(str(bjsL[i]) + '+' + str(jsL[i]))
    dsL.append(str(bjsL[i] + jsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#三位数加法运算题——three add three
def thATh(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11+12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(100, 999, n)  #被加数的三位数列表
  jsL = general.random_int_list(100, 999, n)  #加数的三位数列表
  #获得题与答案
  for i in range(n):
    dsL.append(str(bjsL[i] + jsL[i]))
    ystL.append(str(bjsL[i]) + '+' + str(jsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#四位数加三位数——four add three
def foATh(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11+12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(1000, 9999, n)  #被加数的三位数列表
  jsL = general.random_int_list(100, 999, n)  #加数的两位数列表
  #获得题与答案
  for i in range(n):
    #随机数等于0更高位数的在“+”前面，随机数等于1更高位数的在“+”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(bjsL[i]) + '+' + str(jsL[i]))
    else:
      ystL.append(str(jsL[i]) + '+' + str(bjsL[i]))
    dsL.append(str(bjsL[i] + jsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#四位数加法运算题——four add four
def foAFo(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11+12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(1000, 9999, n)  #被加数的四位数列表
  jsL = general.random_int_list(1000, 9999, n)  #加数的四位数列表
  #获得题与答案
  for i in range(n):
    dsL.append(str(bjsL[i] + jsL[i]))
    ystL.append(str(bjsL[i]) + '+' + str(jsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#两位数减一位数运算题——two sub one
def twSOn(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11-12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(11, 99, n)  #被减数的两位数列表
  jsL = general.random_int_list(1, 9, n)  #减数的一位数列表
  #获得题与答案
  for i in range(n):
    dsL.append(str(bjsL[i] - jsL[i]))
    ystL.append(str(bjsL[i]) + '-' + str(jsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#两位数减法运算题——two sub two
def twSTw(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11-12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(11, 99, n)  #被减数的两位数列表
  jsL = general.random_int_list(11, 99, n)  #减数的两位数列表
  #获得题与答案
  for i in range(n):
    if bjsL[i] > jsL[i]:
      dsL.append(str(bjsL[i] - jsL[i]))
      ystL.append(str(bjsL[i]) + '-' + str(jsL[i]))
    else:
      dsL.append(str(jsL[i] - bjsL[i]))
      ystL.append(str(jsL[i]) + '-' + str(bjsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#三位数减两位数运算题——three sub two
def thSTw(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11-12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(100, 999, n)  #被减数的三位数列表
  jsL = general.random_int_list(11, 99, n)  #减数的两位数列表
  #获得题与答案
  for i in range(n):
    dsL.append(str(bjsL[i] - jsL[i]))
    ystL.append(str(bjsL[i]) + '-' + str(jsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#三位数减三位数运算题——three sub three
def thSTh(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11-12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(100, 999, n)  #被减数的三位数列表
  jsL = general.random_int_list(100, 999, n)  #减数的三位数列表
  #获得题与答案
  for i in range(n):
    if bjsL[i] > jsL[i]:
      dsL.append(str(bjsL[i] - jsL[i]))
      ystL.append(str(bjsL[i]) + '-' + str(jsL[i]))
    else:
      dsL.append(str(jsL[i] - bjsL[i]))
      ystL.append(str(jsL[i]) + '-' + str(bjsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#四位数减三位数减法——four sub three
def foSTh(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11-12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(1000, 9999, n)  #被减数的三位数列表
  jsL = general.random_int_list(100, 999, n)  #减数的三位数列表
  #获得题与答案
  for i in range(n):
    if bjsL[i] > jsL[i]:
      dsL.append(str(bjsL[i] - jsL[i]))
      ystL.append(str(bjsL[i]) + '-' + str(jsL[i]))
    else:
      dsL.append(str(jsL[i] - bjsL[i]))
      ystL.append(str(jsL[i]) + '-' + str(bjsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#四位数减四位数减法——four sub four
def foSFo(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11-12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bjsL = general.random_int_list(1000, 9999, n)  #被减数的三位数列表
  jsL = general.random_int_list(1000, 9999, n)  #减数的三位数列表
  #获得题与答案
  for i in range(n):
    if bjsL[i] > jsL[i]:
      dsL.append(str(bjsL[i] - jsL[i]))
      ystL.append(str(bjsL[i]) + '-' + str(jsL[i]))
    else:
      dsL.append(str(jsL[i] - bjsL[i]))
      ystL.append(str(jsL[i]) + '-' + str(bjsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk