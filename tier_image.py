# 이미지 호스팅 사이트 : https://ifh.cc/
# svg to png : https://svgtopng.com/ko/
import http.client
import json
import requests

Lvimg = ['https://ifh.cc/g/LQJ8Cl.png',
         'https://ifh.cc/g/FT8wxt.png',
         'https://ifh.cc/g/vglZza.png',
         'https://ifh.cc/g/84ZwnK.png',
         'https://ifh.cc/g/jmvQGd.png',
         'https://ifh.cc/g/vq0OmX.png',
         'https://ifh.cc/g/prytZK.png',
         'https://ifh.cc/g/4qNJzr.png',
         'https://ifh.cc/g/Qr2qts.png',
         'https://ifh.cc/g/hrqNMn.png',
         'https://ifh.cc/g/1Do8WT.png',
         'https://ifh.cc/g/7R2zBx.png',
         'https://ifh.cc/g/VvTqo3.png',
         'https://ifh.cc/g/gsskxd.png',
         'https://ifh.cc/g/9CXcLK.png',
         'https://ifh.cc/g/prjtVB.png',
         'https://ifh.cc/g/FNlh9p.png',
         'https://ifh.cc/g/bArAfo.png',
         'https://ifh.cc/g/Rs28s4.png',
         'https://ifh.cc/g/vQmNCg.png',
         'https://ifh.cc/g/BDOcSH.png',
         'https://ifh.cc/g/oNaczn.png',
         'https://ifh.cc/g/Bf33HX.png',
         'https://ifh.cc/g/GfZlFn.png',
         'https://ifh.cc/g/g5DQnz.png',
         'https://ifh.cc/g/sOo3GL.png',
         'https://ifh.cc/g/B8pVqV.png',
         'https://ifh.cc/g/Nhx9pV.png',
         'https://ifh.cc/g/Yff080.png',
         'https://ifh.cc/g/5aWOtd.png',
         'https://ifh.cc/g/fxHXjy.png']

def get_tier_img(pid):
    url = "https://solved.ac/api/v3/problem/show"

    querystring = {"problemId":pid}

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers, params=querystring)

    # print(response.json())
    lv = response.json()["level"]
    # conn = http.client.HTTPSConnection("solved.ac")
    # print(1)
    # headers = { 'Accept': "application/json" }
    # print(2)
    # conn.request("GET", "/api/v3/problem/show?problemId={}".format(pid), headers=headers)
    # print(3)
    # res = conn.getresponse()
    # data = res.read()
    # print(4)
    # print(data)
    # data = json.loads(data.decode("utf-8"),strict=False)
    # print(data)
    
    # print(5)
    # lv = int(data.get("level"))
    # print(6)
    return Lvimg[lv]
# print(get_tier_img(27449))