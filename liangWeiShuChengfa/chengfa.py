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
  fTb = open("./mulExercise/" + nyrhm + "题" + ".txt", "w")
  fDs = open("./mulExercise/" + nyrhm + "得数" + ".txt", "w")
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

#启动
abc = stgb(44) + gtsb(44)
dy(abc)

#两位数乘两位数44题  twMTw(44)  #十位相同个位互补的两位数相乘44题  stgb(44)
#个位相同十位互补的两位数相乘44题  gtsb(44)  #十位相同的两位数相乘44题  swxt(44)