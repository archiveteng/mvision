#!/usr/bin/python

"""
        File      : count.py
        Author    : Cheng WANG
"""
import sys,os

extens = [".py"]
linesCount = 0
filesCount = 0


def funCount(dirName):
    global extens,linesCount,filesCount
    for root,dirs,fileNames in os.walk(dirName):
        for f in fileNames:
            fname = os.path.join(root,f)
            if '.' not in f:
                continue
            try :
                ext = f[f.rindex('.'):]
                if extens.count(ext) > 0:
                    filesCount += 1 

                    if not fname.__contains__("resources"):
                        if not fname.__contains__("__init__"):
                            l_count = len(open(fname).readlines())
                            print(fname, l_count)
                            linesCount += l_count
            except:
                print ("Error occur!")
                pass


if len(sys.argv) > 1 :
    for m_dir in sys.argv[1:]:        
        print (m_dir)
        funCount(m_dir)
else :
    funCount(".")        

print ("files count : ", filesCount)
print ("lines count : ", linesCount)
