import requests
from bs4 import BeautifulSoup as bs
from bs4 import element
# bs4是第三方库需要使用pip命令安装

USER_AGENT_LIST=[
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
import random
user_agent = random.choice(USER_AGENT_LIST)

#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#cookies = "__mta=248370744.1600703562557.1600937071415.1600937825386.9; uuid_n_v=v1; uuid=7A474480FC2211EAB366D3CFFA52AB5D147C2F0BB6504C64AD027AADC98402E7; _lxsdk_cuid=174b15e01c524-0488db7255f902-316b7004-1fa400-174b15e01c6c8; _lxsdk=7A474480FC2211EAB366D3CFFA52AB5D147C2F0BB6504C64AD027AADC98402E7; mojo-uuid=1d28855e9df5055a9123afe5e7799710; _csrf=5c2c521b67fff8bbc2f8d3947b71cdebea3a45b74bb6d5a6abdae3a089a090cd; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1600703562,1600874151,1600936744,1600937321; __mta=248370744.1600703562557.1600937071415.1600937320882.9; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1600937825; _lxsdk_s=174bf4415e5-a17-6c0-9c0%7C%7C14"

#header = {'user-agent':user_agent,'Cookie':cookies}
header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

# 打开猫眼的本地文件
# f = open("work1/经典影片_电影大全_经典高清电影-猫眼电影.htm",'r')
# response = f.read()
# f.close
#print(response)
bs_info = bs(response.text, 'html.parser')


a= 0
films_list = []
for movies in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}):
    if a < 10:
        for movie in movies.find_all('a'):
                # 打印出span的内容，即 name
                film_name = movie.find('span').text.replace('\n', '').replace(' ','')
                print(film_name.replace('\n', '').replace(' ',''))
                # 打印出href的属性值，即 link
                #print('https://maoyan.com'+ movie.get('href'))
                # 打印出电影类型，即<div class="movie-hover-title" title="我的女友是机器人">的第二个内容
                # movie_hover_title_list = list(movie.find_all('div',attrs={'class':'movie-hover-title'}))
                # movie_hover_title_list_type = movie_hover_title_list[1]
                # print("===========================================================")
                # print(type(movie_hover_title_list_type))
                # print(movie_hover_title_list_type)
                # print("===========================================================")
                # print(type(movie_hover_title_list_type.text))
                # print(movie_hover_title_list_type.text)
                # print("===========================================================")
                film_type = list(movie.find_all('div',attrs={'class':'movie-hover-title'}))[1].text.replace('\n', '').replace(' ','')
                #print(film_type.replace('\n', '').replace(' ',''))
                # 打印上映时间
                film_time = movie.find('div',attrs={'class':'movie-hover-title movie-hover-brief'}).text.replace('\n', '').replace(' ','')
                print(film_time.replace('\n', '').replace(' ',''))
                # 将每个电影信息保存成列表
                film_list = [film_name,film_type,film_time]
        a+=1
        # 将每个电影信息列表添加到前十个电影列表内
        films_list.append(film_list)
    else:
        break

# print(films_list)
import pandas as pd
movie_pd = pd.DataFrame(data= films_list)

movie_pd.to_csv('./work1/movies.csv',encoding='utf8',index=False,header=False)


