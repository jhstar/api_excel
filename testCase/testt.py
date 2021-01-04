import json
import requests
import base64
def getHeaders():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer':'https://open.shiguangkey.com/?version&showClose=true&isRegister&bindPhone=false&wechat=false&token=&autoClose=true&systemId=0&inviteLinkId=&local=',
        'terminaltype':'4'
    }
    return headers


def getData():
    dict1={
        'account':'t0327627844',
        'password':'nL+KTcuOMGgrkn81LWVZoA',
        'inviteLinkId':'',
        'ticketLogin': '1'}
    return dict1
def login():
    # s=requests.session()
    r=requests.post(
        url='https://open.shiguangkey.com/api/udb/login/standard',
        data=getData(),
        headers=getHeaders()
    )
    return r.json()['data']['token']

# def queryHeaders():
#     headers={
#         'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
#         'terminaltype':'4',
#         'referer':'https://www.shiguangkey.com/i/course',
#         # 'content-type':'application/x-www-form-urlencoded',
#         'token':'{0}'.format(login())
#        }
#     return headers
# def queryByStudent():
#     # s=requests.session()
#     r=requests.post(
#         url='https://open.shiguangkey.com/api/pcweb/course/queryByStudent',
#         data={
#             'pageIndex':'1',
#             'pageSize':'10'
#         },
#         headers=queryHeaders()
#     )
#     return r.text
def UploadHeaders():
    headers={
        "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        "terminaltype":"4",
        "referer":"https://www.shiguangkey.com/i/profile",
        "content-type":"application/x-www-form-urlencoded",
        "token":"{0}".format(login())
       }
    return headers


# def imgtrans():
#     with open("C:/Users/Administrator/Desktop/1.jpg", "rb") as f:  # 二进制方式打开图文件
#         base64_str = base64.b64encode(f.read())
#     return base64_str
# def getdataimg():
#     data={
#         'img':'{0}'.format(imgtrans())
#         # 'terminalType':'4'
#     }
#     return data

# def Upload():
#     r=requests.post(
#         url='https://www.shiguangkey.com/api/file/base64Upload',
#         headers=UploadHeaders(),
#         data=getdataimg(),
#         files={"file":("1.jpg",open("C:/Users/Administrator/Desktop/1.jpg","rb"),"image/jpeg",{})}
#     )
#     return r.json()['data']['path']
def getdata1():
    data={
       "nickname":"顽皮的虎头兰",
        "gender": "1",
        "qq": "343453",
        "wechat": "453453453543",
        "description":"你34534534534uuuu6"
    }
    return data
def updates():
    r=requests.post(
        url='https://open.shiguangkey.com/api/udb/user/update/userinfo',
        data=getdata1(),
        headers=UploadHeaders()
    )
    return r.text
if __name__ == '__main__':

    updates()
    print(updates())