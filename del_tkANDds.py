import os
#删除一个目录文件中的某些特定后缀名文件
def del_files(path):
  for root , dirs, files in os.walk(path):
    for name in files:
      #filenameSuffix：文件名后缀，是要删除的文件名后缀，比如.txt
      if name.endswith(filenameSuffix):
        os.remove(os.path.join(root, name))
        print ("删除文件: " + os.path.join(root, name))
#删除空目录
def delnull(dirr):
  if os.path.isdir(dirr):
    for p in os.listdir(dirr):
      d  = os.path.join(dirr,p)
      if (os.path.isdir(d) == True):
        delnull(d)
  if not os.listdir(dirr):
    os.rmdir(dirr)
    print('移除空目录: ', dirr)
# 输入相应的内容然后把参数传入到函数中
if __name__ == "__main__":
  filenameSuffix = ".txt"
  path = "D:\\F\\jisuanti\\tkANDds"
  del_files(path)