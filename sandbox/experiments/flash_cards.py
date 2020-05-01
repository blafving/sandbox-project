import requests
from bs4 import BeautifulSoup
from random import randrange
from time import sleep

def pageget(url, dict_p=[]):
    """
    Uses requests to fetch the page with parameters in dict_p, returning the text
    """
    resp = requests.get(url, params = dict_p)
    print('From {}'.format(resp.url))
    return

exceptions_page = 'https://docs.python.org/3/library/exceptions.html'
def create_dict(page):
    """
    Takes the python documentation page on exceptions and creates a dictionary
    with exception classes and values of their definitions.
    """
    cards = {}
    exc_got = requests.get(exceptions_page)
    # print(exc_got.text)
    exc_soup = BeautifulSoup(exc_got.text, features='html.parser')
    exceptions_html = exc_soup.find_all('dl')
    cards = {(object.attrs['class'][0], 
        object.dt.attrs['id']): [string for string in object.dd.p.stripped_strings] for object in exceptions_html if object.dd.p}
    return cards    

exc_dict = create_dict(exceptions_page)
def list_front(cards_dict):
    """
    Returns a list of keys
    """
    return [front for front in cards_dict.keys()]



def pick_random(cards_list):
    """
    Picks a random front card from the list
    """
    return cards_list[randrange(0, len(cards_list))]

picked = pick_random(list_front(exc_dict))
print(picked)
sleep(10)
print(exc_dict[picked])

def compile(cards):
    """
    Takes a dictionary and turns it into a nice 
    """

def soup_to_file(filename, soup_obj):
    """
    Takes a Beautiful Soup object soup_obj and writes to file: 'filename'
    """
    with open(filename, 'w') as openfile:
        for line in soup_obj:
            openfile.write(line)
            openfile.write('\n')

