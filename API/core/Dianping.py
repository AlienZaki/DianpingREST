import traceback
from multiprocessing.dummy import Pool
#from fake_useragent import UserAgent
import requests, json
import time


class Dianping:

    #ua = UserAgent()
    def __init__(self, proxy=None):
        self.session = requests.session()
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36' #self.ua['google chrome']
        self.session.headers['channel'] = 'H5'
        self.session.headers['Cookie'] = '_lxsdk_cuid=Zaki;'
        self.session.headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        self.proxy = proxy

    def get_shopuuid_from_URL(self, url):
        return url.split('/shop/')[1]

    def get_review_responses(self, review):
        review['response_list'] = []
        print(f'=> Getting Review {review["id"]} responses...')
        try:
            url = "http://www.dianping.com/review/ajax/reviewfollownote"
            proxies = {
                'http': f'http://{self.proxy}',
                'https': f'http://{self.proxy}',
            }
            print(proxies)
            #self.session.headers['User-Agent'] = self.ua['google chrome']
            payload = f'reviewId={review["id"]}&nextIndex=1'
            r = self.session.post(url, headers=self.session.headers, data=payload, proxies=proxies)
            if r.status_code == 200 and r.json() and r.json()['code'] == 200:
                responses = [{'date': res['noteDate'], 'author': res['userNickName'], 'text': res['noteBody']}
                             for res in r.json()['msg']['dataList']]
                responses.sort(key=lambda item: item['date'], reverse=True)
                review['response_list'] = responses
            else:
                print('ERROR: Couldn\'t get responses!')
                print(r.text, r.status_code)
        except Exception as e:
            print('ERROR:', e)
            traceback.print_exc()
        print(review)
        return review

    def get_hotel_reviews(self, shopuuid):
        print('=> Getting Reviews...')
        reviews = []
        try:
            r = self.session.get(f'https://m.dianping.com/wxmapi/shop/shopinfo?shopUuid={shopuuid}')
            shop_id = r.json()['shopInfo']['shopId']
            index, limit = 0, 50    # If you increased the limit over 50, comments wil not be shown
            while True:
                url = f'https://ihotel.meituan.com/api/v2/comments/biz/overseaReviewList?platform=1&start={index}&querytype=0&limit={limit}&referid={shop_id}&filterid=300'
                print(url)
                r = self.session.get(url)
                if r.status_code == 200 and r.json()['Data']['List']:
                    data = r.json()['Data']
                    for rev in data['List']:
                        review = {}
                        review['id'] = rev['MainId']
                        review['url'] = f"https://m.dianping.com/review/{rev['MainId']}"
                        review['date'] = time.strftime("%Y-%m-%d", time.localtime(rev['ModifyTime'] / 1000))
                        review['author'] = rev['FeedUser']['UserName']
                        review['score'] = rev['Star'] / 10
                        review['text'] = rev['Content']
                        review['response_list'] = [{'author': i['FromUser']['UserName'], 'date': i['CommentTime'], 'text': i['Content']}
                                                   for i in rev['Comments']] if rev['Comments'] else None   # Get Merchant Responses

                        reviews.append(review)

                    if data['IsEnd']:
                        break
                    else:
                        index += limit
                else:
                    print(r.text)
                    print(r.status_code)

            reviews = list({v['id']: v for v in reviews}.values())  # remove duplicates

            # Getting Reviews' Responses.
            #with Pool(1) as pool:
            #    reviews = pool.map(self.get_review_responses, reviews)
            #    reviews.sort(key=lambda item:item['date'], reverse=True)
            #review['response_list'] = self.get_review_responses(review_id=review['id'])
            return reviews
        except Exception as e:
            print('ERROR:', e)
            traceback.print_exc()

    def get_hotel_info(self, url):
        shopuuid = self.get_shopuuid_from_URL(url)
        url = f'https://mapi.dianping.com/mapi/wechat/shop.bin?shopuuid={shopuuid}'
        r = self.session.get(url)
        data = r.json()
        res = {}
        res['hotel_data'] = {'shop_uid': shopuuid}
        res['hotel_data']['name'] = f"{data['name']} - {data['branchName']}"
        res['hotel_data']['score'] = data['shopPowerRate']
        res['hotel_data']['stars'] = data['shopPower'] / 10
        res['hotel_data']['num_of_reviews'] = data['voteTotal']
        res['hotel_data']['address'] = data['address']
        res['hotel_data']['geo_lat'] = data['geoPoint']['lat']
        res['hotel_data']['geo_long'] = data['geoPoint']['lng']
        res['hotel_data']['region'] = data['regionName']
        res['review_list'] = self.get_hotel_reviews(shopuuid)

        #!!! Remove in production !!!#
        #with open(f'output/Dianping_{shopuuid}.json', 'w', encoding='utf-8-sig') as f:
        #    f.write(json.dumps(res, ensure_ascii=False).encode('utf8').decode())

        return res


if __name__ == '__main__':
    url = 'http://www.dianping.com/shop/G2LQYgctM49uMwzc'  # l4Ty2j8mxAJwtJju k26DvIxfKW2i1jgM juMxXiyFFBAbQJmn
    res = Dianping(proxy='5.79.73.131:13010').get_hotel_info(url)

