from unittest import result
from bs4 import BeautifulSoup
import requests

def yts_search(movie_name):
    url = f"https://yts.am/browse-movies/{movie_name}"
    r = requests.get(url).text 
    soup = BeautifulSoup(r, 'html.parser')
    
    image_div = soup.find_all('a', {"class":"browse-movie-link"})
    image_list = [image_div[i].find("img")['src'] for i in range(len(image_div))]
    
    title_div = soup.find_all('a', {"class":"browse-movie-title"})
    title_list = [title_div[i].text for i in range(len(title_div))]

    movie_urls = [i['href'] for i in title_div]
    magnet_dict = {
            'title' : [],
            'image_url' : [],
            'resolution' : [],
            'quality' : [],
            'size' : [],
            'magnet_link' : [],
        }
    for i in range(len(movie_urls)):
        r = requests.get(movie_urls[i]).text
        soup = BeautifulSoup(r, 'html.parser')
        torrents = soup.find_all('div', {'class':'modal-torrent'})
        
        for torrent in torrents:
            magnet_dict['title'].append(title_list[i])
            magnet_dict['image_url'].append(image_list[i])
            magnet_dict['resolution'].append(torrent.find('div',{'class':'modal-quality'}).span.text)
            magnet_dict['quality'].append(torrent.find_all('p', {'class':'quality-size'})[0].text)
            magnet_dict['size'].append(torrent.find_all('p', {'class':'quality-size'})[1].text)
            magnet_dict['magnet_link'].append(torrent.find('a', {'class':'magnet-download'})['href'])    
    
    results = []
    for i in range(len(magnet_dict['title'])):
        results.append({
            'title' : magnet_dict['title'][i],
            'image_url' : magnet_dict['image_url'][i],
            'resolution' : magnet_dict['resolution'][i],
            'quality' : magnet_dict['quality'][i],
            'size' : magnet_dict['size'][i],
            'magnet_link' : magnet_dict['magnet_link'][i],
        })

    return results

def eztv_search(show_name):
    BASE_URL = "https://eztv.re"
    url = f"{BASE_URL}/search/{show_name}"
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    rows = soup.find_all('tr', {'name':'hover'})
    results = [{'title': i.find_all('a')[1].text,
                'magnet_link' : i.find_all('a')[2]['href'],
                'size' : i.find_all('td')[3].text,
                'seeds' : i.find_all('td')[5].text} for i in rows]
    return results
    

