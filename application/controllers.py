from crypt import methods
from flask import request
from flask import render_template
from flask import current_app as app
import pickle
import numpy as np

##############################################################################################

popular_df = pickle.load(open('pickle/popular.pkl','rb')).reset_index().drop('index',axis=1)
pt = pickle.load(open('pickle/pt.pkl','rb'))   
books = pickle.load(open('pickle/books.pkl','rb'))
similarity_data = pickle.load(open('pickle/similarity_data.pkl','rb'))
###########################################################################

def book_details(name):
    book_data = books.drop('ISBN',axis=1).drop_duplicates('Book-Title')
    book_data = book_data[book_data['Book-Title']==name]
    return book_data.values.tolist()[0]
    # Book-Title, Book-Author, Year-Of-Publication, Publisher, Image-URL-L

def collaborative_filtering_book(name):
    try:
        books=similarity_data[name]
        similar_items=sorted(enumerate(books), key=lambda x:x[1], reverse=True)[1:9]

        details=[]
        for item in similar_items:
            title=pt.index[item[0]]
            details.append(book_details(title))

        return details

    except KeyError:
        return False

popular_df_copy=popular_df.copy()
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

book_title=popular_df['Book-Title'].head(1000).values.tolist()
@app.route("/collaborative_filtering", methods=["GET","POST"])
def collaborative_filtering():
    if request.method == 'POST':
        title = request.form['title']
        if collaborative_filtering_book(title):
            books=collaborative_filtering_book(title)
            return render_template('collaborative_filtering.html', 
                                    books=books,
                                    title=title,
                                    book_title=book_title
                                    )
        else:
            return render_template('collaborative_filtering.html', 
                                    title=title,
                                    show=True, 
                                    alert_color='alert-danger',
                                    alert_condition='Not Found',
                                    alert_message='Please enter a valid book name.',
                                    book_title=book_title)            
    return render_template('collaborative_filtering.html',book_title=book_title)

@app.route("/find_collaborative_filtering/<string:title>")
def find_book(title):
    if collaborative_filtering_book(title):
        books=collaborative_filtering_book(title)
        return render_template('collaborative_filtering.html', 
                                books=books,
                                title=title,
                                book_title=book_title
                                )
    else:
        return render_template('collaborative_filtering.html', 
                                title=title,
                                show=True, 
                                alert_color='alert-danger',
                                alert_condition='Not Found',
                                alert_message='Please enter a valid book name.',
                                book_title=book_title)            

##################################################################################################

new = pickle.load(open('pickle/new.pkl','rb'))
new_dataset = pickle.load(open('pickle/new_dataset.pkl','rb'))
similar = pickle.load(open('pickle/similar.pkl','rb'))
##############################################################

def suggest(book):
    try:
        index=new[new.title==book].index[0]
        recommend=similar[index]
        books=sorted(enumerate(recommend),key=lambda x: x[1],reverse=True)[1:9]
        book_details=[]
        for bk in books:
            bk_index=bk[0]
            book_details.append(new_dataset[['authors','image-url','title','url','description']].values.tolist()[bk_index])
        return book_details
    except:
        return False

books_titles=new.title.values.tolist()
books_titles.sort()
@app.route("/content_base", methods=["GET","POST"])
def content_base():
    if request.method == 'POST':
        title = request.form['title']
        if suggest(title):
            books=suggest(title)
            return render_template('content_base.html', 
                                    books=books,
                                    title=title,
                                    books_titles=books_titles
                                    )
        else:
            return render_template('content_base.html', 
                                    title=title,
                                    show=True, 
                                    alert_color='alert-danger',
                                    alert_condition='Not Found',
                                    alert_message='Please enter a valid book name.',
                                    books_titles=books_titles)            
    return render_template('content_base.html',books_titles=books_titles)

@app.route("/find_content_base/<string:title>")
def find_content_base(title):
    if suggest(title):
        books=suggest(title)
        return render_template('content_base.html', 
                                books=books,
                                title=title,
                                books_titles=books_titles
                                )
    else:
        return render_template('content_base.html', 
                                title=title,
                                show=True, 
                                alert_color='alert-danger',
                                alert_condition='Not Found',
                                alert_message='Please enter a valid book name.',
                                books_titles=books_titles)            


##########################################################################################
similarity_score = pickle.load(open('pickle/similarity_score.pkl','rb'))
##############################################################

def suggest_hybrid_filter(book):
  try:
    index=popular_df_copy[popular_df_copy['Book-Title']==book].index[0]
    books=similarity_score[index]
    books=sorted(enumerate(books),key=lambda x:x[1],reverse=True)[1:9]
    book_details=[]
    for bk in books:
        data=popular_df_copy.loc[bk[0],['Book-Title','Book-Author','Year-Of-Publication','Publisher','Image-URL-L','ISBN']].values
        book_details.append(data)
    return book_details
  except:
    return False
    
@app.route("/hybrid_recommender", methods=["GET","POST"])
def hybrid_recommender():
    if request.method == 'POST':
        title = request.form['title']
        if suggest_hybrid_filter(title):
            books=suggest_hybrid_filter(title)
            return render_template('hybrid.html', 
                                    books=books,
                                    title=title,
                                    book_title=book_title
                                    )
        else:
            return render_template('hybrid.html', 
                                    title=title,
                                    show=True, 
                                    alert_color='alert-danger',
                                    alert_condition='Not Found',
                                    alert_message='Please enter a valid book name.',
                                    book_title=book_title)  

    return render_template('hybrid.html',book_title=book_title)

@app.route("/find_hybrid_recommender/<string:title>")
def find_hybrid_recommender(title):
    if suggest_hybrid_filter(title):
        books=suggest_hybrid_filter(title)
        return render_template('hybrid.html', 
                                books=books,
                                title=title,
                                book_title=book_title
                                )
    else:
        return render_template('hybrid.html', 
                                title=title,
                                show=True, 
                                alert_color='alert-danger',
                                alert_condition='Not Found',
                                alert_message='Please enter a valid book name.',
                                book_title=book_title) 

@app.route('/contact')
def contact():
    return render_template('contact.html')           
