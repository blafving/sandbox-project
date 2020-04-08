import requests

def pageget(url, dict_p):
    """
    Uses requests to fetch the page with parameters in dict_p, returning the text
    """
    resp = requests.get(url, params = dict_p)
    print(resp.url)
    print(resp.text[:200])
    return

    tbm=isch&q=%22violins+and+guitars%22

JEFIT = 'https://www.jefit.com/members/user-logs/log'

params = {'xid':'6490478', 'dd':'2020-04-06'}



"""
JEFIT Integration
What we need
1. Model attributes to handle jefit id
2. Data model for workouts
3. Function for importing a single date from jefit
4. Function for importing a date range from jefit
5. properties that calculate and track strength ratings based on jefit data 
6. Strength page/app/section
7. Plan for the interface
sweep across all dates
