import classes
import csv

# Reads all user information from user data and returns a list of user objects
def read_user_data():
    list_of_users = []
    with open('/Users/jacksonhayward/PycharmProjects/Mountaineers-Trip-Notifications/data/users.csv', newline='') as user_file:
        user_reader = csv.reader(user_file, delimiter=' ')
        for row in user_reader:
            user = classes.User(row[0], row[1])
            list_of_users.append(user)
    return list_of_users





# Reads all current course information from data files and returns list of current courses