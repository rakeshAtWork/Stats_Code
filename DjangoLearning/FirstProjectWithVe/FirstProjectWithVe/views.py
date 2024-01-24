from django.http import HttpResponse
from django.shortcuts import render
# this is just to display the plain text response to browser

def aboutUs(request):
    data={
        "title":"Home Page",
        "msg":"This is a dynamic data from django",
        "lst":["hello","Hii","Byy"],
        "student_Details":[{'name':"rakesh",'phone':'991232323252'},
                           {'name':"Abhishek Kumar",'phone':'7004192779'}],
        "number":[]
    }
    return render(request,"index2.html",data)
    
def courseDetails(request,courseid):
    return HttpResponse(courseid)



def homePage(request):
    # Generation of dynamic Data to the Html Page
    data={
        "title":"Home Page",
        "msg":"This is a dynamic data from django",
        "lst":["hello","Hii","Byy"],
        "student_Details":[{'name':"rakesh",'phone':'991232323252'},
                           {'name':"Abhishek Kumar",'phone':'7004192779'}],
        "number":[]
    }
    return render(request,"index.html",data)

def userForm(request):
    finalans=0
    try:
        n1= int(request.GET['num1'])
        n2 = int(request.GET['num2'])
        finalans=n1+n2
        print("This is your output : - - "+str(n1+n2))
    except:
        pass
        
    return render(request,'userform.html',{'output':finalans})