import os

#读取文件内容
def read_file_fd(filePath):
    if not os.path.exists(filePath):
        return
    fd = open(filePath,'r')
    return fd

#写入文件内容
def write_file_fd(outputPath , content):
    fd = open(outputPath, 'w', encoding="utf-8" )
    return fd

class mapAndReduce:

    #合并文本内容为一行，以空格隔开
    def conbineText(self,filePath):
        file_fd = read_file_fd(filePath)
        lines = []
        for line in file_fd :
            lines.append(line.strip())
        return " ".join(lines)

    def conbind(self,inputPath,outputPath):
        if not os.path.exists( inputPath ):
            return
        filePoint = 0
        files = os.listdir(inputPath)
        write_fd = write_file_fd(outputPath)
        for file in files:
            write_fd.write( "".join( [filePoint ,self.conbineText(inputPath+"/",file) , "\n"]) )
            filePoint += 1
        write_fd.close()

mapAndReduce = mapAndReduce()
print(mapAndReduce.conbineText("d:/Config.ini"))
