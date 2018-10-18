# 爬取豆瓣电影,练习xpath

## url：https://movie.douban.com/cinema/nowplaying/chengdu/
### 注意：  
* response.text返回的是一个经过解码后的字符串，是str(unicode)类型
* response.content返回的是一个原生的字符串，是从网页上抓取下来的，没有经过处理的字符串，
是bytes类型
* xpath规则：  
    + ./ 当前节点获取所有的子节点
    + @属性
    + .//当前节点所有节点
    + .//img/@src img标签里的src属性
* thumbnail 缩略图