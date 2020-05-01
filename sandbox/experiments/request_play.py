import requests
from bs4 import BeautifulSoup
import time

def pageget(url, dict_p):
    """
    Uses requests to fetch the page with parameters in dict_p, returning the text
    """
    resp = requests.get(url, params = dict_p)
    return resp.text

def get_date(date_str):
    """
    retrieves all activities and workouts logged on jefit for a given date
    """
    jefit = 'https://www.jefit.com/members/user-logs/log'
    params1 = {'xid':'6490478', 'dd':date_str}
    resp = requests.get(jefit, params = params1)
    soup = BeautifulSoup(resp.text, features='lxml')
    summaries = soup.find_all(class_='workout-session')
    activities = soup.find_all(class_='exercise-block')
    for activity in activities:
        data = activity.form
        
        print(data)
        print('--------------\n' * 4)
        time.sleep(2)

    data = []
    # for session in summaries:
    #     print(session)
        #     if obj.name == 'div':
        #        data.append(tag.string)
        # data.append('Next Session')
    return data


def is_session_length(tag):
    """
    Returns True if previous sibling of the parent contains string 'Session Length
    """
    return tag.parent.previous_sibling == '<div>Session Length</div>'

def get_summary(workout_soup):
    """
    Retrieves the workout summary info for a single session in a workout soup object
    """
    result = [tag for tag in workout_soup if tag.attrs['class'] == 'workout-session']
    return result

workouts = get_date('2020-04-16')
print(workouts)





# jefitf = open('jefitday.txt', 'wt')
# for line in soup:
#     jefitf.write(line)
#     jefitf.write('\n')
# jefitf.close()

"""
Build a function to analyze one of these exercise blocks and store key values as model attributes... maybe even create new exercise models
Build this into the block_import and update functions 
Write functions to 

analyze performance, store max values 

<div class="exercise-block">
<div class="log-input-layout" style="border: solid 1px #dddddd; border-radius: 10px; position: absolute; width: 555px; z-index: 999; background-color: #ffffff; display: none;">
<div style="text-align: center; font-weight: bold; color: #4d4d4d;">Dumbbell One Leg Squat</div>
<div style="padding: 10px;">
<div style="display: inline-block; width: 40%;"> <img height="150" src="../../../images/exercises/800_600/4848.jpg" width="200"/> </div><div style="display: inline-block; width: 60%; vertical-align: top;">
<form>
<input name="logid" type="hidden" value="560"/>
<input name="exerciseid" type="hidden" value="1212"/>
<input name="belongsys" type="hidden" value="1"/>
<input name="ename" type="hidden" value="Dumbbell One Leg Squat"/>
<input name="recordtype" type="hidden" value="0"/>
<input name="date" type="hidden" value="2020-04-06"/>
<div style="display: inline-block;">
<ul class="logsetlist"> <li style="margin-bottom: 5px;"><span>Set 1 : </span>
<input class="inputlog decimal" maxlength="6" name="weight" size="3" type="text" value="190"/> lbs                            <input class="inputlog" maxlength="6" name="rep" size="3" type="text" value="15"/> Reps
                        </li> <li style="margin-bottom: 5px;"><span>Set 2 : </span>
<input class="inputlog decimal" maxlength="6" name="weight" size="3" type="text" value="190"/> lbs                            <input class="inputlog" maxlength="6" name="rep" size="3" type="text" value="15"/> Reps
                        </li> <li style="margin-bottom: 5px;"><span>Set 3 : </span>
<input class="inputlog decimal" maxlength="6" name="weight" size="3" type="text" value="190"/> lbs                            <input class="inputlog" maxlength="6" name="rep" size="3" type="text" value="15"/> Reps
                        </li> <li style="margin-bottom: 5px;"><span>Set 4 : </span>
<input class="inputlog decimal" maxlength="6" name="weight" size="3" type="text" value="190"/> lbs                            <input class="inputlog" maxlength="6" name="rep" size="3" type="text" value="15"/> Reps
                        </li> <li style="margin-bottom: 5px;"><span>Set 5 : </span>
<input class="inputlog decimal" maxlength="6" name="weight" size="3" type="text" value="190"/> lbs                            <input class="inputlog" maxlength="6" name="rep" size="3" type="text" value="15"/> Reps
                        </li> <li style="margin-bottom: 5px;"><span>Set 6 : </span>
<input class="inputlog decimal" maxlength="6" name="weight" size="3" type="text" value="190"/> lbs                            <input class="inputlog" maxlength="6" name="rep" size="3" type="text" value="15"/> Reps
                        </li> </ul>
<div style="display: block; text-align: center; margin-top: 15px; ">
<button class="update-log-button" type="button">Update Log</button>
</div>
</div> <div style="display: inline-block; vertical-align: top; margin-left: 10px;">
<div class="plus-minus-set plus" style="vertical-align: top;">+
                </div>
<div class="plus-minus-set minus" style="vertical-align: top; margin-top: 15px;">−
                </div>
</div> </form>
</div>
</div>
</div>
"""
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
"""