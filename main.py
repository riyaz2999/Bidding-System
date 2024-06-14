import flask
import sqlite3
from pymongo import MongoClient

client=MongoClient("mongodb://127.0.0.1:27017/")
db=client['ecs']
ECSdata=db.login
ECSdata2=db.bid
ECSdata3=db.newuser
my_website = flask.Flask(__name__)


@my_website.route('/addingbid')
def Addingthebid():
    return flask.render_template("addbid.html")

@my_website.route('/mybid')
def mybid():
    return flask.render_template("mybid.html")

@my_website.route('/timebid')
def timebid():
    return flask.render_template("time based bid.html")

@my_website.route("/")
def my_index_page():
    return flask.render_template("login.html")

@my_website.route("/newuser")
def my_newuser_register_page():
    return flask.render_template("newuserregister.html")

@my_website.route("/bid")
def my_bid_page():
    return flask.render_template("bid.html")

@my_website.route("/about")
def my_createbid_page():
    return flask.render_template("createbid.html")

@my_website.route("/bidbutton",methods = ['post'])
def my_bidbutton_page():
    return flask.render_template("afterbidding.html")

@my_website.route("/contact")
def my_contact_page():
    return flask.render_template("contact.html")

@my_website.route("/dashboard")
def dashboard_page():
    return flask.render_template("dashboard.html")

@my_website.route("/registeruser", methods=['post'])
def my_regiser_user():
    entered_username = flask.request.form.get("username")
    entered_password = flask.request.form.get("password")
    entered_password = entered_password.lower()
    entered_email = flask.request.form.get("email")
    entered_mobileno = flask.request.form.get("mobileno")
    ECSdata.insert_one({"Username":entered_username,"Password":entered_password})
    return flask.render_template('display.html',username=entered_username,password=entered_password)
    print(entered_username, entered_password, entered_email, entered_mobileno)

    con = sqlite3.connect("my_database.sqlite3")

    cur = con.cursor()

    my_table_query = "create table if not exists userstable(name varchar(20),password varchar(15),email varchar(30),mobileno varchar(10))"
    cur.execute(my_table_query)

    cur.execute(f"select email from userstable where email='{entered_email}'")
    result = cur.fetchone()
    if result != None:
        return "Email Already Exists....Try again"
    else:
        my_insert_query = f"insert into userstable values('{entered_username}','{entered_password}','{entered_email}','{entered_mobileno}')"
        cur.execute(my_insert_query)
        con.commit()
        return "User Registered Successfully"


@my_website.route("/loginuser", methods=['post'])
def my_login():
    entered_username = flask.request.form.get("username")
    entered_password = flask.request.form.get("password")
    con = sqlite3.connect("my_database.sqlite3")
    cur = con.cursor()
    cur.execute(f"select * from userstable where name='{entered_username}' and password='{entered_password}'")

    result = cur.fetchone()
    if result is None:
        return flask.render_template("dashboard.html")
    else:
        return flask.render_template("dashboard.html")


if __name__ == "__main__":
    my_website.run(debug=True)

