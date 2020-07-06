from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

model=Flask(__name__)
model.config['SQLALCHEMY_BINDS'] = {'foo': 'sqlite://','bar': 'sqlite://'}
model.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(model)

@model.route('/genre',methods=['GET'])
def genre():
    try:
        str1=request.args.get('search')
        data = pd.DataFrame(pd.read_csv('dataset/moviedataset.csv'),columns=['Title','Genre','Plot'])
        tfidf = TfidfVectorizer(stop_words='english')
        data['Genre'] = data['Genre'].fillna('')
        tfidf_matrix = tfidf.fit_transform(data['Genre'])
        tfidf_matrix.shape
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        indices = pd.Series(data.index, index=data['Title']).drop_duplicates()
        sim_scores = list(enumerate(cosine_sim[indices[str1]]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:6]
        movie_indices =  [data['Title'].iloc[i[0]] for i in sim_scores]
        return jsonify(movie_indices)
    except Exception as ex:
        return (str(ex))
model.run()
