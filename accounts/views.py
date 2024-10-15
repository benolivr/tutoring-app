from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
    if request.method == 'POST':
        form = TutoringHourForm(request.POST)
        if form.is_valid():
            tutoring_hour = form.save(commit=False)
            tutoring_hour.user = request.user
            tutoring_hour.save()
            return redirect('home')
    else:
        form = TutoringHourForm()
    return render(request, 'add_hours.html', {'form': form})

def ta_detail(request, pk):
    ta = CustomUser.objects.get(pk=pk)
    return render(request, 'ta_detail.html', {'ta': ta})


@method_decorator(login_required, name='dispatch')
class UpdateClassesView(UpdateView):
    model = CustomUser
    form_class = UpdateClassesForm
    template_name = 'update_classes.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
