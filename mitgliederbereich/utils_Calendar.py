from datetime import datetime, timedelta
from calendar import HTMLCalendar
from datetime import date
from mitgliederbereich.models import Event

# *************************************** Calendar ***************************************************************

class Calendar(HTMLCalendar):
    _weekdays = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

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
                    cal += '<tr>'
                    cal += f'<td>{day} {self._weekdays[weekday]}</td>'
                    horse_power = 0;
                    while horse_power < 4:
                        cal += f'<td class="setName"><button type="button" \ onClick="nameMistplan(this, {horse_power})" \ value={date(self.year, self.month,day)} > {"name"}</button></td>'
                        horse_power += 1
                    cal += '</tr>'
        return cal

    def createMistplanHeader(self):
        header = '<tr>'
        header += '<th></th>'
        header += '<th>Stuten</th>'
        header += '<th>Wallache</th>'
        header += '<th>Ritter</th>'
        header += '<th>Senioren</th>'
        header += '</tr>'
        return header
