from datetime import date, datetime
import time
class Course:
    def __init__(self, title, link, trip_date, registration_status, branch, difficulty):
        self.title = title
        self.link = link
        self.trip_date = trip_date
        self.registration_status = registration_status
        self.branch = branch
        self.difficulty = difficulty

    def __str__(self):
        return (f'Trip name:                {self.title}\n' +
                f'Trip date:                {self.trip_date}\n' +
                f'Trip registration status: {self.registration_status}\n' +
                f'Branch:                   {self.branch}\n' +
                f'Trip difficulty:          {self.difficulty}\n'
                f'Trip webpage:             {self.link}\n')


    # Determines if the course is open for registration, closed, opening within 10 days or opening later
    # returns an int for each status: 0 = 0pen, 1 = opening_soon, 2 = opening_later, 3 = closed
    def get_status(self):
        if "closes" in self.registration_status:
            return 0
        elif "closed" in self.registration_status:
            return 3
        else:
            today = datetime.today()

            registration = self.registration_status.split()
            day_month = registration[2] + " " + registration[3] + " " + str(today.year)
            trip_date_object = time.strptime(day_month, '%b %d %Y')
            trip_date = datetime.fromtimestamp(time.mktime(trip_date_object))
            delta = trip_date - today

            # if delta is less than 0, add 1 to year and repeat
            if delta.days < 0:
                day_month = registration[2] + " " + registration[3] + " " + str(today.year + 1)
                trip_date_object = time.strptime(day_month, '%b %d %Y')
                trip_date = datetime.fromtimestamp(time.mktime(trip_date_object))
                delta = trip_date - today

            if delta.days < 10:
                return 1
            else:
                return 2






class User:
    def __init__(self, email, set_of_keywords):
        self.email = email
        self.keyword_set = set_of_keywords

    def __str__(self):
        return (f'Email:            {self.email}\n'
                f'List of keywords: {self.keyword_set}')
