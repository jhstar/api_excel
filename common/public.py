import os

def filePath(fileDir,fileName):
    ''':param fileDir 文件的目录
    :param fileName 文件的名称
    :param return  返回文件的位置
    '''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

print(filePath('base','method.py'))
