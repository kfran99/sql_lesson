import hackbright_app

from flask import Flask, render_template, request

app = Flask(__name__)

# Code goes here

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github") 
    student = hackbright_app.get_student_by_github(student_github)
    grades = hackbright_app.get_grades_by_student(student_github)
    html = render_template("student_info.html", grades=grades,
                                                first_name=student[0],
                                                last_name=student[1],
                                                student_github=student_github,
                                                )
    return html

if __name__=="__main__":
    app.run(debug=True)