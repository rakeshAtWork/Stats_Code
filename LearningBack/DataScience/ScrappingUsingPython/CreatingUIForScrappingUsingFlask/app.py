from flask import Flask,request,render_template,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq


app=Flask(__name__)


@app.route("/",methods=["GET"])
def Greet():
    return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)


