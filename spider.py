import requests
from lxml import etree

# 1. 将目标网站的页面抓取下来
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/69.0.3497.100 Safari/537.36",
    'Referer': "https://movie.douban.com/explore"
}
url = 'https://movie.douban.com/cinema/nowplaying/chengdu/'
response = requests.get(url, headers=headers)
# print(response.text)
html = response.text


# 2. 将抓取的数据进行提取
html = etree.HTML(html)
# ul有两个，正在热映和即将上映的，取第一个
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode("utf-8"))
# 当前ul 下所有的Li
lis = ul.xpath("./li")
movies = []
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    duration = li.xpath("@data-duration")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actor = li.xpath("@data-actors")
    poster = li.xpath(".//img/@src")[0]
    movie = {
        'title': title,
        'score': score,
        'duration': duration,
        'region': region,
        'director': director,
        'actor': actor,
        'thumbnail': poster
    }
    movies.append(movie)
print(movies)