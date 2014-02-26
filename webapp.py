import hackbright_app

from flask import Flask, render_template, request

app = Flask(__name__)

# Code goes here

# @app.route("/")
# def get_github():
#     return render_template("get_github.html")

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github") 
    student = hackbright_app.get_student_by_github(student_github)
    grades = hackbright_app.get_grades_by_student(student_github)
    html = render_template("student_info.html", grades=grades,
                                                first_name=student[0],
                                                last_name=student[1],
                                                student_github=student_github
                                                )
    return html

@app.route("/project")
def get_grades():
    hackbright_app.connect_to_db()
    project = request.args.get("project")
    grades = hackbright_app.get_grade_by_project(project)
    html = render_template("project_info.html", project_title=project,
                                                grades=grades)
    return html

@app.route("/grade")
def give_grade():
    hackbright_app.connect_to_db()
    title = request.args.get("title")
    student_github = request.args.get("student_github")
    grade = request.args.get("grade")
    give_grade = hackbright_app.give_student_grade(title, student_github, grade)
    html = render_template("grade.html", give_grade=give_grade)
    return html

@app.route("/new_student")
def post_student():
    return render_template("new_student.html")

@app.route("/new_student2")
def post_student2():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student_github")
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    student = hackbright_app.make_new_student(first_name, last_name, student_github)
    html = render_template("new_student2.html", student=student)
                                                
    return html

@app.route("/new_project")
def post_project():
    return render_template("new_project.html")

@app.route("/new_project2")
def post_project2():
    hackbright_app.connect_to_db()
    title = request.args.get("title")
    description = request.args.get("description")
    max_grade = request.args.get("max_grade")
    project = hackbright_app.make_new_project(title, description, max_grade)
    html = render_template("new_project2.html", project=project)
                                                
    return html


if __name__=="__main__":
    app.run(debug=True)