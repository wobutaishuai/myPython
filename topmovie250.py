import codecs
import requests
from bs4 import BeautifulSoup
DOWNLOAD_URL = 'http://movie.douban.com/top250/'
def download_page(url):
    return requests.get(url,headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0' }).content
def parse_html(html):
    soup=BeautifulSoup(html)
    movie_list_soup=soup.find('ol',attrs={'class':'grid_view'})
    movie_lsit_name=[]
    for movie_li in movie_list_soup.find_all("li"):
        detail=movie_li.find('div',attr={'class':'hd'})
        movie_name=detail.find('span',attr={'class':'title'}).getText()
        movie_lsit_name.append(movie_name)
    next_page=soup.find('span',attrs={'class':'next'}).find('a')
    if next_page:
        return movie_lsit_name,DOWNLOAD_URL+next_page['href']
    return movie_lsit_name,None
def main():
    url=DOWNLOAD_URL
    with codecs.open('miove.txt','wb',encoding='utf-8') as fp:
        while url:
            html=download_page(url)
            movies,url=parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
if __name__ == '__main__':
    main()