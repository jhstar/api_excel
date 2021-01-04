import sys
import os
base_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'base')
sys.path.append(base_path)
from method import Requests
utils_path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'utils')
sys.path.append(utils_path)
from operationExcel import OperationExcel,ExcelValues
# from common.public import *
import pytest
import json
import allure
import allure_pytest

obj=Requests()
excel=OperationExcel()

@pytest.mark.parametrize('datas',excel.runs())
def test_login_study(datas):
    # '''对参数做 反序列化处理'''
    param=datas[ExcelValues.params]
    if len(str(param).strip()) == 0: pass
    elif len(str(param).strip())>0:
        param=json.loads(param)
    # '''对请求头做 反序列化处理'''
    header = datas[ExcelValues.headers]
    if len(str(header).strip()) == 0: pass
    elif len(str(header).strip()) > 0:
        header = json.loads(header)
    status_code=int(datas[ExcelValues.status_code])
    def case_assert_result(r):
        assert r.status_code==status_code
        assert datas[ExcelValues.except1] in json.dumps(r.json(),ensure_ascii=False)
        # '''1.先获取到所有的前置测试点的用例
        #    2.执行前置测试点用例
        #    3.获取到他的结果信息
        #    4.拿他的结果信息替换对应测试点的变量
        # '''
    r = obj.post(
        url=excel.case_prve(datas[ExcelValues.casePre])[ExcelValues.caseUrl],
        data=json.loads(excel.case_prve(datas[ExcelValues.casePre])[ExcelValues.params]),
        headers=json.loads(excel.case_prve(datas[ExcelValues.casePre])[ExcelValues.headers]))
    prevResult = r.json()['data']['token']
    header=excel.header_prve(prevResult)
    # print(r.text)
    # print(r.json()['token'])
    # print(r.json()['data']['token'])

    '''用户登录成功'''
    if datas[ExcelValues.method] == 'get':
        r = obj.get(url=datas[ExcelValues.caseUrl], headers=header)
        # print(r.text)
        case_assert_result(r=r)
    elif datas[ExcelValues.method] == 'post':
        r = obj.post(url=datas[ExcelValues.caseUrl], data=param, headers=header)
        # print(r.text)
        case_assert_result(r=r)

    # print(excel.case_prve('login')[ExcelValues.caseUrl])
    # assert datas['except'] in json.dumps(r.json(),ensure_ascii=False)

if __name__ == '__main__':
    pytest.main(["-s","-v","test_login_token.py","--alluredir","./report/result"])
    import subprocess
    subprocess.call('allure generate report/result/ -o report/html --clean ',shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p 8080 ./report/html',shell=True)