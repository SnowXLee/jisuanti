import random
import time

def random_int_list(start, stop, length):
  start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  length = int(abs(length)) if length else 0
  random_list = []
  for i in range(length):
    random_list.append(random.randint(start, stop))
  return random_list

#排版——排版出来的题本是二元列表
def pb(tb):
  #统计一个题本中有多少个种类的题型——txzl；题型的0及双数是题；题型的单数是答案，是单数减一的题的得数
  txzl = int(len(tb) / 2)  #tb题本——是一个一个二元列表包含该题本所包含的所有题型种类
  jstL = []  #题型的0及双数是计算题
  dsL = []  #题型的单数是得数，是单数减一的题的得数
  pbtb = []  #分离了得数与计算题的排版题本
  for i in range(len(tb)):
    if (i == 0) or ((i % 2) == 0):
      #将不同体型的计算题合并在一个一元列表里
      for j in range(len(tb[i])):
        jstL.append(tb[i][j])
    elif (i % 2) != 0:
      for k in range(len(tb[i])):
        dsL.append(tb[i][k])
  pbtb.append(jstL)
  pbtb.append(dsL)
  return pbtb

#打印
def dy(tb):
  #参数依然是题本类似这种 abc = foafo(4) + thath(4) + twstw(4)
  pbL = pb(tb)  #排版列表经过排版后的题本二元列表
  jstTbL = pbL[0]  #从排列后的题本列表中分割出计算题的部分
  dsTbL = pbL[1]  #从排列后的题本列表中分割出得数的部分
  outputTb = ""
  outputDs = ""
  #为列表的0号元素加两个空格
  jstTbL0 = "  " + jstTbL[0]
  jstTbL[0] = jstTbL0
  dsTbL0 = "  " + dsTbL[0]
  dsTbL[0] = dsTbL0
  jstTbL1 = []
  dsTbL1 = []
  i = 0
  for ts in range(len(jstTbL)):
    #ts题数tb中下标0的长度
    jstTbL1.append(jstTbL[ts])
    dsTbL1.append(dsTbL[ts])
    if (len(jstTbL1) == (4 + 5 * i)):
      jstTbL1.append("\n\n")
      dsTbL1.append("\n\n")
      i = i + 1
  outputTb = "  ".join(jstTbL1)
  outputDs = "  ".join(dsTbL1)
  #获取时间并将其作为文件名
  localtime = time.localtime(time.time())
  nyrhm = str(localtime.tm_year) + "年" + str(localtime.tm_mon) + "月" + str(localtime.tm_mday) + "日" + str(localtime.tm_hour) + "时" + str(localtime.tm_min) + "分"
  fTb = open("./mulExercise/" + nyrhm + "题" + ".txt", "w", encoding= 'utf-8')
  fDs = open("./mulExercise/" + nyrhm + "得数" + ".txt", "w", encoding= 'utf-8')
  fTb.write(outputTb)
  fDs.write(outputDs)
  # 关闭打开的文件，必须关闭不然电脑能炸裂
  fTb.close()
  fDs.close()

#两位数乘两位数——two mul two
def twMTw(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bcsL = random_int_list(10, 99, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  csL = random_int_list(10, 99, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
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
  swsL = random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  gwsL = random_int_list(0, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  
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
  gwsL = random_int_list(0, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  swsL = random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  
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
  swsL = random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  gwsL = random_int_list(0, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表

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
  gwsL = random_int_list(1, 9, n)  #个位数——生成一个存储个位数数字的一个长度n的列表
  swsL = random_int_list(1, 9, n)  #十位数——生成一个存储十位数数字的一个长度n的列表
  
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
  gwsL = random_int_list(1, 9, n)  #个位数——生成一个存储尾数为1的两位数的十位数字的一个长度n的列表
  swsL = random_int_list(10, 99, n)  #十位数——生成一个存储两位数数字的一个长度n的列表
  
  #获得尾数为1的两位数列表以及另一个两位数列表；以及获得得数列表
  #
  for i in range(n):
    #随机数等于0首尾同的数在“×”前面，随机数等于1首尾补的数在“×”后面
    if random.randint(0, 1) == 0:
      ystL.append(str(swsL[i]) + '×' + str(gwsL[i] * 10 + 1))
    else:
      ystL.append(str(gwsL[i] * 10 + 1) + '×' + str(swsL[i]))
    dsL.append(str((gwsL[i] * 10 + 1) * (swsL[i])))
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
  gwsL = random_int_list(80, 120, n)  #被乘数列表——生成一个存储80~120范围内的一个长度n的列表
  swsL = random_int_list(80, 120, n)  #乘数列表——生成一个存储80~120范围内的一个长度n的列表
  
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
  gwsL = random_int_list(30, 70, n)  #被乘数列表——生成一个存储30~70范围内的一个长度n的列表
  swsL = random_int_list(30, 70, n)  #乘数列表——生成一个存储30~70范围内的一个长度n的列表
  
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
  swsL = random_int_list(10, 99, n/4) + random_int_list(100, 999, n/4) + random_int_list(1000, 9999, n/4) + random_int_list(10000, 99999, n/4) #四位数以内任意数，该任意数等分成4份其中一份是两位数任意数、一份三位数任意数、一份四位数任意数、一份五位数任意数——生成以上任意数的一个长度n的列表
  
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

#11~19中的整数相乘——十一到十九相乘eTnXc
def eTnMul(n):
  #参数n为题数也就是乘数与被乘数的个数
  dsL = []  #得数列表
  ystL = []  #运算题列表11*12
  tk = []  #题库列表输出列表，下标1得数列表ds；下标0为题；
  gwsL = random_int_list(11, 19, n)  #被乘数列表——生成一个存储11~19范围内的一个长度n的列表
  swsL = random_int_list(11, 19, n)  #乘数列表——生成一个存储11~19范围内的一个长度n的列表
  
  #获得两个11~19的数相乘的列表；以及获得得数列表
  for i in range(n):
    ystL.append(str(gwsL[i]) + '×' + str(swsL[i]))
    dsL.append(str(gwsL[i] * swsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#两位数混合运算
def lwsHunHeMul(n):
  print("还没写好")

#启动函数，按提示输入相应选项即可导出相应类型的题目以及所需题数
def qidong():
  print("所有题数必须为4的倍数\n")
  print("1：两位数加两位数、2：三位数加两位数、3：三位数加三位数、4：四位数加三位数、5：四位数加四位数\n")
  print("17：两位数减一位数、18：两位数减两位数、19：三位数减两位数、20：三位数减三位数、21：四位数减三位数、22：四位数减四位数\n")
  print("33：两位数乘两位数、34：十同个补乘法、35：个同十补乘法、36：十位相同乘法、37：首尾同乘首尾补乘法、38：尾数为1的两位数相乘、39：接近100的数字相乘、40：接近50的数字相乘、41：任意数与9相乘（题数必须为4的倍数）、42：11~19中的整数相乘\n")
  tx = int(input("输入你需要的题型:"))  #题型
  #抛出错误题型不在上述范围内——不正确重新输入
  if ((tx <= 0) or (tx >= 64)):
    print("请重新输入正确的题型代号")
    qidong()
  ts = int(input("该题型所需题数:"))  #题数
  #抛出错误题型不在上述范围内——不正确重新输入（可能不需要）
  if (ts % 4 != 0):
    print("题数需为4的倍数，请重新输入")
    qidong()
  #1~16是加法，17~32是减法，33~48是乘法，49~64是除法
  if tx == 1:
    dy(twATw(ts))  #两位数加两位数
  elif tx == 2:
    dy(thATw(ts))  #三位数加两位数
  elif tx == 3:
    dy(thATh(ts))  #三位数加三位数
  elif tx == 4:
    dy(foATh(ts))  #四位数加三位数
  elif tx == 5:
    dy(foAFo(ts))  #四位数加四位数
  elif (6 <= tx) and (tx <= 16):
    print("暂无该加法的函数，待添加")
  elif tx == 17:
    dy(twSOn(ts))  #两位数减一位数
  elif tx == 18:
    dy(twSTw(ts))  #两位数减两位数
  elif tx == 19:
    dy(thSTw(ts))  #三位数减两位数
  elif tx == 20:
    dy(thSTh(ts))  #三位数减三位数
  elif tx == 21:
    dy(foSTh(ts))  #四位数减三位数
  elif tx == 22:
    dy(foSFo(ts))  #四位数减四位数
  elif (24 <= tx) and (tx <= 32):
    print("暂无该减法函数，待添加")
  elif tx == 33:
    dy(twMTw(ts))  #两位数乘两位数——普通
  elif tx == 34:
    dy(stgb(ts))  #两位数乘两位数——十同个补乘法
  elif tx == 35:
    dy(gtsb(ts))  #两位数乘两位数——个同十补乘法
  elif tx == 36:
    dy(swxt(ts))  #两位数乘两位数——十位相同乘法
  elif tx == 37:
    dy(swtSwb(ts))  #两位数乘两位数——首尾同乘首尾补
  elif tx == 38:
    dy(w1LwMul(ts))  #尾数为1的两位数相乘——尾1两位数乘
  elif tx == 39:
    print("试行接近100的数的范围为80~120")
    dy(jj100Mul(ts))  #接近100的数字相乘——接近100相乘
  elif tx == 40:
    print("试行接近100的数的范围为30~70")
    dy(jj50Mul(ts))  #接近50的数字相乘——接近50相乘
  elif tx == 41:
    dy(n9Mul(ts))  #任意数与9相乘——nc9（n是任意数、Mul是乘、9是乘数或者被乘数）
  elif tx == 42:
    dy(eTnMul(ts))  #11~19中的整数相乘——十一到十九相乘eTnXc（Eleven to nineteen）
  elif (43 <= tx) and (tx <= 48):
    print("暂无该乘法函数，待添加")
  elif (49 <= tx) and (tx <= 64):
    print("暂无该除法函数，待添加")

#启动
qidong()