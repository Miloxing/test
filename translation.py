import urllib.request
import urllib.parse
import json
import time
import random


while True:
    content = input ('输入要翻译的内容(输入‘q!’退出程序)：')
    if (content!='q!'):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

        iplist = ['119.28.50.37:82','120.77.201.46:8080','211.147.67.150:80']

        proxy_support = urllib.request.ProxyHandler({'http':random.choice(iplist)})

        opener = urllib.request.build_opener(proxy_support)
        
        
        data = {
        'i':'why','from':'AUTO','to':'AUTO','smartresult':'dict','client':'fanyideskweb','salt':'1519199592010','sign':'a7309c59c5824e048c8988ee2b010d48','doctype':'json','version':'2.1','keyfrom':'fanyi.web','action':'lan-select','typoResult':'false'}
        data['i']=content
        data = urllib.parse.urlencode(data).encode('utf-8')

        req=urllib.request.Request(url,data)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')

        response = opener.open(req)
        
        html = response.read().decode('utf-8')

        target = json.loads(html)
        print('翻译结果：%s'% (target['translateResult'][0][0]['tgt']))
        time.sleep(3)
    else:
        break


