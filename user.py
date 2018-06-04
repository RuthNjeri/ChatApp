import datetime


class User:
    users = []
    comments = []

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.role = 'Normal'
        self.save_user()

    def save_user(self):
        userinfo = {'username': self.username, 'password': self.password}
        User.users.append(userinfo)

    def create_comment(self, comment):
        user_comment = {
            'id': len(User.comments) + 1,
            'author': self.username,
            'comment': comment,
            'time_created': datetime.datetime.now()
        }
        User.comments.append(user_comment)

    def edit_comment(self, id, comment):
        edit_comment = [
            comment for comments in User.comments if comments['id'] == id
        ]
        edit_comment[0]['comment'] = comment
        User.comments.append(edit_comment)

    def delete_comment(self, id):
        delete_comment = [
            comment for comment in User.comments if comments['id'] == id
        ]
        User.comments.remove(delete_comment[0])
