import requests
import re
import sys
import io
import wordcloud
import jieba
import matplotlib.pyplot as plt
sys.stdout = io.TextIOWrapper( sys.stdout.buffer, encoding='gb18030')#编码
url='https://www.bilibili.com/ranking'#B站排行榜链接
response=requests.get(url)
html=response.text
video_list=re.findall(r'<a href="(.*?)" target="_blank">', html)#B站排行榜链接列表
label_list=[]
video_name=re.findall(r'target="_blank" class="title">(.*?)</a><!----><div class="detail"><span class="data-box">',html)#B站排行榜视频名
video_play=re.findall(r'<i class="b-icon play"></i>(.*?)</span>', html)#播放数
video_view=re.findall(r'<i class="b-icon view"></i>(.*?)</span><a target="_blank"',html)#评论数
video_up=re.findall(r'<i class="b-icon author"></i>(.*?)</span></a>', html)#UP主
for i in range (0, 100):
	print('%d.'%(i+1), end='')
	print('%-65s'%video_name[i],end='')
	print('up主: %-15s'%video_up[i], end='')
	print('播放数: %-8s'%video_play[i], end='')
	print('评论数: %s'%video_view[i])#循环输出视频名、 UP主、 播放数、 评论数
for video in video_list:
	video_response=requests.get(video)
	video_html=video_response.text
	video_label=re.findall(r'target="_blank">(.*?)</a>', video_html)
	for label in video_label:
		label_list.append(label)#把排行榜视频的所有标签添加进label_list
label_string=" ".join(label_list)#把label_list转string型
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')
w.generate(label_string)
w.to_file('BiliBili.png')
