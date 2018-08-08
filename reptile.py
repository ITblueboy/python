# coding: utf-8
import urllib2
import re
from bs4 import BeautifulSoup

# 使用python标准库获取指定URL的响应


def OpenPage(url):
    Myheaders = {}
    # urllib2.Request方法构建http请求
    request = urllib2.Qequest(url, headers=Myheaders)
    f = urllib2.urlopen(request)
    data = f.read()
    # python内置的解码方法 decode解码 encode编码
    return data.decode("GBK", errors="ignore").encode("utf-8")


# 从小说主页获取各个章节的URL
def ParseMainPage(page):
    #调用BeatifulSoup库解析页面 
    soup = BeautifulSoup(page,"html.parser")
    #find_all方法查询所有的指定内容
    #包含read字符串的href链接 通过正则表达式
    list_charts = soup.find_all(href=re.compile("read"))
#    url_list = ["http://www.shengxu6.com" + item['href'] for item in list_charts]
    url_list = []
    for item in list_charts:
        #print type(item)
        #每一个item是一个tag标签类的实例化对象
        #通过item['href'] 可以获取到href的值
        #print item["href"]
        url_list.append("http://www.shengxu6.com" + item['href'])

    return url_list


# 根据各个章节的URL获取章节名和正文
def ParseDetailPage(page):
    soup = BeautifulSoup(page, "html.parser")
    # get_text 方法获取标签类包含的内容
    title = soup.find_all(class_="panel-heading")[0].get_text()
    content = soup.find_all(class_="content-body")[0].get_text()
    return title, content[:-12]


# 把数据写入输出文件
def WriteDataToFile(data):
    with open("output.txt", "a+") as f:
        f.write(data)


def Test():
    print OpenPage("http://www.shengxu6.com/book/2967.html")
    ParseMainPage()
    ParseDetailPage()
    print title
    print content


if __name__ == "_main_":
    # 打开主页
    MainPage = OpenPage("http://www.shengxu6.com/book/2967.html")
    # 解析主页，获得各个章节URL
    GetUrl = ParseMainPage(MainPage)
    for item in GetUrl:
        # 打开章节页面
        print "Clone " + item
        page = OpenPage(item)
        # 获取章节标题和正文
        title, content = ParseDetailPage(page)
        print "Clone title is" + title
        data = "\n\n\n" + title + "\n\n\n" + content
        WriteDataToFile(data.encode("utf-8"))
