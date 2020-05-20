import requests
import bs4
import re


# This programm takes all movies from IMDB (first 200) and prints their title, genre and rating to console

def extraction_from_link( link):
    counter = 1
    headers = {'Accept-Language': 'en-US,en;q=0.8'}
    res = requests.get(link, headers=headers)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    f = open("C:\MyBrain\DM\Project\movie_titles.txt","a")

    for foo in soup.find_all('div', attrs={'class': 'lister-item-content'}):
        movie_title = foo.find('a', attrs={'href': re.compile("/title/")}).text
        # print(movie_title.text)
        genre = foo.find('span', attrs={'class': re.compile("genre")}).text
        # rating = foo.find('div', attrs={'class': "inline-block ratings-imdb-rating"}).attrs['data-value']
        rating = foo.find('span', attrs={'class': re.compile("ipl-rating-star__rating")}).text
        print(f"{movie_title}  {genre}  {rating}")
        f.write(movie_title + '\n')
        list_of_movies.append(movie_title)
        counter = counter + 1



if __name__ == "__main__":
    list_of_movies = []
    # extraction_from_link( "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating")
    # extraction_from_link(
    #     "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
    # extraction_from_link(
    #     "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")
    # extraction_from_link(
    #     "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt")
    # extraction_from_link(
    #     "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt")

    extraction_from_link(
        "https://www.imdb.com/list/ls005750764/?sort=list_order,asc&st_dt=&mode=detail&page=2")

    # print(list_of_movies)
    # for elem in list_of_movies:
    #     print(elem)
