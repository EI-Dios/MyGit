from bs4 import BeautifulSoup               #网页解析，获取数据
import re                   #正则表达式，进行文字匹配
import urllib.request,urllib.error          #制定URL，获取网页数据

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    #3.保存数据
    saveData(datalist)


findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)        #re.S让换行符包含在字符中

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)

        #2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):         #查找符合要求的字符串，形成列表
            item = str(item)

            imgSrc = re.findall(findImgSrc,item)[0]
            datalist.append(imgSrc)
    #print(len(datalist))
    return datalist





#得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html



def saveData(datalist):
    x = 0
    for data in datalist:
        urllib.request.urlretrieve(data,'D:\image\%s.jpg' % x)
        x += 1
    print("下载完成！")




if __name__ == "__main__":
    main()