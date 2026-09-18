# Importación
from flask import Flask, render_template, request, redirect, session

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'my_top_secret_123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    user_email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Card {self.id}>'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST':

        form_login = request.form['email'].strip()
        form_password = request.form['password'].strip()
            

        user = User.query.filter_by(email=form_login).first()
        if user and user.password == form_password:
            session['user_email'] = user.email
            return redirect('/index')
        else:
            error = 'Nombre de usuario o contraseña incorrectos'
        
    return render_template('login.html', error=error)

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        

        user = User(email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return redirect('/')
    else:    
        return render_template('registration.html')


@app.route('/index')
def index():

    email = session.get('user_email')
    if not email:
        return redirect('/')
        
    cards = Card.query.filter_by(user_email=email).all()
    return render_template('index.html', cards=cards)


@app.route('/card/<int:id>')
def card(id):
    if not session.get('user_email'):
        return redirect('/')
        
    card_item = Card.query.get_or_404(id)
    return render_template('card.html', card=card_item)

@app.route('/create')
def create():
    if not session.get('user_email'):
        return redirect('/')
        
    return render_template('create_card.html')


@app.route('/form_create', methods=['GET', 'POST'])
def form_create():
    if not session.get('user_email'):
        return redirect('/')

    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        text = request.form['text']
        email = session["user_email"]

        card_item = Card(title=title, subtitle=subtitle, text=text, user_email=email)

        db.session.add(card_item)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')


@app.route('/logout')
def logout():
    session.pop('user_email', None)
    return redirect('/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
