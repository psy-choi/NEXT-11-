from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

# 디버깅 모드

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = 'chromedriver_win32'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

driver.get("https://movie.naver.com/")

time.sleep(1)
rankbtn = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/div[1]/div/div/ul/li[3]/a')
rankbtn.click()

# #1위부터 20위까지 가져오기
# for i in range(2,23):
#     time.sleep(1)
#     if i == 12:
#         continue
#     new_i = str(i)
#     movie = driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr['+new_i+']/td[2]/div/a').text
#     print(movie)


# 1위부터 20위까지 개요 감독, 평점
file = open('movie120.csv', mode="w", newline="")
writer = csv.writer(file)
for i in range(10, 23):
    if i == 12:
        continue
    time.sleep(2) # 접속
    moviebtn = driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr['+str(i)+']/td[2]/div/a')
    moviebtn.click()
    
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # 개요
    genre = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a:nth-child(1)')
    print("개요 :", genre.get_text())
    
    # 감독
    director = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a')
    print("감독 :", director.get_text())
    
    # 평점
    try:
        score = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a/div/span/span').text        
        new_score = score.split(" ")[2]
        print("평점 :", score.split(" ")[2])
    except NoSuchElementException:
        score = "아직 집계 되지 않았습니다."
        new_score = score
        print("평점 :", score)
    time.sleep(1)
    writer.writerow([genre.get_text(), director.get_text(), score])
    driver.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")

file.close()
    
# 본인이 좋아하는 영화 + csv로 저장
driver.get("https://movie.naver.com/")

search_box = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/fieldset/div/span/input')
search_box.send_keys('엣지 오브 트모로우')
inputbtn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/fieldset/div/button')
inputbtn.click()

time.sleep(1)

inputbtn = driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div/div[1]/ul[2]/li[1]/dl/dt/a')
inputbtn.click()

time.sleep(1)

html2 = driver.page_source
soup = BeautifulSoup(html2, 'html.parser')
title = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > h3 > a').get_text()
director = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a').get_text()

# 스크롤 내리기
driver.execute_script("window.scrollTo(0, 700)")

score = soup.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_area > div.netizen_score > div > div > em').get_text()
review = soup.select_one('#content > div.article > div.section_group.section_group_frst > div:nth-child(5) > div:nth-child(2) > div.score_total > strong > em').get_text()
print("제목 :",title)
print("감독 :",director)
print("평점 :",score)
print("리뷰 개수:",review.strip())

# file = open('movie.csv', mode="w", newline="")
# writer = csv.writer(file)
# time.sleep(3)
# writer.writerow([title, director, score, review])
# file.close()