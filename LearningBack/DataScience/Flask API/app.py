from flask import Flask,request,jsonify,render_template
# in flask we have request module

app = Flask(__name__)


# Route making
@app.route("/")  # This is home page directory.
def helloWorld():
    return render_template("index.html")


# we have route with methods like GET POST
@app.route("/demo",methods=["POST"])
def math_operation():
    if (request.method=="POST"):
        op=request.json["operation"]
        if op=="add":
            num1=request.json["num1"]
            num2=request.json["num2"]
            res=num1+num2
            return jsonify(f"The operation is {op} and the result is {res}")
        else:
            return "OOps something not correct"
        

@app.route("/operation",methods=["POST"])
def operation():
    if (request.method=="POST"):
        op=request.form["operation"]
        if op=="add":
            num1=int(request.form["num1"])
            num2=int(request.form["num2"])
            res=num1+num2
            return render_template("result.html",result=res)
        
        


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)

