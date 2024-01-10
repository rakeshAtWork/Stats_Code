# Building Urls Dynamically

from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return "welcome to web aaps."

@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the marks is "+str(score)


# result Checking

@app.route("/results/<int:score>")
def result(score):
    if score>50:
        return "You have passed!!! with grace marks of 10"
    else:
        return "You have failed."    


# redirect feature

@app.route("/calres/<int:marks>")
def calres(marks):
    url="success"
    return redirect(url_for(url,score= marks))


if __name__ == "__main__":
    app.run(debug=True)
    
    
    