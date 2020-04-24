import requests
import re
import sys
import io
import wordcloud
import jieba
import matplotlib.pyplot as plt
sys.stdout = io.TextIOWrapper( sys.stdout.buffer, encoding='gb18030')
url='https://www.bilibili.com/ranking'
response=requests.get(url)
html=response.text
video_list=re.findall(r'<a href="(.*?)" target="_blank">', html)
label_list=[]
video_name=re.findall(r'target="_blank" class="title">(.*?)</a><!----><div class="detail"><span class="data-box">',html)
video_play=re.findall(r'<i class="b-icon play"></i>(.*?)</span>', html)
video_view=re.findall(r'<i class="b-icon view"></i>(.*?)</span><a target="_blank"',html)
video_up=re.findall(r'<i class="b-icon author"></i>(.*?)</span></a>', html)
for i in range (0, 100):
	print('%d.'%(i+1), end='')
	print('%-65s'%video_name[i],end='')
	print('up主: %-15s'%video_up[i], end='')
	print('播放数: %-8s'%video_play[i], end='')
	print('评论数: %s'%video_view[i])
for video in video_list:
	video_response=requests.get(video)
	video_html=video_response.text
	video_label=re.findall(r'target="_blank">(.*?)</a>', video_html)
	for label in video_label:
		if(label!='美食作家王刚R'):
		    label_list.append(label)
label_string=" ".join(label_list)
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')
w.generate(label_string)
w.to_file('BiliBili.png')