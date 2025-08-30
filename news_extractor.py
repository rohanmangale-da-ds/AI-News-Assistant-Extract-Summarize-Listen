from bs4 import BeautifulSoup
import requests
import json
import winsound
import time 
start = time.time()
def extractor():
    """
    This function extracts news data from the Times of India website.
    It retrieves the headline and body of each news article and saves it to a JSON file.
    It returns total time taken for the extraction process.
    """
    # 1. Define the URL of the Times of India homepage
    toi_link = "https://timesofindia.indiatimes.com/"

    response = requests.get(toi_link)
    #The .raise_for_status() method checks if the request was successful (status code 200).
    response.raise_for_status() 

    # 3. Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')


    news_containers = soup.find_all(class_='col_l_6')
    all_news_data = []
    for container in news_containers:
        # Find the link tag (<a>) within the container
        link_tag = container.find('a', href=True)
        
        # Find the figcaption tag which holds the headline text
        headline_tag = container.find('figcaption')
        
        if link_tag and headline_tag:
            # Get the full URL from the 'href' attribute
            full_article_url = link_tag['href']

            # Get the headline text from the figcaption tag
            headline_text = headline_tag.text.strip()
            
            # get the news data
            try:
                response1 = requests.get(full_article_url)
                response1.raise_for_status() 
                soup1 = BeautifulSoup(response1.text, 'html.parser')
                news_data = soup1.find(class_ = '_s30J clearfix')
                news_data_striped = news_data.text.strip()
                print(f"Headline: {headline_text}")
                print(f"News: {news_data_striped}")
                print("-"*156)
                article_dict = {
                                "headline": headline_text,
                                "body": news_data_striped
                                                            }
                # Append the dictionary to your list
                all_news_data.append(article_dict)

            except:
                pass

    with open('news_data.json', 'w', encoding='utf-8') as f:
            # Use json.dump() to write the entire list
            json.dump(all_news_data, f, indent=4, ensure_ascii=False)
    print("All data has been saved to news_data.json")
    end = time.time()
    total_time = end - start
    winsound.Beep(1000, 500)
    print(f"Total time taken: {total_time} seconds")
    return total_time

if __name__ == "__main__":
    extractor()
