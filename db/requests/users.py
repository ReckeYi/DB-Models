from db.engine import session
from db.models.users import User

class UserRequests:

    # GET USERS DATA

    def get_all_users(self):
        users = session.query(
            User
        ).order_by(
            User.id
        ).all()
        return users

    def get_users_by_role(self, role):
        users = session.query(
            User
        ).filter(
            User.role == role
        ).order_by(
            User.id
        ).all()
        return users

    def get_user_by_email(self, email):
        users = session.query(
            User
        ).filter(
            User.email == email
        ).order_by(
            User.id
        ).first()
        return users

    def get_users_by_username(self, username):
        users = session.query(
            User
        ).filter(
            User.username == username
        ).first()
        return users

    def get_user_by_id(self, user_id):
        users = session.query(
            User
        ).filter(
            User.id == user_id
        ).first()
        return users

    # ADD USER

    def add_user(self, username, email, role):
        users = User(
            username=username,
            email=email,
            role=role
        )
        session.add(users)
        session.commit()

    # DELETE USER

    def del_user_by_id(self, user_id):
        user = session.query(
            User
        ).filter(
            User.id == user_id
        ).first()
        session.delete(user)
        session.commit()

    def del_user_by_name(self, username):
        user = session.query(
            User
        ).filter(
            User.username == username
        ).first()
        session.delete(user)
        session.commit()

    def del_user_by_email(self, email):
        user = session.query(
            User
        ).filter(
            User.email == email
        ).first()
        session.delete(user)
        session.commit()

    # UPDATE USER

    def change_user_name(self, username, new_username):
        user = session.query(
            User
        ).filter(
            User.username == username
        ).first()
        user.username = new_username
        session.commit()

    def change_user_email(self, email, new_email):
        user = session.query(
            User
        ).filter(
            User.email == email
        ).first()
        user.email = new_email
        session.commit()

    def change_user_role_by_username(self, username, new_role):
        user = session.query(
            User
        ).filter(
            User.username == username
        ).first()
        user.role = new_role
        session.commit()

    def change_user_role_by_email(self, email, new_role):
        user = session.query(
            User
        ).filter(
            User.email == email
        ).first()
        user.role = new_role
        session.commit()


# user_request = UserRequests()
# print(user_request.get_all_users())
# user_request.add_user('admin', 'admin@admins.com', 'Admin')
# user_request.get_all_users()
