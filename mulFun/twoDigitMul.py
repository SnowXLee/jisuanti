import random
import sys
sys.path.append(r'..')
from generalFun import general

#两位数乘两位数——two mul two
def twMTw(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bcsL = general.random_int_list(10, 99, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  csL = general.random_int_list(10, 99, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  #获得题与答案
  for i in range(n):
    dsL.append(str(bcsL[i] * csL[i]))
    ystL.append(str(bcsL[i]) + '×' + str(csL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#十位相同个位互补的两位数相乘——十同个补
def stgb(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  swsL = general.random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  gwsL = general.random_int_list(0, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  
  #获得十位相同个位互补的乘数与被乘数的题的列表；以及获得得数列表
  for i in range(n):
    dsL.append(str((swsL[i] * 10 + gwsL[i]) * (swsL[i] * 10 + (10 - gwsL[i]))))
    ystL.append(str((swsL[i] * 10 + gwsL[i])) + '×' + str((swsL[i] * 10 + (10 - gwsL[i]))))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#个位相同十位互补的两位数相乘——个同十补
def gtsb(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  gwsL = general.random_int_list(0, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  swsL = general.random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  
  #获得个位相同十位互补的乘数与被乘数的题的列表；以及获得得数列表
  for i in range(n):
    dsL.append(str((swsL[i] * 10 + gwsL[i]) * ((10 - swsL[i]) * 10 + gwsL[i])))
    ystL.append(str(swsL[i] * 10 + gwsL[i]) + '×' + str((10 - swsL[i]) * 10 + gwsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#十位相同的两位数相乘——十位相同
def swxt(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  swsL = general.random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  gwsL = general.random_int_list(0, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表

  #获得十位相同的两位数的乘数与被乘数的题的列表；以及获得得数列表
  for i in range(n):
    dsL.append(str((swsL[i] * 10 + random.randint(0, 9)) * (swsL[i] * 10 + random.randint(0, 9))))
    ystL.append(str((swsL[i] * 10 + random.randint(0, 9))) + '×' + str(swsL[i] * 10 + random.randint(0, 9)))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#一个数首尾相同与另一个首尾互补的两位数相乘——首尾同首尾补
def swtSwb(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  gwsL = general.random_int_list(1, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  swsL = general.random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  
  #获得首尾同首尾补的乘数与被乘数的题的列表；以及获得得数列表
  #首尾相同的两位数用个位数列表gwsL的数，首尾互补的两位数用十位数列表swsL的数
  for i in range(n):
    #随机数等于0首尾同的数在“×”前面，随机数等于1首尾补的数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(swsL[i] * 10 + swsL[i]) + '×' + str((10 - gwsL[i]) * 10 + gwsL[i]))
    else:
      ystL.append(str((10 - gwsL[i]) * 10 + gwsL[i]) + '×' + str(swsL[i] * 10 + swsL[i]))
    dsL.append(str((swsL[i] * 10 + swsL[i]) * ((10 - gwsL[i]) * 10 + gwsL[i])))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#尾数为1的两位数相乘——尾1两位数乘
def w1LwMul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  gwsL = general.random_int_list(1, 9, n)  #乘数的十位数——生成一个存储尾数为1的两位数的十位数字的一个长度n的列表
  swsL = general.random_int_list(1, 9, n)  #被乘数的十位数——生成一个存储尾数为1的两位数十位数数字的一个长度n的列表
  
  #获得两个尾数为1的两位数列表；以及获得得数列表
  for i in range(n):
    ystL.append(str(gwsL[i] * 10 + 1) + '×' + str(swsL[i] * 10 + 1))
    dsL.append(str((gwsL[i] * 10 + 1) * (swsL[i] * 10 + 1)))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#接近100的数字相乘——接近100相乘
def jj100Mul(n):
  print("思考何为接近100的数，什么范围的数更适合这个方法")
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  gwsL = general.random_int_list(80, 120, n)  #被乘数列表——生成一个存储80~120范围内的一个长度n的列表
  swsL = general.random_int_list(80, 120, n)  #乘数列表——生成一个存储80~120范围内的一个长度n的列表
  
  #获得两个接近接近100的数相乘的列表；以及获得得数列表
  for i in range(n):
    ystL.append(str(gwsL[i]) + '×' + str(swsL[i]))
    dsL.append(str(gwsL[i] * swsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk
  
#接近50的数字相乘——接近50相乘
def jj50Mul(n):
  print("思考何为接近50的数，什么范围的数更适合这个方法")
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  gwsL = general.random_int_list(30, 70, n)  #被乘数列表——生成一个存储30~70范围内的一个长度n的列表
  swsL = general.random_int_list(30, 70, n)  #乘数列表——生成一个存储30~70范围内的一个长度n的列表
  
  #获得两个接近接近50的数相乘的列表；以及获得得数列表
  for i in range(n):
    ystL.append(str(gwsL[i]) + '×' + str(swsL[i]))
    dsL.append(str(gwsL[i] * swsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#任意数与9相乘——任意数乘9（n是任意数、Mul是乘、9是乘数或者被乘数）
def n9Mul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  swsL = general.random_int_list(10, 99, n/4) + general.random_int_list(100, 999, n/4) + general.random_int_list(1000, 9999, n/4) + general.random_int_list(10000, 99999, n/4) #四位数以内任意数，该任意数等分成4份其中一份是两位数任意数、一份三位数任意数、一份四位数任意数、一份五位数任意数——生成以上任意数的一个长度n的列表
  
  #获得任意数乘9的计算题列表；以及获得得数列表
  for i in range(n):
    #随机数等于0数9“×”前面，随机数等于1任意数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(swsL[i]) + '×' + str(9))
    else:
      ystL.append(str(9) + '×' + str(swsL[i]))
    dsL.append(str(9 * swsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#任意数与99相乘——任意数乘99（n是任意数、Mul是乘、99是乘数或者被乘数）
def n99Mul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bcsL = general.random_int_list(10, 99, n/4) + general.random_int_list(100, 999, n/4) + general.random_int_list(1000, 9999, n/4) + general.random_int_list(10000, 99999, n/4) #四位数以内任意数，该任意数等分成4份其中一份是两位数任意数、一份三位数任意数、一份四位数任意数、一份五位数任意数——生成以上任意数的一个长度n的列表
  
  #获得任意数乘99的计算题列表；以及获得得数列表
  for i in range(n):
    #随机数等于0数99“×”前面，随机数等于1任意数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(bcsL[i]) + '×' + str(99))
    else:
      ystL.append(str(99) + '×' + str(bcsL[i]))
    dsL.append(str(99 * bcsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#任意数与999相乘——任意数乘999（n是任意数、Mul是乘、999是乘数或者被乘数）
def n999Mul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  bcsL = general.random_int_list(10, 99, n/4) + general.random_int_list(100, 999, n/4) + general.random_int_list(1000, 9999, n/4) + general.random_int_list(10000, 99999, n/4) #四位数以内任意数，该任意数等分成4份其中一份是两位数任意数、一份三位数任意数、一份四位数任意数、一份五位数任意数——生成以上任意数的一个长度n的列表
  
  #获得任意数乘999的计算题列表；以及获得得数列表
  for i in range(n):
    #随机数等于0数999“×”前面，随机数等于1任意数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(bcsL[i]) + '×' + str(999))
    else:
      ystL.append(str(999) + '×' + str(bcsL[i]))
    dsL.append(str(999 * bcsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#11~19中的整数相乘——十一到十九相乘eTnXc
def eTNMul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  gwsL = general.random_int_list(11, 19, n)  #被乘数列表——生成一个存储11~19范围内的一个长度n的列表
  swsL = general.random_int_list(11, 19, n)  #乘数列表——生成一个存储11~19范围内的一个长度n的列表
  
  #获得两个11~19的数相乘的列表；以及获得得数列表
  for i in range(n):
    ystL.append(str(gwsL[i]) + '×' + str(swsL[i]))
    dsL.append(str(gwsL[i] * swsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#两位数混合运算——two mix mul
def twMixMul(n):
  print("还没写好")