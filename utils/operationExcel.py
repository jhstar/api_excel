import xlrd
import os
import sys
common_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'common')
sys.path.append(common_path)
from public import filePath
# from common.public import filePath
'''文件的封装导入包'''

import json
class ExcelValues:
    caseID="用例的id"
    caseModel="模块"
    caseName="接口的名称"
    caseUrl="请求地址"
    casePre="前置条件"
    method="请求方法"
    paramsType="请求格式"
    params="请求参数"
    except1="期望结果"
    isRun="是否运行"
    headers="请求头"
    status_code="状态码"

class OperationExcel:

    def getSheet(self):

        book = xlrd.open_workbook(filePath('data', 'box.xlsx'))
        return book.sheet_by_index(0)

    @property
    def getRows(self):
       '''获取总行数'''
       return self.getSheet().nrows

    @property
    def getCols(self):
        '''获取总列数'''
        return self.getSheet().ncols

    def getExcelDatas(self):
        datas=list()
        title=self.getSheet().row_values(0)
        # 忽略第一行数据
        for row in range(1,self.getSheet().nrows):
            row_values=self.getSheet().row_values(row)
            datas.append(dict(zip(title,row_values)))
        return datas
    def runs(self):
        '''获取到可执行的测试用例'''
        run_list=[]
        for item in self.getExcelDatas():
            isRun=item[ExcelValues.isRun]
            if isRun=='y':run_list.append(item)
            else:pass
        return run_list
    # def Params(self):
    #     params_list=[]
    #     for item in self.runs():
    #         params=item[ExcelValues.params]
    #         # print(params)
    #         if len(str(params).strip())==0:pass
    #         elif len(str(params).strip())>0:
    #             params=json.loads(params)
    #     return params
    def case_prve(self,casePrve):
        # '''拿到所有前置的测试点测信息'''
        for item in self.runs():
            if casePrve in item.values():
                return item
        return None
    def header_prve(self,prevResult):
        # '''拿到所有前置的测试点测信息'''
        for item in self.runs():
            headers=item[ExcelValues.headers]
            if '{token}' in headers:
                headers=str(headers).replace('{token}',prevResult)
                # print(type(headers))
                # print (json.loads(headers))
        return json.loads(headers)





if __name__ == '__main__':
    obj=OperationExcel()
    print(obj.header_prve('token'))

    # print(obj.case_prve('login')[ExcelValues.caseUrl])
    # print(obj.case_prve('login')[ExcelValues.headers])

    # for item in obj.Params():
        # print(type(item))
    # obj.getExcelDatas()
    # for item in obj.getExcelDatas():
    #     print(item[ExcelValues.caseUrl])

    # print(OperationExcel().getHtt1(1))
    # print(OperationExcel().getData1(1))
    # print(OperationExcel().getData('data','yaa.yaml',1))
    # print(OperationExcel().getUrl(1))
    # print(OperationExcel().getHtt('data', 'yaa.yaml', 1))