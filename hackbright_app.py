import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    print """\
Student: %s %s
Github account: %s"""%(row[0], row[1], row[2])

def get_project_by_title(title):
    query = """SELECT title, description, max_grade FROM Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
Project: %s
Description: %s
Max_grade: %d"""%(row[0], row[1], row[2])

def get_grade_by_project(last_name, project_title):
    query = """SELECT first_name, last_name, project_title, grade FROM Grades JOIN Students ON (Students.github=Grades.student_github) WHERE project_title = ? and last_name = ?""" 
    DB.execute(query, (project_title, last_name))
    row = DB.fetchone()
    print """\
Student: %s %s
Project: %s
Grade: %s"""%(row[0], row[1], row[2], row[3])

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def make_new_student(first_name, last_name, github):
    query = """INSERT into Students values (?,?,?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s"%(first_name, last_name) 

def make_new_project(title, description, max_grade):
    query = """INSERT into Projects (title, description, max_grade) values (?,?,?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s"%(title)

def give_student_grade(student_github, project_title, grade):
    query = """INSERT into Grades values (?,?,?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print "Successfully added grade: %s for %s to %s"%(grade, student_github, project_title)

def main():
    connect_to_db()
    command = None
    while command != "quit":
        input_string = raw_input("HBA Database> ")
        input_list = input_string.split(None, 1)
        token_string = input_list[1]
        token_list = token_string.split(',')
        tokens = [a.strip() for a in token_list]
        command = input_list[0]
        args = tokens[:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "project":
            get_project_by_title(*args)
        elif command == "new_project":    
            make_new_project(*args)
        elif command == "grade":
            get_grade_by_project(*args)
        elif command == "give_grade":
            give_student_grade(*args)


    CONN.close()

if __name__ == "__main__":
    main()
