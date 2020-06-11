#
#consine： 相似度计算
#jacard：  相似度计算



import os
import math

#读取文件内容
def read_file_fd(filePath):
    if not os.path.exists(filePath):
        return
    fd = open(filePath,'r', encoding="utf-8")
    return fd

#写入文件内容
def write_file_fd(outputPath):
    fd = open(outputPath, 'w', encoding="utf-8" )
    return fd

def wordCountMap( words):
    words = list.sort(words)
    currentWord = None
    wordCount = 0
    wordDict = {}
    allWords = 0
    for word in words:
        if currentWord != None and currentWord != word:
            wordDict.put(str(currentWord), wordCount)
            wordCount = 0
            allWords += 1
        wordCount += 1
        currentWord = word
    wordDict.put(str(currentWord), wordCount)
    return wordDict,allWords

class mapAndReduce:

    #合并文本内容为一行，以空格隔开
    def conbineText(self,filePath):
        file_fd = read_file_fd(filePath)
        lines = []
        for line in file_fd :
            lines.append(line.strip())
        return " ".join(lines)

    #合并文件夹下文件到一个文本中
    def conbind(self,inputPath,outputPath):
        if not os.path.exists( inputPath ):
            return
        filePoint = 0
        files = os.listdir(inputPath)
        write_fd = write_file_fd(outputPath)
        for file in files:
            write_fd.write( "\t".join( [str(filePoint) , "".join([self.conbineText(inputPath+"/"+file),"\n"])]) )
            filePoint += 1
        write_fd.close()

    def reduces(self,inputFile,outputFile):
        if not os.path.exists( inputFile ):
            return
        lines = read_file_fd(inputFile)
        allCount = 0
        allWords = []
        for line in lines:
            patitions = line.split("\t")
            if len(patitions) != 2:
                continue
            words = patitions[1].split(" ")
            wordset = set(words)
            allWords.extend(wordset)
            allCount += 1

        list.sort(allWords)

        write_fd = write_file_fd(outputFile)

        #统计单词
        currentWord = None
        wordCount = 0
        for word in allWords:
            if currentWord != None and currentWord != word:
                rate = math.log( float(allCount) / (float(wordCount) + 1 ))
                print(word + "=" + str(rate) )
                write_fd.write( " ".join([str(currentWord),  str(math.log( float(allCount) / (float(wordCount) + 1 ))) + "\n" ]))
                wordCount = 0
            currentWord = word
            wordCount += 1

        write_fd.write( " ".join([str(currentWord), str(math.log( float(allCount) / (float(wordCount) + 1 )))  + "\n"  ]))


    def read_idf(self,inputPath):
        if not os.path.exists(inputPath):
            return

        read_fd = read_file_fd(inputPath)
        idf = {}
        for line in read_fd:
            partion = line.split(" ")
            if len(partion) != 2 :
                continue
            idf[str(partion[0])] = float(partion[1])
        return idf

    def tf(self, idfPath ,content):
        words = str(content).split(" ")
        if len(words) <= 0:
            return

        list.sort(words)
        currentWord = None
        wordCount = 0
        wordDict = {}
        wordArray = []
        allWords = 0
        for word in words:
            if currentWord != None and currentWord != word:
                wordDict[str(currentWord)] = wordCount
                wordArray.append(str(currentWord))
                wordCount = 0
                allWords += 1
            wordCount += 1
            currentWord = word
        wordDict[str(currentWord)] = wordCount
        wordArray.append(str(currentWord))
        allWords += 1

        idf = self.read_idf(idfPath)

        for word in wordArray:
            if not word in idf.keys():
                continue

            tf = wordDict[word] / allWords
            wordIdf = idf[word]
            print(word , str(tf) , "tf-idf:"+str(tf*wordIdf) )

mapAndReduce = mapAndReduce()
# mapAndReduce.conbind("E:/study/codes/codes/data","E:/study/codes/codes/conbind")
#mapAndReduce.reduces("E:/study/codes/codes/conbind","E:/study/codes/codes/idf")
mapAndReduce.tf("E:/study/codes/codes/idf","黑龙江 我们 都 是 好 孩子 吗 ， 我们 是 孩子 吗")

