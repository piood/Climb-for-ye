import requests
import sys
import io
import re
import wordcloud
import jieba
import matplotlib.pyplot as plt
sys.stdout = io.TextIOWrapper( sys.stdout.buffer, encoding='gb18030')#编码
headers={
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
	'Referer':'https://www.zhihu.com/',
	'Cookie':'_zap=d39ea999-dcf8-444d-bbb0-2cda0cafc120; _xsrf=h9rWw9E1GllsC5SWVFhNuzIwLh1rMJwC; d_c0="AFBXCSgdwRCPTq5Y9be2-hfV9PYFoGjShYU=|1580617560"; _ga=GA1.2.199974176.1582682758; __utmv=51854390.100--|2=registration_date=20181024=1^3=entry_date=20181024=1; __utma=51854390.199974176.1582682758.1583305021.1585272208.2; __utmz=51854390.1585272208.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/341975664; q_c1=9c9ff1c675e64038b8d4f73a8df65af8|1586325841000|1583305018000; tshl=; _gid=GA1.2.287555753.1587213310; tst=h; l_cap_id="YTIwYzhiMjI3NTQ0NGE0MDliMTFmYzNiZTZjNmJiNjc=|1587730036|32ef96126d9fb594b61796060856cffed84fb8eb"; r_cap_id="MjFhN2JlOGRjNmE4NGU1OTk1M2M1YmY2MWJjMTliMDA=|1587730036|b4cb68731ebb9cf87f0e05710097d99a186865c8"; cap_id="MTlmOGZmNTdiYWNiNDNjMDgyYWZhOWEzMjQ1MWEzNTg=|1587730036|2b27bc6b2c54f935d1a40cac4bc40ea1a79f4888"; capsion_ticket="2|1:0|10:1587730745|14:capsion_ticket|44:MmIzNzczZDljNjJlNGU1Y2E1YzZmYzlkNGFhYmRjYzI=|ec1563485d9859e93670e450806fc90bda9e3c37ecf1f5e0924bcc207c05cf09"; z_c0="2|1:0|10:1587730749|4:z_c0|92:Mi4xMHE2ZUdRQUFBQUFBVUZjSktCM0JFQ1lBQUFCZ0FsVk5QQ2VRWHdCMEw4SkIweFhYdjM2MkNRYlJST05vQmp1YV9R|88f851b854eea8ad6729fb2429a78fc05904beb9e2c2db789a5876569d1ec64e"; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1587727997,1587730067,1587730328,1587776517; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1587776517; _gat_gtag_UA_149949619_1=1; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1587776512|1587776509; SESSIONID=p7nbxGhl3KjKzVkhyjXr4iclHgP18JaYYcrceiKgOxy; JOID=VVsUBknAQ0LGbpmGd8KCGHEOUaxgtHYooxPa7B_2DCqJE8rpHcbJ4ppvn4B0mt4-2fxJ44bNWRpplWC67e7yNmU=; osd=W10RAEPORUfAZJeAcsSIFncLV6ZusnMuqR3c6Rn8AiyMFcDnG8PP6JRpmoZ-lNg73_ZH5YPLUxRvkGaw4-j3MG8='
}#Cookie要更改
response=requests.get("https://www.zhihu.com/hot",headers=headers)#知乎热榜链接
html=response.text
html_list=re.findall(r'</div></div><div class="HotItem-content"><a href="(.*?)" title="', html)#抓取所有热榜话题链接
print(html_list)
print(len(html_list))
label_list=[]
for i in range(0, 50):
	hot_response=requests.get(html_list[i], headers=headers)#必须要有headers,要不然无法访问
	hot_html=hot_response.text
	hot_label=re.findall(r'keywords" content="(.*?)"/><meta itemProp="answerCount"', hot_html)#抓取所有热词
	hot_name=re.findall(r'><title data-react-helmet="true">(.*?)？ - 知乎</title><meta name="viewport"', hot_html)#抓取标题
	print('%d.'%(i+1), end='')
	print(hot_name[0])
	for i in range(len(hot_label)):
		label_list.append(hot_label[i])
print(label_list)
label_string=" ".join(label_list)#转换为string型
print(label_string)
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')
w.generate(label_string)
w.to_file('zhihu.png')#生成词云图片
