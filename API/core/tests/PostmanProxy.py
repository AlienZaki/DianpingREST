import requests

headers = {
    'Host': 'orion-http.gw.postman.co',
    'pm-u': None,
    'pm-h0': '',
    'pm-o0': 'method={method}, timings=true, timeout=180000, rejectUnauthorized=true',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjNlNTM0MjM1LWY5YzAtNDE2OC04NTc5LTViZDY5Zjk0NjBiMCIsInVzZXJJZCI6NjUwMjM4NSwidGVhbUlkIjoyMTc4NTQzLCJpdiI6IjByY0xRSHN5Q3FPaG8rdEpBeVJqbmc9PSIsImFsZ28iOiJhZXMtMTI4IiwiaWF0IjoxNjUxMjk0OTEyLCJleHAiOjE2NTEyOTY3MTJ9.JuJw8XDetIBGE2Bu63zCgb0Uo2__pUOV9y82MevPGmM',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
    'origin': 'https://orange-spaceship-502414.postman.co',
}

data = '------WebKitFormBoundaryX7IL5f93TrDhtdtA\nContent-Disposition: form-data; name="a"\n\nx\n------WebKitFormBoundaryX7IL5f93TrDhtdtA--\n'


def request(**kwargs):
    headers['pm-u'] = kwargs['url']
    headers['pm-o0'] = headers['pm-o0'].format(method=kwargs['method'])
    if kwargs['headers']:
        headers['pm-h0'] = ', '.join([f"{h}={kwargs['headers'][h]}" for h in kwargs['headers'].keys()])
    data = kwargs['data']
    print(data)

    res = requests.post('https://orion-http.gw.postman.co/v1/request', headers=headers, data=data,)

    return res


if __name__ == '__main__':
    url = "http://www.dianping.com/review/ajax/reviewfollownote"
    xheaders = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '_lxsdk_cuid=Zaksi;',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2762.73 Safari/537.36'
    }

    payload = f'reviewId=1078184745&nextIndex=1'
    r = request(method='post', url=url, data=payload, headers=xheaders)
    print(r.text, r.status_code)