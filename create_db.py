from app import app
from models import User, db


with app.app_context():
    # Create the database and tables
    db.create_all()

    # Add some sample data
    if not User.query.first():
        users = [
            User(name='Alice'),
            User(name='Bob'),
            User(name='Charlie')
        ]
        db.session.add_all(users)
        db.session.commit()

    print("Database initialized with sample users.")
