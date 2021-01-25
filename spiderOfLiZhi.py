from lxml import etree
import requests
from time import sleep
flag = 1
url = "https://so.jstv.com/?keyword=%E6%96%B0%E5%9E%8B%E5%86%A0%E7%8A%B6%E7%97%85%E6%AF%92&page="
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
target = open('LiZhi_news扩散.txt','w',encoding='utf-8')
for i in range(356,369):
    new_url = url+str(i)  #获得每一页的url
    page_text = requests.get(new_url,headers).text#获得该页的源代码
    #获得etree对象
    tree = etree.HTML(page_text)
    news_li_list = tree.xpath('//div[@class="lzxw_lxz"]/ul/li')
    for li in news_li_list:
        news_href = li.xpath('./span/a/@href')[0]
        news_name = li.xpath('./span/a/text()')[0]
        target.write("标题："+news_name)
        child_page_text = requests.get(news_href,headers).content.decode('utf-8')
        #print(child_page_text)
        child_tree = etree.HTML(child_page_text)
        time = child_tree.xpath('//span[@class="time"]/text()')
        if(len(time)!=0):
            target.write("   时间："+time[0])
        paragraph_list = child_tree.xpath('//div[@class="content"]/p')
        for p in paragraph_list:
            content = []
            content = p.xpath('./text()')
            if(len(content)!=0):
                target.write(content[0]+'\n')
        print("完成"+str(flag)+"项，位于第"+str(i)+"页")
        flag=flag+1
target.close()