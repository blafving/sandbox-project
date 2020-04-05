from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Nutrient, User, Day
from .forms import UserForm
import myfitnesspal
import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

def home(request):
    user_list = User.objects.all()
    print(user_list)
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
    days = Day.objects.filter(user=username).order_by('date')
    ### Graphing
    x = range(len(days))
    y = [day.cal_balance for day in days]
    plot = figure(
        title='Check it', 
        x_axis_label='Time', 
        y_axis_label='Calorie balance', 
        plot_width=800, 
        plot_height=800
        )
    plot.line(x, y, line_width=2)
    script, div = components(plot)
    days.reverse()
    context = {
        'days': days,
        'script': script,
        'div': div
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
