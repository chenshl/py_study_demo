#!usr/bin/python
# _*_ coding: UTF-8 _*_
# @author : csl
# @date   : 2018/2/24 22:29
'''文件操作'''


def read_file(filepath,filename):
    '''按行读取文件'''
    filepn = filepath + "/"  + filename
    with open(filepn,"r") as file:
        for line in file.readlines():
             print(line.strip())
        # return line.strip()

def write_file(filepath,filename,content,iscover):
    '''写入文件内容'''
    # content : 写入文件内容
    # iscover : 是否覆盖，及填加到文件最后还是将文件整个覆盖
    filepn = filepath + "/" + filename
    if iscover == True:
        with open(filepn,'w') as file:
            file.write(content + "\n")  #写入后换行
    else:
        with open(filepn,'a') as file:  #光标停留在文件末尾
            file.write(content + "\n")




if __name__ == "__main__":
    filep = "C:/Users/Administrator/Desktop"
    filen = "pythontest1.txt"
    writecontent = """百日衣衫尽
    黄河入海流
    欲穷千里目
    更上一层楼
    """
    write_file(filep,filen,writecontent,False)
    read_file(filep,filen)
