@echo off
setlocal enabledelayedexpansion
::进入以下目录
cd D:\F\jisuanti
::Python 运行run.py文件并等待程序执行完毕再执行下一步
start /wait python run.py
::进入会出现新建文件的目录，即tkANDds目录下的某一个子目录。
cd /d D:\F\jisuanti\tkANDds
::tkANDds目录中有四个子目录，有新建文件的目录显示为最新目录
for /f "delims=" %%i in ('dir /b /ad /od') do (set "var=%%i")
::输出该目录名称并存放在 %var% 中
echo 最新创建的文件夹是：%var%
:: 设置文件所在目录
set src_dir=%var%
:: filename用于存放目标文件名
::set filename=""
::进入有新建文件的目录
cd /d %src_dir%
::寻找新建文件并打印出来
for /f %%a in ('dir /o-d /tc /b .') do (
  echo 文件完整信息: %%a
  set deshu_filename=%%~na%%~xa
  echo 文件名: !filename!, 最新创建时间： %%~ta
  ::找到最新文件后跳转到forBreak1，因为这个循环没有停止事件需要自己去终止循环，否则会打印该目录下所有文件名。
  goto forBreak1
)
:forBreak1

::bat 中set 变量1=变量2 中等于号两边不能用空格否则会出错
set ti_filename=%deshu_filename%
::替换字符，比如[阿巴阿巴9时16分得数.txt]替换成[阿巴阿巴9时16分题.txt]
set "ti_filename=%ti_filename:得数=题%"
::依次打开得数与题文件
start "" %deshu_filename%
start "" %ti_filename%