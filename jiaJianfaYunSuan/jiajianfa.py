import random
import time

#随机数函数
def random_int_list(start, stop, length):
  start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
  length = int(abs(length)) if length else 0
  random_list = []
  for i in range(length):
    random_list.append(random.randint(start, stop))
  return random_list

#两位数加法运算题——两位数加法two add two
def twATw(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11+12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = random_int_list(10, 99, n)  #被加数的两位数列表
  jsL = random_int_list(10, 99, n)  #加数的两位数列表
  #获得题与答案
  for i in range(n):
    dsL.append(str(bjsL[i] + jsL[i]))
    ystL.append(str(bjsL[i]) + '+' + str(jsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#三位数加法运算题——three add three
def thATh(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11+12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = random_int_list(100, 999, n)  #被加数的三位数列表
  jsL = random_int_list(100, 999, n)  #加数的三位数列表
  #获得题与答案
  for i in range(n):
    dsL.append(str(bjsL[i] + jsL[i]))
    ystL.append(str(bjsL[i]) + '+' + str(jsL[i]))
  tk.append(ystL)
  tk.append(dsL)
  return tk

#四位数加法运算题——four add four
def foAFo(n):
  #参数n为题数
  dsL = []  #得数列表
  ystL = []  #运算题列表11+12
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = random_int_list(1000, 9999, n)  #被加数的四位数列表
  jsL = random_int_list(1000, 9999, n)  #加数的四位数列表
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
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = random_int_list(10, 99, n)  #被减数的两位数列表
  jsL = random_int_list(0, 9, n)  #减数的一位数列表
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
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = random_int_list(10, 99, n)  #被减数的两位数列表
  jsL = random_int_list(10, 99, n)  #减数的两位数列表
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
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = random_int_list(100, 999, n)  #被减数的三位数列表
  jsL = random_int_list(10, 99, n)  #减数的两位数列表
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
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = random_int_list(100, 999, n)  #被减数的三位数列表
  jsL = random_int_list(100, 999, n)  #减数的三位数列表
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
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = random_int_list(1000, 9999, n)  #被减数的三位数列表
  jsL = random_int_list(100, 999, n)  #减数的三位数列表
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
  tk = []  #题库列表输出列表，下标0得数列表ds；下标1为题；
  bjsL = random_int_list(1000, 9999, n)  #被减数的三位数列表
  jsL = random_int_list(1000, 9999, n)  #减数的三位数列表
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
  fTb = open("./exercise/" + nyrhm + "题" + ".txt", "w")
  fDs = open("./exercise/" + nyrhm + "得数" + ".txt", "w")
  fTb.write(outputTb)
  fDs.write(outputDs)
  # 关闭打开的文件，必须关闭不然电脑能炸裂
  fTb.close()
  fDs.close()

#两位数加两位数44题  twATw(44)  #三位数加两位数44题  thATw(44)  
#三位数加三位数44题  thATh(44)  #四位数加三位数44题  foATh(44)
#四位数加四位数44题  foAFo(44)  
#两位数加两位数加三位数36题  

#两位数减两位数44题  twSTw(44)  #三位数减两位数44题  thSTw(44)
#三位数减三位数44题  thSTh(44)  #四位数减三位数44题  foSTh(44)
#四位数减四位数44题  foSFo(44)



#启动
abc = twSTw(44)
dy(abc)


#题库种类
#加法：两位数加法运算题——twatw(n)、三位数加法运算题——thath(n)、四位数加法运算题——foafo(n)
#减法：两减一减法twson(n)、两减两减法twstw(n)、三减两减法thstw(n)、三减三减法thsth(n)、四减三减法fosth(n)、四减四减法fosfo(n)
