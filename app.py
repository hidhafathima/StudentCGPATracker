from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)

conn=sqlite3.connect("students.db")
cursor=conn.cursor()

cursor.execute("""
CREATE  TABLE IF NOT EXISTS STUDENTS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    cgpa REAL
)
""")

conn.commit()
conn.close()
            
               
@app.route("/",methods=["GET","POST"])
def home():
    
    
     if request.method=="POST":
          

          student_name=request.form["student_name"]
          cgpa=request.form["cgpa"]

          

          conn=sqlite3.connect("students.db")
          cursor=conn.cursor()

          cursor.execute(
               "INSERT INTO students(name,cgpa) VALUES(?,?)",
               (student_name,cgpa)
          )
          print("Saving:",student_name,cgpa)
          conn.commit()
          conn.close()

          print("Saved to database")
          conn=sqlite3.connect("students.db")
          cursor=conn.cursor()

          cursor.execute("SELECT * FROM students")
          students=cursor.fetchall()
          print("Students from database:",students)

          conn.close()
              

     return render_template("index.html",students=students)
if __name__=="__main__":
    app.run(debug=True)
