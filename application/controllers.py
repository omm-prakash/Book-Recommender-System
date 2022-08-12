from crypt import methods
from flask import request
from flask import render_template
from flask import current_app as app
import pickle
import numpy as np

popular_df = pickle.load(open('pickle/popular.pkl','rb'))
pt = pickle.load(open('pickle/pt.pkl','rb'))   
books = pickle.load(open('pickle/books.pkl','rb'))
similarity_data = pickle.load(open('pickle/similarity_data.pkl','rb'))


def book_details(name):
    book_data = books.drop('ISBN',axis=1).drop_duplicates('Book-Title')
    book_data = book_data[book_data['Book-Title']==name]
    return book_data.values.tolist()[0]
    # Book-Title, Book-Author, Year-Of-Publication, Publisher, Image-URL-L

def recommend_book(name):
    try:
        books=similarity_data[name]
        similar_items=sorted(enumerate(books), key=lambda x:x[1], reverse=True)[1:9]

        details=[]
        for item in similar_items:
            title=pt.index[item[0]]
            details.append(book_details(title))
            # details.append(title)

        return details

    except KeyError:
        return False

popular_df=popular_df.head(100)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/trending")
def trending():
    image=list(popular_df["Image-URL-L"].values)
    title=list(popular_df["Book-Title"].values)
    author=list(popular_df["Book-Author"].values)
    rating=list(popular_df["Avg-Book-Rating"].values)
    publication=list(popular_df["Publisher"].values)

    return render_template(
                            'trending.html',
                            image=image,
                            title=title,
                            author=author,
                            rating=rating,
                            publication=publication
                        )

@app.route("/recommend", methods=["GET","POST"])
def recommend():
    if request.method == 'POST':
        title = request.form['title']
        if recommend_book(title):
            books=recommend_book(title)
            return render_template('recommend.html', 
                                    books=books,
                                    title=title
                                    )
        else:
            return render_template('recommend.html', 
                                    title=title,
                                    show=True, 
                                    alert_color='alert-danger',
                                    alert_condition='Not Found',
                                    alert_message='Please enter a valid book name.')            
    return render_template('recommend.html')

@app.route("/find_book/<string:title>")
def find_book(title):
    if recommend_book(title):
        books=recommend_book(title)
        return render_template('recommend.html', 
                                books=books,
                                title=title
                                )
    else:
        return render_template('recommend.html', 
                                title=title,
                                show=True, 
                                alert_color='alert-danger',
                                alert_condition='Not Found',
                                alert_message='Please enter a valid book name.')            
