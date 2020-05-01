from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Nutrient, User, Day
from .forms import UserForm
import datetime
import pandas as pd
from bokeh.plotting import figure, output_file
from bokeh.embed import components

def home(request):
    user_list = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/user/')
    else:
        form = UserForm()
    context = {
        'form': form, 
        'user_list': user_list
    }
    return render(request, 'mydata\home.html', context)

def user(request, username):
    # Day objects for the given user
    record = get_object_or_404(User, pk=username)
    record.recent_import()
    days = Day.objects.filter(user=username).order_by('date').reverse()
    ### Graphing
    data = {}
    data['date'] = [day.date for day in days]
    data['y plot'] = [day.nutrient.cal_burned for day in days] # Sets attribute for analysis
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    plot = figure(
        title=record.name(), 
        x_axis_label='Time', 
        x_axis_type='datetime',
        y_axis_label='Calories burnt',  # Sets Name for y axis
        plot_width=800, 
        plot_height=400
        )
    plot.segment(
        x0=df['date'], 
        y0=[0 for day in days], 
        x1=df['date'],
        y1=df['y plot'],
        color='#00CC66', 
        line_width=4)
    script, div = components(plot)
    stats = record.snapshot() # User function 
    context = {
        'days': days,
        'script': script,
        'div': div,
        'stats': stats,
    }
    return render(request, r'mydata\user.html', context)


def import_myfitpal(request):
    """
    Not currently used for anything - all import functionality was baked into the models
    """
    if request.method == 'POST':
        form = MyfitdataForm(request.POST)
        if form.is_valid():
            daycounter = datetime.timedelta(days=1)
            user = User.objects.get(pk=form.data['user'])
            user.start_date = datetime.date.fromisoformat(form.data['start_date'])
            while import_date <= info[3]:
                try:
                    Nutrient.objects.get(
                        date=import_date, 
                        user_rec=User.objects.get(pk=info[1])
                    ).update()
                except DoesNotExist:
                    new = Nutrient.objects.create(
                        date=import_date, 
                        user=info[1],
                    )
                    new.update()
                finally:
                    import_date += info[0] 

            return HttpResponseRedirect('working/')
        else:
            return HttpResponseRedirect('notworking/')
    else:
        form = MyfitdataForm()
        return render(request, 'mydata\importmyfitpal.html', {'form': form})

def working(request):
    return render(request, 'mydata\working.html')

def notworking(request):
    return render(request, 'mydata\\notworking.html')
