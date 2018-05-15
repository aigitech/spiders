# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import os
import requests
url = 'http://www.yestone.com/gallery/1501754333627'
start_url = requests.get(url)
soup =BeautifulSoup(start_url.text,'lxml')
items = soup.find_all('img',class_='img-responsice')
folder_path = './photo'
if os.path.exists(folder_path) == False:
    os.makedirs(folder_path)
for index,item in enumerate(items):
    if item:
        html = requests.get(item.get('data-src'))
        img_name = folder_path + str(index + 1) + '.png'
        image = Image.open(BytesIO(html.content))
        image.save('E:\yesone\pic' + img_name)
        print("第%d张图片下载完成" %(index + 1))
        time.sleep(1)
    print("图片抓取完成！")