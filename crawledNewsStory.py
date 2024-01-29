from crawlingTest import crawling_multiple, crawling_and_printing
import requests
from bs4 import BeautifulSoup

# TODO 기사의 본문을 크롤링하는 함수
# crawling_mulitple()에서 headline_link만 받아오기

url_prefix = 'https://www.yna.co.kr/news/'
# crawling_and_printing(url_prefix, 1, 2) # 범위 설정

def crawling_news_story(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_story = soup.select('#articleWrap > div.content01.scroll-article-zone01 > div > div > article > p')
    news_story = [tag.text for tag in news_story]
    news_story = ' '.join(news_story)
    print(news_story)
    return news_story
