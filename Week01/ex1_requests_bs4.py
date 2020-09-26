
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

movie_url = 'https://maoyan.com/films?showType=3'

header = {}
header['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
header['cookie'] = 'uuid_n_v=v1; uuid=F3CACEE0FC1C11EA8DE53FC79079ED9441FCD023D6A04384ABAB38AF63C2E217; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1600779333,1600786926,1600787346,1600822534; _lxsdk_cuid=174b139c74cc8-052d8985facd7c8-4c3f247a-1fa400-174b139c74dc8; _lxsdk=F3CACEE0FC1C11EA8DE53FC79079ED9441FCD023D6A04384ABAB38AF63C2E217; __mta=156135684.1600701187966.1600787345872.1600822534459.10; mojo-uuid=70e6c5792dccb54fdb6a06d7941d7734; _csrf=1a2a1180096594e6204fe8de3586773f7dc7b37a235e4344c5024df7d4b5d896; mojo-trace-id=1; mojo-session-id={"id":"752fbcd1dffea1ab2d845b3c6fb047a5","time":1600822534293}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1600822534; _lxsdk_s=174b875612a-a14-da7-50c%7C%7C2'

rsp = requests.get(movie_url, headers=header)
print(f"status_code: {rsp.status_code}")

#bs_info = bs(response.text, 'html.parser')
# 
#
#for tags in bs_info.find_all('div', attrs={'class':'movie-hover-info'}):
#    for div_tag in tags.find_all('div'):
#        print(type(div_tag.text))
#        print(div_tag.text)


def bs_process(response):
    item = []
    bs_info = bs(response.text, 'html.parser')

    for tags in bs_info.find_all('div', attrs={'class':'movie-hover-info'}):
        for div_tag in tags.find_all('div'):
            item.append(div_tag.text)

    return item

it_list = bs_process(rsp)


def process_10_movies_data(item_list):
    data_processed = []

    for i in range(0, 40):
        if i % 4 == 0:
            item_list[i] = item_list[i].split("\n")[1]
            data_processed.append(item_list[i])

        elif i % 4 == 1:
            item_list[i] = item_list[i].replace(" ", "")
            item_list[i] = item_list[i].replace("\n", "")
            data_processed.append(item_list[i])

        elif i % 4 == 3:
            item_list[i] = item_list[i].replace(" ", "")
            item_list[i] = item_list[i].replace("\n", "")
            data_processed.append(item_list[i])

        else:
            continue

    return data_processed

ten_movies_list = process_10_movies_data(it_list)


ten_movies_info  = pd.DataFrame(data=ten_movies_list)
ten_movies_info.to_csv("./MaoyanMovies.csv", encoding='utf-8', index=False, header=False)


print("Done!")


