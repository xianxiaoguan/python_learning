# encoding: utf-8
import os
import shutil
import time

time0 = "2021-08-05 14:18:0"  # 起始日期
time1 = "2021-08-05 14:19:0"  # 结束日期
t0 = time.mktime(time.strptime(time0, '%Y-%m-%d %H:%M:%S'))
t1 = time.mktime(time.strptime(time1, '%Y-%m-%d %H:%M:%S'))
print("to:%f"%t0)
print("t1:%f"%t1)
targetDir = r"C:\game"  # 目标目录
print("正在处理，请稍等.....")
curDir = os.getcwd()
for root, dirs, files in os.walk(curDir):
    # 先创建目标目录
    curFolder = root[len(curDir) + 1:]  # 提取当前文件夹
    tempTargetDir = os.path.join(targetDir, curFolder)  # 生成目标目录绝对路径
    # print(tempTargetDir)
    if os.path.exists(tempTargetDir):
        shutil.rmtree(tempTargetDir)
    # 再拷贝文件
    for fileName in files:
        absFileName = os.path.join(root, fileName)
        # print(absFileName)
        # print(os.path.getmtime(absFileName))
        if os.path.splitext(absFileName)[1] != '.py' and os.path.getmtime(absFileName) >= t0 and os.path.getmtime(
                absFileName) <= t1:
            if not os.path.exists(tempTargetDir):
                os.makedirs(tempTargetDir)
            print("正在拷贝文件：", absFileName)
            shutil.copy(absFileName, tempTargetDir)
print("done")
os.system("pause")