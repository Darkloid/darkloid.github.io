import subprocess
import re
import requests

getIPV6_process = subprocess.Popen("ipconfig", stdout = subprocess.PIPE)

output = (getIPV6_process.stdout.read())

ipv6_pattern='2403:ac00:[0-9a-f:]+'
ipv4_pattern='172\.20\.[0-9]{1,3}\.[0-9]{1,3}'
ipv4_local_pattern='172\.17\.[0-9]{1,3}\.[0-9]{1,3}'

ipv6 = re.search(ipv6_pattern, str(output))
ipv4 = re.search(ipv4_pattern, str(output))
ipv4_local = re.search(ipv4_local_pattern, str(output)).group()

if ipv6 is not None:
    ipv6 = ipv6.group()
else:
    ipv6 = ''

if ipv4 is not None:
    ipv4 = ipv4.group()
else:
    ipv4 = ''

print(ipv4)
url = "http://dynv6.com/api/update?hostname=darkloid.dynv6.net&token=C745iSAq5fQyfubay_V6YWP2_b6_rL&ipv4=" + ipv4
response = requests.get(url=url)
print(response.text)

print(ipv6)
# url = "http://dynv6.com/api/update?hostname=darkloid.dynv6.net&token=C745iSAq5fQyfubay_V6YWP2_b6_rL&ipv6=" + ipv6
# response = requests.get(url=url)
# print(response.text)

print(ipv4_local)
url = "http://dynv6.com/api/update?hostname=darkloid-local.dynv6.net&token=erySEmcsdzBHtxTU8omU1XCyScgyJU&ipv4=" + ipv4_local
response = requests.get(url=url)
print(response.text)

url = "http://iyuu.cn/IYUU6284T8564b4f14627a55d57f5bcdca4bc235701b4654a.send?text=NAS%20IP地址已更新&desp=" + ipv4 + "\n" + ipv4_local + "\n" + ipv6
response = requests.get(url=url)
print(response.text)