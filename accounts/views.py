from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import datetime

from .forms import CustomUserCreationForm, TutoringHourForm, UpdateClassesForm
from .models import CustomUser, TutoringHour


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


from django.views.generic import TemplateView
from .models import TutoringHour

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hours = TutoringHour.objects.all()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        times = [f"{hour:02d}:00" for hour in range(7, 21)]
        schedule = {day: {time: [] for time in times} for day in days}

        for hour in hours:
            time_str = hour.hour.strftime("%H:%M")
            if time_str in schedule[hour.day]:
                schedule[hour.day][time_str].append(hour.user)

        context['schedule'] = schedule
        return context

@login_required
def add_hours(request):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    times = [time.strftime("%I:%M %p").lstrip('0') for time in [datetime.time(hour) for hour in range(7, 21)]]
    schedule = {day: [] for day in days}

    if request.method == 'POST':
        TutoringHour.objects.filter(user=request.user).delete()
        availability = request.POST.getlist('availability')
        for slot in availability:
            day, time_str = slot.split('_')
            hour = datetime.datetime.strptime(time_str, "%I:%M %p").time()
            TutoringHour.objects.create(user=request.user, day=day, hour=hour)
        return redirect('home')
    else:
        existing_hours = TutoringHour.objects.filter(user=request.user)
        for hour in existing_hours:
            time_str = hour.hour.strftime("%I:%M %p").lstrip('0')
            schedule[hour.day].append(time_str)

    context = {
        'days': days,
        'times': times,
        'schedule': schedule,
    }
    return render(request, 'add_hours.html', context)

def ta_detail(request, pk):
    ta = CustomUser.objects.get(pk=pk)
    classes = ta.tutoring_classes.all().order_by('cSCI_Alphanumeric')
    return render(request, 'ta_detail.html', {'ta': ta, 'classes': classes})


@method_decorator(login_required, name='dispatch')
class UpdateClassesView(UpdateView):
    model = CustomUser
    form_class = UpdateClassesForm
    template_name = 'update_classes.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

@login_required
def test_view(request):
    users = CustomUser.objects.all()
    user_data = []

    for user in users:
        tutoring_hours = TutoringHour.objects.filter(user=user)
        user_data.append({
            'user': user,
            'tutoring_hours': tutoring_hours,
        })

    context = {
        'user_data': user_data,
    }
    return render(request, 'test.html', context)
