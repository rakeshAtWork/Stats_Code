# integrating html with flask.

from flask import Flask,redirect,url_for, render_template, request

# render template is used to render html page.



app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template('index.html')


@app.route("/success/<int:score>")
def success(score):
    return render_template('result.html',result = "PASS",score=score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template('result.html',result = "FAIL",score=score)

# result Checking

@app.route("/results/<int:score>")
def result(score):
    if score>50:
        return "You have passed!!! with grace marks of 10"
    else:
        return "You have failed."    


# Result checker html page.

@app.route("/submit",methods=['GET',"POST"])
def greet():
    # our custom logic
    if request.method == "POST":
        science = float(request.form['science'])
        math = float(request.form['maths'])
        c= float(request.form['c'])
        data_science  = float(request.form['datascience'])
        
        total_score = (science+math+c+data_science)/4
        
    res=""
    
    if(total_score>=50):
        res="success"
    else:
        res ="fail"
    
    return redirect(url_for(res,score= total_score))

# redirect feature

@app.route("/calres/<int:marks>")
def calres(marks):
    url="success"
    return redirect(url_for(url,score= marks))


if __name__ == "__main__":
    app.run(debug=True)
    
    
    