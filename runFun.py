import time
import sys
from addAndSubFun import addAndSub
from mulFun import twoDigitMul
from mulFun import threeDigitMul
from mulFun import fourDigitMul


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
def dy(tb, tName):
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
  fTb = open(tName + nyrhm + "题" + ".txt", "w", encoding= 'utf-8')
  fDs = open(tName + nyrhm + "得数" + ".txt", "w", encoding= 'utf-8')
  fTb.write(outputTb)
  fDs.write(outputDs)
  # 关闭打开的文件，必须关闭不然电脑能炸裂
  fTb.close()
  fDs.close()

#启动函数，按提示输入相应选项即可导出相应类型的题目以及所需题数
def qidong():
  print("所有题数必须为4的倍数\n")
  print("1：两位数加两位数、2：三位数加两位数、3：三位数加三位数、4：四位数加三位数、5：四位数加四位数\n")
  print("17：两位数减一位数、18：两位数减两位数、19：三位数减两位数、20：三位数减三位数、21：四位数减三位数、22：四位数减四位数\n")
  print("33：两位数乘两位数、34：十同个补乘法、35：个同十补乘法、36：十位相同乘法、37：首尾同乘首尾补乘法、38：尾数为1的两位数相乘、39：接近100的数字相乘、40：接近50的数字相乘、41：11~19中的整数相乘\n")
  print("42：任意数与9相乘、43：任意数与99相乘、44：任意数与999相乘、45：两位数混合运算\n")
  print("46：三位以上的数字与11相乘、47：三位以上的数字与111相乘、48：接近两百的数字相乘、49：100~110中的整数相乘、50：三位数与两位数相乘、51：三位数乘以三位数、52：四位数与两位数相乘、53：四位数乘以三位数\n")
  print("")
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
  dirNameAdd = ".\\tkANDds\\addition\\"
  dirNameSub = ".\\tkANDds\\subtraction\\"
  dirNameMul = ".\\tkANDds\\multiplication\\"
  dirNameDiv = ".\\tkANDds\\division\\"
  #1~16是加法，17~32是减法，33~48是乘法，49~64是除法
  if tx == 1:
    dy(addAndSub.twATw(ts), tName = dirNameAdd + '两位数加两位数')  #两位数加两位数
  elif tx == 2:
    dy(addAndSub.thATw(ts), tName = dirNameAdd + '三位数加两位数')  #三位数加两位数
  elif tx == 3:
    dy(addAndSub.thATh(ts), tName = dirNameAdd + '三位数加三位数')  #三位数加三位数
  elif tx == 4:
    dy(addAndSub.foATh(ts), tName = dirNameAdd + '四位数加三位数')  #四位数加三位数
  elif tx == 5:
    dy(addAndSub.foAFo(ts), tName = dirNameAdd + '四位数加四位数')  #四位数加四位数
  elif (6 <= tx) and (tx <= 16):
    print("暂无该加法的函数，待添加")
  elif tx == 17:
    dy(addAndSub.twSOn(ts), tName = dirNameSub + '两位数减一位数')  #两位数减一位数
  elif tx == 18:
    dy(addAndSub.twSTw(ts), tName = dirNameSub + '两位数减两位数')  #两位数减两位数
  elif tx == 19:
    dy(addAndSub.thSTw(ts), tName = dirNameSub + '三位数减两位数')  #三位数减两位数
  elif tx == 20:
    dy(addAndSub.thSTh(ts), tName = dirNameSub + '三位数减三位数')  #三位数减三位数
  elif tx == 21:
    dy(addAndSub.foSTh(ts), tName = dirNameSub + '四位数减三位数')  #四位数减三位数
  elif tx == 22:
    dy(addAndSub.foSFo(ts), tName = dirNameSub + '四位数减四位数')  #四位数减四位数
  elif (24 <= tx) and (tx <= 32):
    print("暂无该减法函数，待添加")
  elif tx == 33:
    dy(twoDigitMul.twMTw(ts), tName = dirNameMul + '两位数乘两位数')  #两位数乘两位数——普通
  elif tx == 34:
    dy(twoDigitMul.stgb(ts), tName = dirNameMul + '十同个补乘法')  #两位数乘两位数——十同个补乘法
  elif tx == 35:
    dy(twoDigitMul.gtsb(ts), tName = dirNameMul + '个同十补乘法')  #两位数乘两位数——个同十补乘法
  elif tx == 36:
    dy(twoDigitMul.swxt(ts), tName = dirNameMul + '十位相同乘法')  #两位数乘两位数——十位相同乘法
  elif tx == 37:
    dy(twoDigitMul.swtSwb(ts), tName = dirNameMul + '首尾同乘首尾补')  #两位数乘两位数——首尾同乘首尾补
  elif tx == 38:
    dy(twoDigitMul.w1LwMul(ts), tName = dirNameMul + '尾1两位数乘')  #尾数为1的两位数相乘——尾1两位数乘
  elif tx == 39:
    print("试行接近100的数的范围为80~120")
    dy(twoDigitMul.jj100Mul(ts), tName = dirNameMul + '接近100相乘')  #接近100的数字相乘——接近100相乘
  elif tx == 40:
    print("试行接近100的数的范围为30~70")
    dy(twoDigitMul.jj50Mul(ts), tName = dirNameMul + '接近50相乘')  #接近50的数字相乘——接近50相乘
  elif tx == 41:
    dy(twoDigitMul.eTNMul(ts), tName = dirNameMul + '11~19中的整数相乘')  #11~19中的整数相乘——十一到十九相乘eTnXc（Eleven to nineteen）
  elif tx == 42:
    dy(twoDigitMul.n9Mul(ts), tName = dirNameMul + '任意数与9相乘')  #任意数与9相乘——nc9（n是任意数、Mul是乘、9是乘数或者被乘数）
  elif tx == 43:
    dy(twoDigitMul.n99Mul(ts), tName = dirNameMul + '任意数与99相乘')  #任意数与99相乘——nc99（n是任意数、Mul是乘、99是乘数或者被乘数）
  elif tx == 44:
    dy(twoDigitMul.n999Mul(ts), tName = dirNameMul + '任意数与999相乘')  #任意数与999相乘——nc999（n是任意数、Mul是乘、9是乘数或者被乘数）
  elif tx == 45:
    print("还没写好")  #两位数混合运算
  elif tx == 46:
    dy(threeDigitMul.th11Mul(ts), tName = dirNameMul + '三位以上的数字与11相乘')  #三位以上的数字与11相乘——three 11 mulnineteen）
  elif tx == 47:
    dy(threeDigitMul.th111Mul(ts), tName = dirNameMul + '三位以上的数字与111相乘')  #三位以上的数字与111相乘——three 111 mul
  elif tx == 48:
    dy(threeDigitMul.jj200Mul(ts), tName = dirNameMul + '接近两百的数字相乘')  #接近两百的数字相乘——接近200相乘
  elif tx == 49:
    dy(threeDigitMul.mul100_110(ts), tName = dirNameMul + '100~110中的整数相乘')  #100~110中的整数相乘——mul 100 110
  elif tx == 50:
    dy(threeDigitMul.thTwMul(ts), tName = dirNameMul + '#三位数与两位数相乘')  #三位数与两位数相乘——three two mul
  elif tx == 51:
    dy(threeDigitMul.thThMul(ts), tName = dirNameMul + '三位数乘以三位数')  #三位数乘以三位数——three three mul
  elif tx == 52:
    dy(fourDigitMul.foTwMul(ts), tName = dirNameMul + '四位数与两位数相乘')  #四位数与两位数相乘——four two mul
  elif tx == 53:
    dy(fourDigitMul.foThMul(ts), tName = dirNameMul + '四位数乘以三位数')  #四位数乘以三位数——four three mul
  elif (54 <= tx) and (tx <= 64):
    print("暂无该除法函数，待添加")
