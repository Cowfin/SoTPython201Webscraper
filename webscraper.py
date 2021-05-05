from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.trademe.co.nz/gaming'
web = requests.get(URL)
content = BeautifulSoup(web.content, 'html.parser')

def main():
        #print(web) #should be ~[200]~
        #print(content)
        title_and_description = defaultdict()
        #print(title_and_description)
        items = content.find_all("div", class_='title')
        #print(items[1])

        for i in items:
                encoded_string = i.encode('utf-8').decode('utf-8')
                clean_string = encoded_string.replace('<div class="title">','')\
                                                     .replace('</div>','')\
                                                             .strip()

                #print(clean_string)
                unfiltered_list = clean_string.split('\n')
                title_and_description[unfiltered_list[0]] = "SoT"
                #print(unfiltered_list)
                title_and_description[unfiltered_list[0]] = unfiltered_list[2].strip() if len(unfiltered_list) == 3 else ''
        write_csv(title_and_description)

def write_csv(input: dict):
        with open('result.csv','w',newline='') as f:
                writer = csv.writer(f)
                for key,value in input.items():
                        writer.writerow([key,value])

if __name__ == '__main__':
    main()

