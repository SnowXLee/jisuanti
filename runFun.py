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
  #1~16是加法，17~32是减法，33~64是乘法
  dirNameAdd = ".\\tkANDds\\addition\\"
  dirNameSub = ".\\tkANDds\\subtraction\\"
  dirNameMul = ".\\tkANDds\\multiplication\\"
  dirNameDiv = ".\\tkANDds\\division\\"
  #打印函数dy(题本类型tlx，题名字tName)
  tName = {
    1: dirNameAdd + '两位数加两位数',
    2: dirNameAdd + '三位数加两位数',
    3: dirNameAdd + '三位数加三位数',
    4: dirNameAdd + '四位数加三位数',
    5: dirNameAdd + '四位数加四位数',
    17: dirNameSub + '两位数减一位数',
    18: dirNameSub + '两位数减两位数',
    19: dirNameSub + '三位数减两位数',
    20: dirNameSub + '三位数减三位数',
    21: dirNameSub + '四位数减三位数',
    22: dirNameSub + '四位数减四位数',
    33: dirNameMul + '两位数乘两位数',
    34: dirNameMul + '十同个补乘法',
    35: dirNameMul + '个同十补乘法',
    36: dirNameMul + '十位相同乘法',
    37: dirNameMul + '首尾同乘首尾补',
    38: dirNameMul + '尾1两位数乘',
    39: dirNameMul + '接近100相乘',
    40: dirNameMul + '接近50相乘',
    41: dirNameMul + '11~19中的整数相乘',
    42: dirNameMul + '任意数与9相乘',
    43: dirNameMul + '任意数与99相乘',
    44: dirNameMul + '任意数与999相乘',
    45: dirNameMul + '还没写好，两位数混合运算',
    46: dirNameMul + '三位以上的数字与11相乘',
    47: dirNameMul + '三位以上的数字与111相乘',
    48: dirNameMul + '接近两百的数字相乘',
    49: dirNameMul + '100~110中的整数相乘',
    50: dirNameMul + '三位数与两位数相乘',
    51: dirNameMul + '三位数乘以三位数',
    52: dirNameMul + '四位数与两位数相乘',
    53: dirNameMul + '四位数乘以三位数',
  }
  #题的类型tlx——打印函数dy(题本类型tlx，题名字tName)；ts是tlx里面调用的题型的参数——题数
  tlx = {
    1: addAndSub.twATw,#两位数加两位数
    2: addAndSub.thATw,#三位数加两位数
    3: addAndSub.thATh,#三位数加三位数
    4: addAndSub.foATh,#四位数加三位数
    5: addAndSub.foAFo,#四位数加四位数
    17: addAndSub.twSOn,#两位数减一位数
    18: addAndSub.twSTw,#两位数减两位数
    19: addAndSub.thSTw,#三位数减两位数
    20: addAndSub.thSTh,#三位数减三位数
    21: addAndSub.foSTh,#四位数减三位数
    22: addAndSub.foSFo,#四位数减四位数
    33: twoDigitMul.twMTw,#两位数乘两位数
    34: twoDigitMul.stgb,#十同个补乘法
    35: twoDigitMul.gtsb,#个同十补乘法
    36: twoDigitMul.swxt,#十位相同乘法
    37: twoDigitMul.swtSwb,#首尾同乘首尾补
    38: twoDigitMul.w1LwMul,#尾1两位数乘
    39: twoDigitMul.jj100Mul,#接近100相乘
    40: twoDigitMul.jj50Mul,#接近50相乘
    41: twoDigitMul.eTNMul,#11~19中的整数相乘
    42: twoDigitMul.n9Mul,#任意数与9相乘
    43: twoDigitMul.n99Mul,#任意数与99相乘
    44: twoDigitMul.n999Mul,#任意数与999相乘
    45: twoDigitMul.twMixMul,#还没写好，两位数混合运算
    46: threeDigitMul.th11Mul,#三位以上的数字与11相乘
    47: threeDigitMul.th111Mul,#三位以上的数字与111相乘
    48: threeDigitMul.jj200Mul,#接近两百的数字相乘
    49: threeDigitMul.mul100_110,#100~110中的整数相乘
    50: threeDigitMul.thTwMul,#三位数与两位数相乘
    51: threeDigitMul.thThMul,#三位数乘以三位数
    52: fourDigitMul.foTwMul,#四位数与两位数相乘
    53: fourDigitMul.foThMul,#四位数乘以三位数
  }
  #调用打印函数dy(题本类型tlx，题名字tName)；ts是tlx里面调用的题型的参数——题数
  dy(tlx.get(tx, '暂无该加法的函数，待添加')(ts), tName.get(tx, '暂无该加法的函数的对应键，待添加'))