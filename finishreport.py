import sys
import os
import requests
import re

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')#元组保存
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10#各量级对应位数
    for s in reversed(symbols):#反转元组，以最快找出符合的量级
        if n >= prefix[s]:#遇到符合的量级则计算后return
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)#按%.1f格式返回字符串
    return "%sB" % n#小于以上量级，直接返回B

def tracker2site(tracker):
    sites = {'tjupt':'TJUPT', 'btschool':'BTSchool', 'hdchina':'HDChina', 'chdbits':'CHDBits', 'npupt':'蒲公英', 'ourbits':'OurBits', 'pterclub':'PTer', 'totheglory':'TTG', 'htpt':'海棠', 'open':'OpenCD', 'soulvoice':'聆音', 'byr':'北邮人'}
    for i in sites:
        if(re.search(i, tracker)):
            return sites[i]
    return '未知站点'
    
params = sys.argv
del params[0] #删除文件路径

tracker = tracker2site(params[0])
del params[0]

size = bytes2human(int(params[0]))
del params[0]

filename = " ".join(params)
filename = filename.replace('%' , '%25')
filename = filename.replace('+' , '%2B')
filename = filename.replace('/' , '%2F')
filename = filename.replace('?' , '%3F')
filename = filename.replace('#' , '%23')
filename = filename.replace('&' , '%26')
filename = filename.replace('=' , '%3D')
filename = filename.replace(' ' , '%20')

url = "http://iyuu.cn/IYUU***.send?text=" + '【' + tracker + '】' + filename + '%20下载完成（' + size + '）'
response = requests.get(url=url)
print(response.text)

os.system("C:/IYUUAutoReseed/1.Windows辅种.cmd")