import datetime
import requests, os, pprint
from bs4 import BeautifulSoup

os.system("cls" if os.name == "nt" else "clear")

req = requests.get('https://jmonline.com.br/')
req_JU = requests.get('https://jornaldeuberaba.com.br/')
soup = BeautifulSoup(req.text, 'html.parser')
soup_JU = BeautifulSoup(req_JU.text, 'html.parser')

title_JM = soup.select('h3')
title_JU = soup_JU.select('span[style="color: #fa8500;"]')

def sorted_news(hn):
    hn_sorted = sorted(hn, key=lambda k: k['title'], reverse=False)
    for idx, news in enumerate(hn_sorted):
        print(f"{idx + 1} - {news['title']}")
    return hn_sorted
    
    


def create_custom_hn(title):
    hn=[]
    date_today = datetime.date.today().strftime("%d/%m/%Y")
    print(f"{'-' * 50} Data: {date_today}\n")
    print("Jornal da Manhã\n")
    for idx, item in enumerate(title):
        # newsline = item.find_next('p').getText()  # Assuming the newsline is in a <p> tag after the <h3>
        title = item.getText()
        hn.append({'title': title})
        if idx > 10:
            break
        print(f"{idx + 1} - {title}")
    print(f"\nTotal de notícias: {len(hn)}")

def create_custom_hn2(title):
    hn=[]
    print("\nJornal de Uberaba\n")
    for idx, item in enumerate(title):
        # Removed unused variable "newsline"
        title = item.getText()  # Extracting the 'alt' attribute directly
        if len(title) > 20:
            
            hn.append({'title': title})
            if idx > 5:
                break
            print(f"{idx + 1} - {title}")
    print(f"\nTotal de notícias: {len(hn)}")
    
        
create_custom_hn(title_JM)

create_custom_hn2(title_JU)

