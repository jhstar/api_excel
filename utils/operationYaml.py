import yaml
from common.public import filePath

class OperationYaml:
    def readYaml(self):
        with open(filePath('data','ya.yaml'),'r',encoding="utf-8") as f:
            return list(yaml.safe_load_all(f))

    def readYamlE(self,fileDir,fileName):
        with open(filePath(fileDir=fileDir,fileName=fileName),'r',encoding='utf-8') as f:
            return yaml.safe_load(f)

if __name__ == '__main__':
    # obj=OperationYaml()
    print(OperationYaml().readYamlE('data','yaa.yaml')['header_login_01'])
    # print(obj.readYaml())
    # for item in obj.readYaml():
    #     print(item['url'])
    # print(type(item))