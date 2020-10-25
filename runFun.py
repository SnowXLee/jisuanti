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

#tkNameAPath——题库中文名称(也是txt文件的前缀名)和导出题库的txt路径，里面是字典
#NP——name or path
def tkNamePath(np, n):
  #导出题库的txt路径
  dirNameAdd = ".\\tkANDds\\addition\\"
  dirNameSub = ".\\tkANDds\\subtraction\\"
  dirNameMul = ".\\tkANDds\\multiplication\\"
  dirNameDiv = ".\\tkANDds\\division\\"
  #tkName——题库中文名称(也是txt文件的前缀名)
  tkName = {
    # "1~16": "加法",
    1: '两位数加两位数',
    2: '三位数加两位数',
    3: '三位数加三位数',
    4: '四位数加三位数',
    5: '四位数加四位数',
    # "17~32": "减法",
    17: '两位数减一位数',
    18: '两位数减两位数',
    19: '三位数减两位数',
    20: '三位数减三位数',
    21: '四位数减三位数',
    22: '四位数减四位数',
    # "33~56": "两位数乘法",
    33: '两位数乘两位数',
    34: '十同个补乘法',
    35: '个同十补乘法',
    36: '十位相同乘法',
    37: '首尾同乘首尾补',
    38: '尾1两位数乘',
    39: '接近100相乘',
    40: '接近50相乘',
    41: '11~19中的整数相乘',
    42: '还没写好，两位数混合运算',
    # "57~66": "三位数乘法",
    57: '三位数与两位数相乘',
    58: '三位数乘以三位数',
    59: '三位以上的数字与11相乘',
    60: '三位以上的数字与111相乘',
    61: '100~110中的整数相乘',
    62: '接近两百的数字相乘',
    # "67~72": "四位数乘法",
    67: '四位数与两位数相乘',
    68: '四位数乘以三位数',
    69: '四位数乘以四位数',
    # "73~88": "任意数与n乘法",
    73: '任意数与9相乘',
    74: '任意数与99相乘',
    75: '任意数与999相乘',
  }
  #np①name返回tkName[n]，用于print出来②path返回dirName**+tkName[n]，用于txt导出路径以及命名文件
  #抛出异常——当tkName中没有的键值时返回一个值None，然后在启动qidong()中接住这个值不让程序继续往下运行
  if tkName.get(n, None) == None:
    return None
  if np == "name":
    return tkName.get(n)
  elif np == "path":
    #1~16: 加法
    if 1 <= n <= 16:
      return (dirNameAdd + tkName.get(n))
    #17~32: 减法
    elif 17 <= n <= 32:
      return (dirNameSub + tkName.get(n))
    #33~88：乘法
    elif 33 <= n <= 88:
      return (dirNameMul + tkName.get(n))

#tkFun()——内含题库函数的字典，用于给dy(题本类型tlx，题名字tName)的tlx参数题干相应函数
def tkFun(tx, ts):
  #题的类型tlx——打印函数dy(题本类型tlx，题名字tName)；ts是tlx里面调用的题型的参数——题数
  tlx = {
    #1~16:加法
    1: addAndSub.twATw,#两位数加两位数
    2: addAndSub.thATw,#三位数加两位数
    3: addAndSub.thATh,#三位数加三位数
    4: addAndSub.foATh,#四位数加三位数
    5: addAndSub.foAFo,#四位数加四位数
    #17~32:减法
    17: addAndSub.twSOn,#两位数减一位数
    18: addAndSub.twSTw,#两位数减两位数
    19: addAndSub.thSTw,#三位数减两位数
    20: addAndSub.thSTh,#三位数减三位数
    21: addAndSub.foSTh,#四位数减三位数
    22: addAndSub.foSFo,#四位数减四位数
    #33~56:两位数乘法
    33: twoDigitMul.twMTw,#两位数乘两位数
    34: twoDigitMul.stgb,#十同个补乘法
    35: twoDigitMul.gtsb,#个同十补乘法
    36: twoDigitMul.swxt,#十位相同乘法
    37: twoDigitMul.swtSwb,#首尾同乘首尾补
    38: twoDigitMul.w1LwMul,#尾1两位数乘
    39: twoDigitMul.jj100Mul,#接近100相乘
    40: twoDigitMul.jj50Mul,#接近50相乘
    41: twoDigitMul.eTNMul,#11~19中的整数相乘
    42: twoDigitMul.twMixMul,#还没写好，两位数混合运算
    #57~66三位数乘法
    57: threeDigitMul.thTwMul,#三位数与两位数相乘
    58: threeDigitMul.thThMul,#三位数乘以三位数
    59: threeDigitMul.th11Mul,#三位以上的数字与11相乘
    60: threeDigitMul.th111Mul,#三位以上的数字与111相乘
    61: threeDigitMul.mul100_110,#100~110中的整数相乘
    62: threeDigitMul.jj200Mul,#接近两百的数字相乘
    #67~72四位数乘法
    67: fourDigitMul.foTwMul,#四位数与两位数相乘
    68: fourDigitMul.foThMul,#四位数乘以三位数
    69: fourDigitMul.foFoMul,#四位数乘四位数
    #73~88:任意数与n乘法
    73: twoDigitMul.n9Mul,#任意数与9相乘
    74: twoDigitMul.n99Mul,#任意数与99相乘
    75: twoDigitMul.n999Mul,#任意数与999相乘
  }
  return tlx.get(tx, '暂无该加法的函数，待添加')(ts)

#启动函数，按提示输入相应选项即可导出相应类型的题目以及所需题数
def qidong():
  #题库的题类型的中文名——下次修改的方法，第一步在tName_zh中添加对应的题目的中文名称与号码，第二步在打印题型对应的号码的print中的对应行输入tName_zh。第三步tName中添加相应号码的tName_zh。第四步tlx中添加对应的函数
  #刚进程序时打印print对应题型的号码等提示信息
  for i in range(88):
    #每到字典的题型分类边界值时打印一个换行符
    if tkNamePath("name", i) != None:
      print((str(i) + "." + tkNamePath("name", i)), end="  ")
    if i in {16, 32, 56, 66, 72, 88}:
      print("\n")
  print("\n")
  print("所有题数必须为4的倍数\n", end="\n")
  tx = int(input("输入你需要的题型:"))  #题型
  #抛出错误题型不在上述范围内——不正确重新输入
  if ((tx <= 0) or (tx >= 100)):
    print("请重新输入正确的题型代号")
    qidong()
  ts = int(input("该题型所需题数:"))  #题数
  #抛出错误题型不在上述范围内——不正确重新输入（可能不需要）
  if (ts % 4 != 0):
    print("题数需为4的倍数，请重新输入")
    qidong()
  #1~16:加法, 17~32:减法, 33~64:乘法{33~56:两位数乘法, 57~72:三位数乘法,67~72四位数乘法:四位数乘法, 73~88:任意数与n乘法,}
  #调用打印函数dy(题本类型tlx=tkFun(tx, ts)，题名字tName=tkNamePath("path", tx))；ts是tlx里面调用的题型的参数——题数
  dy(tkFun(tx, ts), tkNamePath("path", tx))
