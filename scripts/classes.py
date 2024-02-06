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


class User:
    def __init__(self, email, list_of_keywords):
        self.email = email
        self.keyword_list = list_of_keywords
