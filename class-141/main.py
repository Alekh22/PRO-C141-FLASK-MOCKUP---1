from flask import Flask,jsonify,request
import csv
allmovies=[]
with open ("article.csv",encoding="utf8")as f:
    reader= csv.reader(f)
    data=list(reader)
    allmovies=data[1:]
liked_article=[]
unliked_article=[]

pp=Flask(__name__)

@app.route("/get-article")
def getarticle():
    return jsonify({"data":allmovies[0],"status":"success"})

@app.route("/liked_article",methods=["POST"])
def likedmovie():
    movies=allmovies[0]
    allmovies=allmovies[1:]
    liked_article.append(movies)
    return jsonify ({"status":"success"}),201

@app.route("/unliked_article",methods=["POST"])
def unlikedmovie():
    movies=allmovies[0]
    allmovies=allmovies[1:]
    unliked_article.append(movies)
    return jsonify ({"status":"success"}),201

if __name__ =="__main__":
    app.run()