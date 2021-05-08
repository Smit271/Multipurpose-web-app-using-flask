from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from form import RegistrationForm, Weather, Movie, Synonym, Flickr_Form
from flask_sqlalchemy import SQLAlchemy
from Current_Weather_API import Weather_detail
from OMDB_Movies_search_API import Ratings
from datamuse_api import Synonyms
from advice import Advice_API
from flickr_api import Flickr


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
db = SQLAlchemy(app)


class Subscribers(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mail_id = db.Column(db.String(50), nullable=False)
    city_name = db.Column(db.String(50), nullable = False)

    def __repr__(self):
        return f"{self.name} with {self.mail_id} for {self.city_name}"


@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
    advice  = Advice_API()  
    details = advice.advice()
    return render_template('main.html', result = details)

"""
@app.route("/flickr", methods = ['GET', 'POST'])
def flickr():
    form  = Flickr_Form()  
    if request.method == 'POST':
        tag = request.form.get('tag')
        pages_url  = Flickr(str(tag))
        details = pages_url.get_photo()
        #name = details[0]
        #temp = details[2]
        #discription = details[1]
        return render_template('flickr.html', form = form , result = details)
    return render_template('flickr.html', form = form)
"""

@app.route("/weather_feed", methods = ['GET', 'POST'])
def weather_feed():
    form  = Weather()  
    if request.method == 'POST':
        city = request.form.get('city_name')
        weather = Weather_detail(str(city))
        details = weather.weather()
        #name = details[0]
        #temp = details[2]
        #discription = details[1]
        return render_template('weather.html', form = form , result = details)
    return render_template('weather.html', form = form)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    db.session.commit()

    if request.method == 'POST':
        name = request.form.get('name')
        mail_id = request.form.get('email')
        city_name = request.form.get('city')

        if city_name and mail_id:
            existing_user = Subscribers.query.filter(
                Subscribers.city_name == city_name or Subscribers.mail_id == mail_id
            ).first()
            if existing_user:
                flash(f'{mail_id} for  city {city_name}  already subscribed!', 'danger   ')
                return redirect(url_for('home'))
            new_user = Subscribers(
                name=name,
                mail_id=mail_id,
                city_name=city_name
            )  # Create an instance of the Subscribers class
            db.session.add(new_user)  # Adds new Subscribers record to database
            db.session.commit()  # Commits all changes
            redirect(url_for('home'))

            with open('subscribers.txt' , 'a') as f:
                f.write(f"{name}, {mail_id}, {city_name}\n")
            f.close()
        if form.validate_on_submit():
            flash(f'Subscribed for {form.name.data}!', 'success')
            return redirect(url_for('home'))

    return render_template('register.html', title = 'Register', form = form)


@app.route("/movie_ratings", methods = ['GET', 'POST'])
def movie_ratings():
    form = Movie()
    if request.method == 'POST':
        name = request.form.get('movie_name')
        ratings = Ratings(name).ratings()
        return render_template('movie_ratings.html', form = form , result = ratings)
    return render_template('movie_ratings.html', form = form)


@app.route("/synonyms", methods = ['GET', 'POST'])
def synonyms():
    form = Synonym()
    if request.method == 'POST':
        word = request.form.get('word')
        synonyms = Synonyms(word).rhyming_word()
        return render_template('synonyms.html', form = form , result = synonyms)
    return render_template('synonyms.html', form = form)


if __name__ == "__main__":
	db.create_all()
	app.run(port = 8080, debug = True)
