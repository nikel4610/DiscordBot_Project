from crawlingTest import crawling_multiple, crawling_and_printing
import requests
from bs4 import BeautifulSoup

# TODO 기사의 본문을 크롤링하는 함수
# crawling_mulitple()에서 headline_link만 받아오기

url_prefix = 'https://www.yna.co.kr/news/'
crawling_and_printing(url_prefix, 1, 2) # 범위 설정

def crawling_news_story(url):
    crawling_multiple(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_story = []

    # //*[@id="articleWrap"]/div[2]/div/div/article/p[1]/text()
    # TODO 이거 왜 안됨? Xpath 로 크롤링 하려는데 오류 남
    # soupsieve.util.SelectorSyntaxError: Malformed attribute selector at position 1

    for i in range(1, 100):
        news_story_element = soup.select_one(f'//*[@id="articleWrap"]/div[2]/div/div/article/p[{i}]')
        # 뒤에 /text() 붙은것도 있고 아닌것도 있음 번호 상관 없이 
        if news_story_element:
            news_story.append(news_story_element.text)
        else:
            break

    return news_story

for i in range(1, 2):
    url = url_prefix + str(i)
    print(crawling_news_story(url))



# -> test()가 붙은것과 안붙은것 차이? p[?] 번호에 상관없이 text()가 붙은것도 있고 아닌것도 있음

