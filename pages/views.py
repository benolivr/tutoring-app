from django.views.generic import TemplateView
from .models import TutoringHour
import datetime

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hours = TutoringHour.objects.all()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        times = [datetime.time(hour).strftime("%I:%M %p").lstrip('0') for hour in range(7, 21)]
        schedule = {day: {time: [] for time in times} for day in days}

        for hour in hours:
            time_str = hour.hour.strftime("%I:%M %p").lstrip('0')
            if time_str in schedule[hour.day]:
                schedule[hour.day][time_str].append(hour.user)

        context['schedule'] = schedule
        return context