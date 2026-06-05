from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)

conn=sqlite3.connect("students.db")
cursor=conn.cursor()

cursor.execute("""
CREATE  TABLE IF NOT EXISTS STUDENTS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    branch TEXT,
    cgpa REAL
)
""")

conn.commit()
conn.close()
            
               
@app.route("/",methods=["GET","POST"])
def home():
    
     
     if request.method=="POST":
          
          print("POST REQUEST RECIEVED")
          student_name=request.form["student_name"]
          branch=request.form["branch"]
          cgpa=request.form["cgpa"]

         

          conn=sqlite3.connect("students.db")
          cursor=conn.cursor()

          cursor.execute(
               "INSERT INTO students(name,branch,cgpa) VALUES(?,?,?)",
               (student_name,branch,cgpa)
          )
          
          conn.commit()
          conn.close()

          
     conn=sqlite3.connect("students.db")
     cursor=conn.cursor()

     cursor.execute("SELECT * FROM students")
     students=cursor.fetchall()

     conn.close()
              

     return render_template("index.html",students=students)
    
if __name__=="__main__":
    app.run(debug=True)
