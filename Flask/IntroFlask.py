# install python extenstion and make your environment ready.

from flask import Flask   # importing flask library.

app = Flask(__name__)   # creation of flask app.



# here i have used decorator.

@app.route('/')
def welcome():
    return "welcome to flask application with rakesh"


if __name__ == "__main__":
    print("You are in main function.")
    app.run(debug=True)  # here debug = true helps to do work under development
    
    
# This is WSDI Application.








