# -*- coding: utf-8 -*-
import os
import shutil
import time

originDir = '/Users/admin/Desktop/ios'
#本地项目多语言路径
desDir = '/Volumes/M/workSpace/BaBa-iOS-1.1.9/Resources'

def copyToDestinationFolder(originPath,destPath):
    start = time.time()
    i = 0
    for oriDirName, oriSubdirList, oriFileList in os.walk(originPath):
                                    for fname in oriFileList:
                                            if fname.endswith('.strings'):
                                               lists = fname.split('.')
                                               lists = lists[0].split('_')
                                               regName = lists[1]
                                               if regName == 'zh':
                                                   regName = 'zh-Hans'
                                               regName = '%s.%s' % (regName,'lproj')

                                               for dirName, subdirList, fileList in os.walk(destPath):
                                                                                if dirName.endswith(regName):
                                                                                    srcFile = '%s/%s' % (oriDirName,fname)
                                                                                    shutil.copy(srcFile,dirName) #拷贝到目标目录
                                                                                    oriFolder = '%s/%s' % (dirName,'Localizable.strings')
                                                                                    if os.path.isfile(oriFolder):
                                                                                        os.remove(oriFolder)    #移除原来的文件
                                                                                    oriFolder = '%s/%s' % (dirName,fname)
                                                                                    if os.path.isfile(oriFolder):
                                                                                        destFolder = '%s/%s' % (dirName,'Localizable.strings')
                                                                                        os.rename(oriFolder,destFolder) #重命名
                                                                                    i  = i + 1

    c = time.time() - start
    print('程序运行耗时:%0.2f 秒'%(c))
    print('总共处理了 %s 个文件'%(i))

copyToDestinationFolder(originDir,desDir)