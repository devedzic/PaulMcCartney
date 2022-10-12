"""Web crawling and scraping.
BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

import requests
from bs4 import BeautifulSoup

from util import utility
from settings import *


BASE_URL = 'https://www.imdb.com/'
# Start from https://www.imdb.com, type anything in the Search box, and in the result find Advanced Search.
# Click Keyword, and in Enter a keyword insert Paul McCartney. Select reference-to-paul-mccartney.

# Other candidates:
# https://ultimateclassicrock.com/search/?s=paul%20mccartney
# https://ultimateclassicrock.com/search/?s=albums
# https://www.rockarchive.com/artists?page=1
# https://digitaldreamdoor.com/pages/bg_hits/bg_hits_61.html
# https://www.paulmccartney.com/discography/albums/all
# https://rock-bands.com/
# https://rateyourmusic.com/charts/top/album/1960s/             # blocks IP address!


def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed (allow_redirects=False)
    response = requests.get(url, allow_redirects=False)

    # Get text from the Response object, using <response>.text
    response_text = response.text

    # Create and return the corresponding BeautifulSoup object from the response text; use features='html.parser'
    return BeautifulSoup(response_text, features='html.parser')


def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """


def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    Essentially, get_next_soup() just returns get_soup(get_specific_page(start_url, page)),
    i.e. converts the result of the call to get_specific_page(start_url, page), which is a string,
    into a BeautifulSoup object.
    """


def crawl(url: str, max_pages=1):
    """Web crawler that collects info about movies from IMDb,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup()) from multi-page movie lists.
    Parameters: the url of the starting IMDb page and the max number of pages to crawl in case of multi-page lists.
    """


def get_4_digit_substring(a_string):
    """Returns the first 4-digit substring from a_string.
    It assumes that a_string contains a 4-digit substring representing a year.
    Useful when the year of a movie release on IMDb is represented like '(1988, part 2)', or '(video, 2002)'."""


def get_m_info(start_url: str, max_pages=1):
    """
    Returns structured information about movies from a multi-page IMDb movie list.
    :param start_url: the url of the starting page of a multi-page IMDb movie list
    :param max_pages: the max number of pages to crawl
    :return: a list of tuples of info-items about the movies from a multi-page IMDb movie list
    Creates and uses the following data:
    - h3_list - a list of all 'h3' tags from multiple IMDb pages
                (each 'h3' tag contains: movie title, year of release, and (relative) link to the movie's IMDb page)
    - poster_list - a list of all relevant 'div' tags from multiple IMDb pages
                    (each such a 'div' tag contains the link to the poster of the corresponding movie)
    - info_list - a list of 3-tuples of information about each movie from h3_list ((title, year, link) tuples)
    - poster_link_list - a list of links to the posters of the movies from poster_list
    - complete_list - a list of 4-tuples of information about each movie from info_list and poster_list
    """

    # Initialize h3_list and poster_list as empty lists, as well as the generator object (crawl(start_url, max_pages))

    # In a while True loop, get the next soup from the generator and use it to populate h3_list and poster_list
    # by extending them with the relevant tags from the soup
    # (find all 'h3' tags and 'div' tags that contain class="lister-item-image ribbonize" attribute)

    # Initialize info_list as an empty list.
    # Repeat the following steps for each h3 in a for loop over h3_list:
    # Extract title from h3.a.text (strip() it in order to eliminate leading/trailing whitespace).
    # Extract year from <span class="lister-item-year text-muted unbold"> using h3.find(...).text,
    # and filter it by get_4_digit_substring(year); set year to 'unknown' if get_4_digit_substring(year) returns None.
    # Extract relative link from h3.a['href'] (make sure to lstrip('/') from it as well) and append it to BASE_URL.
    # Append (title, year, link) to info_list.

    # Initialize poster_link_list as an empty list.
    # In a for loop over all posters in poster_list, extract the poster link from poster.a.img['loadlate']
    # and append it to poster_link_list.
    # Note that extraction from poster.a.img['src'] does not work. Check the saved HTML code (soup) of the entire page.

    # Initialize complete_list as an empty list.
    # In a for loop over zip(info_list, poster_link_list) extract (title, year, link, poster_link) tuples and
    # append them to complete_list.
    # Return complete_list.


if __name__ == "__main__":

    # Getting started
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key' \
    #             '&sort=moviemeter,asc&mode=detail&page=1'
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=reference-to-paul-mccartney&ref_=kw_nxt&' \
    #             'sort=moviemeter,asc&mode=detail&page=1'
    start_url = 'https://ultimateclassicrock.com/search/?s=paul%20mccartney'

    # # Create Response object from GET request, using requests.get(<url>, allow_redirects=False)
    # response = requests.get(start_url, allow_redirects=False)
    # print(type(response))
    # print(response)
    # print()

    # # Get response text from Response object, using <response>.text
    # response_text = response.text
    # print(response_text[:4000])
    # print()

    # Get BeautifulSoup object from response text, using BeautifulSoup(<response text>, features='html.parser')
    soup = get_soup(start_url)
    # print(type(soup))
    # print(str(soup))
    # print()

    # Save BeautifulSoup object to an HTML file,
    # using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace')
    soup_file = DATA_DIR / 'soup.html'
    soup_file.write_text(str(soup), encoding='utf-8', errors='replace')
    print()

    # Demonstrate <BeautifulSoup object>.find('<tag>'), <BeautifulSoup object>.find_all(<tag>),
    # <BeautifulSoup object>.find_all(<tag>, {'<tag_attr_name>': "<tag_attr_value>"});
    # use, e.g., 'h3' or 'div' as the tags in the examples (e.g., <div class="lister-item-image ribbonize">)
    # h3_first = soup.find('h3')
    # print(type(h3_first))
    # print()
    # print(h3_first)

    # h3_first = soup.find('h3', {'class': "lister-item-header"})
    # print(type(h3_first))
    # print()
    # print(h3_first)

    # movie_items = soup.find_all('div', {'class': "lister-item mode-detail"})
    # print(movie_items)
    # print()

    # span_first = soup.find('article')
    # print(span_first)
    # print()
    # print(type(span_first))
    # print()
    # a_first = soup.find('article').find('a').text
    # print(a_first)
    # print()

    articles = soup.findAll('article')
    print(len(articles))
    print()
    for article in articles:
        # image = article.findNext('a').find('figcaption').text
        # image = article.findNext('a').text
        # print(image)
        div_image = article.findNext('div', {'class': 'article-image-wrapper'})
        div_content = article.findNext('div', {'class': 'content'})

        featured_image_url = div_image.findNext('a').attrs['data-image']
        # print(featured_image_url)
        article_title = div_content.find('a').text
        # print(article_title)
        article_date = div_content.findNext('div', {'class': 'auth-date'}).findNext('time')
        print(article_date)



    # Demonstrate getting a 'subtag' for a tag (a bs4.element.Tag object), e.g. h3.find('<subtag>')
    print()

    # Demonstrate getting an attribute value for a tag (a bs4.element.Tag object),
    # e.g. h3.find('<subtag>'), filtered with <{'class': "<class name>"}>;
    # alternatively: h3.find('<tag>')['<attr>'], h3.find('<subtag>').get('<attribute>'),
    # h3.find('<subtag>').<attribute>,... (<attribute>: e.g. text)
    print()

    # Demonstrate <tag>.find_next_siblings() (returns all <tag>'s siblings) and
    # <tag>.find_next_sibling() (returns just the first one)
    print()

    # Each bs4.element.ResultSet, bs4.element.Tag,... can be used to create another BeautifulSoup object,
    # using BeautifulSoup(str(<bs4.element object>), features='html.parser')
    print()

    # Get/Return all text from a bs4.element.Tag object, using <bs4.element.Tag object>.text
    print()

    # Get/Return and remove a specific item from a bs4.element.ResultSet using <result set>.pop(<index>) (default: last)
    print()

    # Example: get all movie titles from an IMDb page
    print()

    # # Test get_soup()
    # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
    #             'mode=detail&page=1&sort=moviemeter,asc'
    print()

    # Test get_specific_page()
    print()

    # Test get_next_soup()
    print()

    # Test crawl()
    print()

    # Test get_4_digit_substring()
    print()

    # Test get_m_info()
    print()





    """
    HTML tags with examples:
    https://www.tutorialstonight.com/html-tags-list-with-examples.php
    
    start_url:
    https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&mode=detail&page=1&sort=moviemeter,asc

    Finding relevant tags:
    body/wrapper/root/pagecontent/content-2-wide/main/article/lister list detail sub-list/lister-list/lister-item mode-detail/
	    lister-item-image ribbonize/removable-wrapper/a
	    lister-item-content/<h3 class="lister-item-header">/
	        <a ...>
	        <span class="lister-item-year text-muted unbold">(2000)</span>
	"""
