from lxml import etree
import requests

BASE_DOMAIN = 'http://www.ygdy8.net'

HEADERS = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/69.0.3497.100 Safari/537.36",
    }

def get_detail_urls(url):

    response = requests.get(url, headers=HEADERS)
    # print(response.text)
    # print(response.content.decode('gbk'))
    html = response.content.decode('gbk')

    html = etree.HTML(html)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    # for detail_url in detail_urls:
    #     print(BASE_DOMAIN+detail_url)
    detail_urls = map(lambda  url:BASE_DOMAIN+url, detail_urls)
    return detail_urls

def parse_detail_page(url):
    pass


def spider():
    # {}占个位置，format填充
    base_url = 'http://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html'
    for x in range(1,8):
        print("="*30)
        print(x)
        print("="*30)
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            print(detail_url)

if __name__ == '__main__':
    spider()