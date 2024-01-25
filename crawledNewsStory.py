from crawlingTest import crawling_multiple
import requests
from bs4 import BeautifulSoup

# TODO 기사의 본문을 크롤링하는 함수
# headline_link 에 저장된 링크를 받아서 본문 내용만 크롤링하는 def

# //*[@id="articleWrap"]/div[2]/div/div/article/p[1]/text()
# //*[@id="articleWrap"]/div[2]/div/div/article/p[2]/text()
# //*[@id="articleWrap"]/div[2]/div/div/article/p[3]
# //*[@id="articleWrap"]/div[2]/div/div/article/p[4]
# //*[@id="articleWrap"]/div[2]/div/div/article/p[5]

# -> test()가 붙은것과 안붙은것 차이? p[?] 번호에 상관없이 text()가 붙은것도 있고 아닌것도 있음

