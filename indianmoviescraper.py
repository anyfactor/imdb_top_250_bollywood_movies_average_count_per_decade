from selenium import webdriver
import csv

browser= webdriver.Chrome()
browser.get('https://www.imdb.com/india/top-rated-indian-movies/')

outputFile = open('bollyimdb.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)


for i in range(1, 251):
    list_elem = browser.find_element_by_xpath(f'//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[{i}]')
    movie = list_elem.find_element_by_xpath('td[2]/span')
    year = list_elem.find_element_by_xpath('td[2]/a')
    rating = list_elem.find_element_by_xpath('td[3]/strong')
    outputWriter.writerow([movie.text, year.text, rating.text])

outputFile.close()
print('done!!')
