import requests
from bs4 import BeautifulSoup

def get_headlines(url):
    
    response = requests.get(url)
    
    if response.status_code == 200:
       
        soup = BeautifulSoup(response.text, 'html.parser')
        
       
        title = soup.title.string if soup.title else 'No title found'
        
       
        headers = {}
        
        
        for i in range(1,4):
            header_tag = f'h{i}'
            headers[header_tag] = [header.get_text(strip=True) for header in soup.find_all(header_tag)]
        
       
        print(f"Page Title: {title}")
        for header, texts in headers.items():
            if texts:
                print(f"\n{header.upper()} Headers:")
                for text in texts:
                    print(f"- {text}")
        
       
        def ask_them(search_word):
            news = str(headers) + " " + title 
            if search_word.lower() in news.lower():  
                print("Yes, it's there in the news")
            else:
                print("The given word is not there in the news")
        
       
        code = str(input("Enter the word you want to search for in the news: "))
       
        ask_them(code)
    
    else:
        print(f"Error: Unable to fetch the URL. Status code: {response.status_code}")



news_url = str(input('Paste the URL of the news channel from which you want to know the main news: '))  
get_headlines(news_url)
