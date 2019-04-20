from datetime import datetime, timedelta
from calendar import HTMLCalendar
from mitgliederbereich.models import Event

# *************************************** Calendar ***************************************************************

class Calendar(HTMLCalendar):
    _weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td for Calendar
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul>{d}</ul></td>"
        return '<td></td>'

        # formats a week as a tr

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

        cal = f'<table class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal

    #********************************************* Mistplan *************************************************************

    def formatmonthMistplan(self, withyear=True):
        cal = f'<table class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += self.createMistplanHeader()
        for week in self.monthdays2calendar(self.year, self.month):
            for day, weekday in week:
                if (day != 0):
                    cal += f'<tr>'
                    cal += f'<td>{day} {self._weekdays[weekday]}</td>'
                    #cal += f'<td>{self._weekdays[weekday]}</td>'
                    cal += f'<td class="setName">{"name"}</td>'
                    cal += f'<td class="setName">{"name"}</td>'
                    cal += f'<td class="setName">{"name"}</td>'
                    cal += f'<td class="setName">{"name"}</td>'
                    cal += f'</tr>'
        return cal

    def createMistplanHeader(self):
        header = f'<tr>'
        header += f'<th></th>'
        header += f'<th>Stuten</th>'
        header += f'<th>Wallache</th>'
        header += f'<th>Ritter</th>'
        header += f'<th>Senioren</th>'
        header += f'</tr>'
        return header
