# Book-Recommender-System
Its is a project to recommend similar books to the client, using different techniques.

1. **Popularity Based** 
   - Rank based recommender, using review of reader with high book review frequency. 
2. **Collaborative Filtering**
   - Collaborative methods for recommender systems are methods that are based solely on the past interactions recorded between users and items in order to produce new recommendations. These interactions are stored in the so-called “user-item interactions matrix”.
   - Then, the main idea that rules collaborative methods is that these past user-item interactions are sufficient to detect similar users and/or similar items and make predictions based on these estimated proximities.
   ![image](https://miro.medium.com/max/770/1*m_Z6Da5FZ62KN2yH-x_GOQ@2x.png)
3. **Content Based Method**
   - Unlike collaborative methods that only rely on the user-item interactions, content based approaches use additional information about users and/or items.
   - The idea of content based methods is to try to build a model, based on the available “features”, that explain the observed user-item interactions. 
   ![image1](https://miro.medium.com/max/770/1*ReuY4yOoqKMatHNJupcM5A@2x.png)

4. **Hybrid Recommender**
   - The limitation of both content-based and collaborative methods, and they both address some limitations from the other, it is natural to consider combining these two methods together, which leads to the Hybrid method.

#### Cosine Similarity
![cosine_similarity](https://i2.wp.com/blog.knoldus.com/wp-content/uploads/2019/04/cos_similarity.jpg?w=810&ssl=1)
-  Book embedding vectors pointing in the same direction will receive high cosine similarity scores. The idea is that directions through the latent concept space capture the essence of books. 
  
#### My Approch
- I had two dataset from diffrent source i.e. [book-recommendation-dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset) and [book-depository-dataset](https://www.kaggle.com/datasets/sp1thas/book-depository-dataset).
- The first one have a good number of user review for the books, but didn't have description about those books.
- I made the content based filter using `book-depository-dataset` that show in the app as `Content Based` page.
- With `book-recommendation-dataset`, I have made all types of recommender system.
- As the `book-recommendation-dataset` didn't have description about books, I have extracted features, i.e. english keyswords from their `Book-Title` and publisher etc to make a content based recommender system. With description on the books the models could be improved.
- The `Hybrid Recommender` is a weighted sum of popularity rank, content similarity and collaborative filtering. With poor description data I gave less weight for `content based recommender`, while using the same for hybrid recommender.
- Visit [here](https://github.com/omm-prakash/Book-Recommender-System/tree/main/ipynb) to have a look on data processing.

# Local Setup
- Clone the project
- Run ` bash local_setup.sh`

# Local Development Run
- `bash local_run.sh` It will start the flask app in `development`. Suited for local development

# Replit run
- Go to shell and run
    `pip install --upgrade poetry`
- Click on `main.py` and click button run
- Sample project is at https://replit.com/@thejeshgn/flask-template-app
- The web app will be availabe at https://flask-template-app.thejeshgn.repl.co
- Format https://<replname>.<username>.repl.co

# Folder Structure

- `db_directory` has all the csv files regarding the books used in the project.
- `application` is where our application code is
- `local_setup.sh` set up the virtualenv inside a local `.env` folder. Uses `pyproject.toml` and `poetry` to setup the project
- `local_run.sh`  Used to run the flask application in development mode
- `static` - default `static` files folder. It serves at '/static' path. More about it is [here](https://flask.palletsprojects.com/en/2.0.x/tutorial/static/).
- `templates` - Default flask templates folder
- `pickle` - Holds binary files after processing in the `book-recommender.ipynb` file, used in the application
- `ipynb` - ipynb files used for data preprocessing and creating recommenders 


