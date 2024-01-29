from crawlingTest import crawling_multiple, crawling_and_printing
import requests
from bs4 import BeautifulSoup

# TODO 기사의 본문을 크롤링하는 함수
# crawling_mulitple()에서 headline_link만 받아오기

url_prefix = 'https://www.yna.co.kr/news/'
crawling_and_printing(url_prefix, 1, 2) # 범위 설정

# //*[@id="articleWrap"]/div[2]/div/div/article = xpath
# 위의 xpath 에 있는 <p></p> 태그 안에 있는 본문 내용을 크롤링 하는 def
# url은 crawling_multiple()에서 받아온 headline_link

def crawling_news_story(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_story = soup.select_one('#articleWrap > div.content01.scroll-article-zone01 > div > div > article')
    print(news_story.text)
    return news_story

crawling_news_story('https://www.yna.co.kr/view/AKR20240129101900061?section=news')

