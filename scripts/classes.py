class Course:
    def __init__(self, title, link, trip_date, registration_open_date, registration_close_date, branch):
        self.title = title
        self.link = link
        self.trip_date = trip_date
        self.registration_open_date = registration_open_date
        self.registration_close_date = registration_close_date
        self.branch = branch


class User:
    def __init__(self, email, list_of_keywords):
        self.email = email
        self.keyword_list = list_of_keywords

