import requests,time
from  bs4  import BeautifulSoup
#dc0741e1-da3b-4078-b899-b101395ccd5b
s= requests.session()
data="grant_type=password&company_id=null&password=10203040Aa%40%40&scope=first_party%2Cidentity.basic%2Cpublic%2Ctoken.refresh&username=&client_id=3e066b50-6598-11e7-a07a-db7aca4729b6"

headers={
    'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9,fr;q=0.8',
'content-length': '203',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://dashboard.envoy.com',
'referer': 'https://dashboard.envoy.com/',
'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

res = s.post("https://app.envoy.com/a/auth/v0/token",headers=headers,data=data)
time.sleep(3)
res = s.get("https://dashboard.envoy.com/")
soup = BeautifulSoup(res.text,"lxml")
print(res.text)