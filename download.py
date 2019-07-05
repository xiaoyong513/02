# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://k6.csnjcbnxdnb.xyz/pw/thread.php?fid=111'
asia_response = requests.get(url)
asia_response.encoding = 'utf-8'
asia_soup = BeautifulSoup(asia_response.text, "html.parser")
titles = asia_soup.select("h3 a")  # CSS 选择器
# for title in titles:
    # print(title.get_text(), title.get('href'))  # 标签体、标签属性

video_html_url = 'http://k6.csnjcbnxdnb.xyz/pw/html_data/111/1907/4162136.html'
video_html_response = requests.get(video_html_url)
video_html_response.encoding = 'utf-8'
video_html_soup = BeautifulSoup(asia_response.text, "html.parser")
print(video_html_soup)
