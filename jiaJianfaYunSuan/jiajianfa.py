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

#两位数加法运算题——两位数加法
def lwsjf(n):
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

#三位数加法运算题——三位数加法
def swsjf(n):
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

#四位数加法运算题——四位数加法
def swsjf_(n):
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

#两位数减一位数运算题——两减一减法
def ljyjf(n):
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

#两位数减法运算题——两减两减法
def ljljf(n):
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

#三位数减两位数运算题——三减两减法
def sjljf(n):
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

#三位数减三位数运算题——三减三减法
def sjsjf(n):
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

#四位数减三位数减法——四减三减法
def fjsjf(n):
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

#四位数减四位数减法——四减四减法
def fjfjf(n):
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
  #参数依然是题本类似这种 abc = ljljf(4) + sjljf(4) + fjfjf(4)
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
  for ts in range(len(jstTbL)):
    #ts题数tb中下标0的长度
    if (ts + 1) % 4 == 0:
      jstTbL.insert(ts + 1, "\n\n")
      dsTbL.insert(ts + 1, "\n\n")
  outputTb = "  ".join(jstTbL)
  outputDs = "  ".join(dsTbL)
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


#启动
abc = ljljf(4) + sjljf(4) + fjfjf(4)
dy(abc)







#题库种类
#加法：两位数加法运算题——lwsjf(n)、三位数加法运算题——swsjf(n)、四位数加法运算题——fjfjf(n)
#减法：两减一减法ljyjf(n)、两减两减法ljljf(n)、三减两减法sjljf(n)、三减三减法sjsjf(n)、四减三减法fjsjf(n)、四减四减法fjfjf(n)
