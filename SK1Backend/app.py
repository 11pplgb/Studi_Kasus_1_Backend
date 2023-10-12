from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

db = SQL("sqlite:///score.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if  request.method == "POST":
      name = request.form.get("name")
      score = request.form.get("score")

      db.execute("INSERT INTO score (name,score) VALUES(?,?)",name,score )
      return redirect("/")

    else:

      score = db.execute("SELECT * FROM score")
      

    return render_template("index.html", score=score)

@app.route("/edit/<id>", methods =["GET","POST"])
def edit_data(id):
  if request.method == "GET":
    editsc = db.execute("SELECT * from score WHERE id = ?",id)[0]
    print(editsc)
    return render_template("edit.html",editsc=editsc)
  elif request.method == "POST":
    editsc_name = request.form.get("name")
    editsc_score = request.form.get("score")
    db.execute("UPDATE score set name = ?, score = ? where id = ?", editsc_name,editsc_score,id)
    return redirect("/")
