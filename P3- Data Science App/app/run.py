import json
import plotly
import pandas as pd
import numpy as np
import operator
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from pprint import pprint
from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from sklearn.externals import joblib
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/Disaster_Response.db')
df = pd.read_sql_table('disaster_categories', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    
    #Getting the distribution of related messages sent per category
    category_related_counts = df.groupby('related').count()['message']
    category_related_names = ['Related' if i==1 else 'Not Related' for i in list(category_related_counts.index)]

    #Getting the distribution of requests messages sent per category
    requests_counts = df.groupby(['related','request']).count().loc[1,'message']
    category_requests_names = ['Requests' if i==1 else 'Not Requests' for i in list(requests_counts.index)]
    
    #getting the distribution of messages sent pert category
    category_names = df.iloc[:,4:].columns
    category_boolean = (df.iloc[:,4:] != 0).sum().values
    # Top ten categories count
    top_category_count = df.iloc[:,4:].sum().sort_values(ascending=False)[0:10]
    top_category_names = list(top_category_count.index)
    
    
    # create visuals
    # TODO: Below is an example - modify to create your own visuals
    graphs = [
        {
           'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Messages sent per Genres',
                'yaxis': {
                    'title': "Count of messages"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
       
        {
            'data': [
                Bar(
                    x=category_names,
                    y=category_boolean,
                    #orientation = 'h',
                    marker=dict(color="slategrey")
                    
                )
                  
            ],

            'layout': {
                'title': 'Distribution of Messages sent per Categories',
                'yaxis': {
                    'title': "Count of messages"
                },
                'xaxis': {
                    'title': "",
                    'tickangle': -35
                    #'rotation':90
                }
            }
            
        },
         {
            'data': [
                Bar(
                    x=top_category_names,
                    y=top_category_count,
                    marker=dict(color="slategrey")
                )
            ],

            'layout': {
                'title': 'Top Ten Categories',
                'yaxis': {
                    'title': "Count of messages"
                },
                'xaxis': {
                    'title': "Categories"
                }
            }
        },
        {
            'data': [
                Bar(
                    x=category_related_names,
                    y=category_related_counts,
                    marker=dict(color="slategrey")
                )
            ],

            'layout': {
                'title': 'Distribution of Messages sent that are Related with Disaster',
                'yaxis': {
                    'title': "Count of messages"
                },
                'xaxis': {
                    'title': ""
                }
            }
        },
        {
            'data': [
                Bar(
                    x=category_requests_names,
                    y=requests_counts,
                    marker=dict(color="slategrey")
                    
                )
            ],

            'layout': {
                'title': 'Distribution of Request Messages <br> considering only Disaster Related Messages',
                'yaxis': {
                    'title': "Count of messages"
                },
                'xaxis': {
                    'title': ""
                }
            }
        }
    ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()
