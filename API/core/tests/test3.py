import requests

url = "https://orion-http.gw.postman.co/v1/request"

payload = "reviewId=1077938928&nextIndex=1"
headers = {
  'authority': 'orion-http.gw.postman.co',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
  'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjNlNTM0MjM1LWY5YzAtNDE2OC04NTc5LTViZDY5Zjk0NjBiMCIsInVzZXJJZCI6NjUwMjM4NSwidGVhbUlkIjoyMTc4NTQzLCJpdiI6IjByY0xRSHN5Q3FPaG8rdEpBeVJqbmc9PSIsImFsZ28iOiJhZXMtMTI4IiwiaWF0IjoxNjUxMjk0OTEyLCJleHAiOjE2NTEyOTY3MTJ9.JuJw8XDetIBGE2Bu63zCgb0Uo2__pUOV9y82MevPGmM',
  'cache-control': 'no-cache',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://orange-spaceship-502414.postman.co',
  'pm-h0': 'Content-Type=application/x-www-form-urlencoded; charset%3DUTF-8, User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/52.0.2762.73 Safari/537.36, Accept=*/*, Cache-Control=no-cache, Postman-Token=baec8ad7-3271-4cf8-b1e4-52cd4e3ae7b2, Host=www.dianping.com, Accept-Encoding=gzip%2C deflate%2C br, Connection=keep-alive, Cookie=_lxsdk_cuid%3DZaksi;',
  'pm-o0': 'method=POST, timings=true, timeout=180000, rejectUnauthorized=true',
  'pm-u': 'http://www.dianping.com/review/ajax/reviewfollownote',
  'pragma': 'no-cache',
  'referer': 'https://orange-spaceship-502414.postman.co/workspace/My-Workspace~39eb9c71-4306-45c1-8735-259bcbef180d/request/6502385-d97c6f04-fff9-461f-85b2-efb34cd94040',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'sec-gpc': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
