import requests
from bs4 import BeautifulSoup

def crawling_multiple(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    times = []
    headline_links = []
    headlines = []

    for i in range(1, 27):
        time_element = soup.select_one(f'#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child({i}) > div > div.info-box01 > span.txt-time')
        headline_link_element = soup.select_one(f'#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child({i}) > div > div.news-con > a')
        headline_element = soup.select_one(f'#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child({i}) > div > div.news-con > a > strong')

        # Check if elements are found before accessing attributes
        if time_element and headline_link_element and headline_element:
            times.append(time_element.text)
            headline_links.append(headline_link_element['href'])
            headlines.append(headline_element.text)

    return times, headline_links, headlines

def crawling_and_printing(url_prefix, start, end):
    for i in range(start, end + 1):
        url = url_prefix + str(i)
        times, headline_links, headlines = crawling_multiple(url)

        # Now you can access the individual lists for each attribute
        for time, headline_link, headline in zip(times, headline_links, headlines):
            print(time, headline_link, headline)

url_prefix = 'https://www.yna.co.kr/news/'
crawling_and_printing(url_prefix, 1, 2)

# TODO time 시간을 날짜와 시간으로 나눠서 저장해야 함 -> 후에 같은 날짜만 모아서 내용 요약 + 키워드 추출
# TODO headline_link 기사의 본문을 크롤링해야 함 -> crawledNewsStory.py 에서 링크를 받아서 본문 내용만 크롤링 하는 코드 작성하기