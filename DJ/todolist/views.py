from django.shortcuts import render, redirect

from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://jaivikas2512:Rmjvv2512@cluster0.xwii3oi.mongodb.net/test"
)

UserData = client.User_Info
SignupCollection = UserData.New_users

from bson.objectid import ObjectId

# Create your views here.


def sessiontorf(req):
    activeuser = (req.session).get("Loged In User")
    print(activeuser)
    if activeuser:
        myuser = True
    else:
        myuser = False

    return myuser


def home(req):
    return render(req, "home.html", {"logg": sessiontorf(req)})


def signup(req):
    if req.method == "POST":
        print("========================")

        name = req.POST.get("username")
        email = req.POST.get("email")
        password = req.POST.get("password")

        if_user_exist = SignupCollection.find_one({"email": email})
        print("---------------------------")
        if if_user_exist:
            return redirect("loginpage")
        else:
            data = {"username": name, "email": email, "password": password}
            SignupCollection.insert_one(data)
            print(req.POST)
            return redirect("homepage")

    return render(req, "signup.html", {"logg": sessiontorf(req)})


def login(req):
    print(dict(req.session))
    if req.method == "POST":
        # Getting Email And Password Given By User For Login
        nameoremail = req.POST.get("usernameOremail")
        password = req.POST.get("loginpass")

        # Checking If Username Exists In Database
        userexists = SignupCollection.find_one({"username": nameoremail})
        if userexists:
            print("username Exists")
            dbpass = userexists.get("password")
            # Checking If The Given Password Matches The One With The Database
            if dbpass == password:
                req.session["Loged In User"] = nameoremail
                return redirect("homepage")
            else:
                return render(
                    req,
                    "login.html",
                    {"prompt": "Incorrect Username Or Password . Please Try Again ..."},
                )

        else:
            print("username doesn't Exists")
            userexists = SignupCollection.find_one({"email": nameoremail})

            # Checking If UserEmail Exists In Database
            if userexists:
                dbpass = userexists.get("password")
                usname = userexists.get("username")

                # Checking If The Given Password Matches The One With The Database
                if dbpass == password:
                    req.session["Loged In User"] = usname
                    return redirect("homepage")
                else:
                    return render(
                        req,
                        "login.html",
                        {
                            "prompt": "Incorrect Username Or Password . Please Try Again ..."
                        },
                    )

            else:
                print("userEmail dosen't Exists")
                return render(
                    req,
                    "login.html",
                    {"prompt": "Incorrect Username Or Password . Please Try Again ..."},
                )

    return render(req, "login.html")


def logout(req):
    del req.session["Loged In User"]
    return redirect("homepage")


def task(req):
    activeuser = dict((req.session))
    if activeuser:
        return render(req, "task.html", {"logg": sessiontorf(req)})
    else:
        return redirect("loginpage")


def addtask(req):
    # If ActiveUser Then We Get
    user = (dict(req.session)).get("Loged In User")
    userCol = UserData[user]
    if req.method == "POST":
        # Getting The Input Values To Store In db
        title = req.POST.get("title")
        category = req.POST.get("category")
        duedate = req.POST.get("date")
        duetime = req.POST.get("time")
        flag = req.POST.get("flag")
        note = req.POST.get("note")

        taskData = {
            "title": title,
            "Note": note,
            "category": category,
            "duedate": duedate,
            "duetime": duetime,
            "flag": int(flag),
            "completed": False,
        }
        # Inserting The taskdate Into DB
        mydata = userCol.insert_one(taskData)
        updatelocation = {"_id": ObjectId(oid=mydata.inserted_id)}
        updatevalue = {"$set": {"docId": str(mydata.inserted_id)}}

        userCol.update_one(updatelocation, updatevalue)
        return redirect("taskpage")
    return render(req, "addtask.html", {"logg": sessiontorf(req)})


# ----------------------------------------------------------------------------------------
def gettasks(req):
    user = (dict(req.session)).get("Loged In User")
    userCol = UserData[user]
    #  Getting The Whole TaskData And Sorting Based On Date Preference :
    addedtaskdata = list(userCol.find())
    newaddedtaskdata = []
    completedtaskdata = []
    for task in addedtaskdata:
        torf = task.get("completed")
        if torf:
            completedtaskdata.append(task)
        else:
            newaddedtaskdata.append(task)
    newaddedtaskdata = sorted(newaddedtaskdata, key=lambda x: x["duedate"])
    completedtaskdata = sorted(
        completedtaskdata, key=lambda x: (x["duedate"], x["flag"]), reverse=True
    )

    return {"addedtaskdata": newaddedtaskdata, "completedtasks": completedtaskdata}


def viewtask(req):
    print("View Remaining Tasks")
    return render(req, "viewtask.html", gettasks(req))


def viewcomptask(req):
    print("View Completed Tasks")
    return render(req, "completedtask.html", gettasks(req))


def overduetask(req):
    print("View Overduetasks Tasks")
    return render(req, "overduetask.html", gettasks(req))


def taskcomp(req, docId):
    user = (dict(req.session)).get("Loged In User")
    tasks = UserData[user]
    tasks.update_one({"docId": docId}, {"$set": {"completed": True}})
    return redirect("completedtaskpage")


def taskdel(req, docId):
    user = (dict(req.session)).get("Loged In User")
    tasks = UserData[user]
    tasks.delete_one({"docId": docId})
    return redirect("taskpage")
