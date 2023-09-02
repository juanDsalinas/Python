from app import app
from app import engine, Base

with app.app_context():
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()


if __name__ == '__main__':
    app.run(port=8000,debug=True)