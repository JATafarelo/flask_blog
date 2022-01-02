from main import db
from main.models import User,Post

# db.create_all()

# user_1 = User(username='admin',email='admin@admin.com',password = 'password')
# db.session.add(user_1)
# user_2 = User(username='joao',email='jatafarelo@hotmail.com',password = '123456')
# db.session.add(user_2)
# db.session.commit()

User.query.all()

user = User.query.first()

user.password
