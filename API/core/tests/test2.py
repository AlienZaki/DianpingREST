import requests
import pickle

session = requests.Session()

print('=> Loading session...')
try:
   cookies = pickle.load(open("cookies_dianping.pkl", "rb"))
   session.cookies.update(cookies)
   print('=> Session loaded!')
except:
   print('=> WARNING: Couldn\'t load cookies.')







from fake_useragent import UserAgent
ua = UserAgent()


proxies = {
    'http': 'http://5.79.73.131:13010',
    'https': 'http://5.79.73.131:13010',
}


url = "http://www.dianping.com/review/ajax/reviewfollownote"

payload = "reviewId=1070162806&nextIndex=1"
headers = {
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Cookie': '_lxsdk_cuid=Zaksi;',
  'User-Agent': ua['google chrome']
}
#session.get('http://dianping.com')
session.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
session.cookies['_lxsdk_cuid'] = 'Zaksi'
#response = requests.request("GET", 'http://api.ipify.org?format=json', headers=headers, data=payload, proxies=proxies)
response = session.post(url, data=payload, proxies=proxies)

print(response.text)





print('=> Saving session...')
pickle.dump(session.cookies, open("cookies_dianping.pkl", "wb"))
print('=> Session saved!')