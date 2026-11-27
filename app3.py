from flask import Flask, jsonify

import socket



app = Flask(__name__)



courses = [

    {"id": 1, "name": "Python Programming", "credits": 3},

    {"id": 2, "name": "Cloud Computing", "credits": 3},

    {"id": 3, "name": "DevOps Engineering", "credits": 4},

    {"id": 4, "name": "Cyber Security", "credits": 3},

    {"id": 5, "name": "Database Management", "credits": 3}

]



@app.route("/")

def home():

    return jsonify({

        "app": "App 3 - IT Course Management",

        "status": "Running",

        "served_by": socket.gethostname()

    })



@app.route("/courses")

def get_courses():

    return jsonify(courses)



@app.route("/courses/<int:course_id>")

def get_course(course_id):

    course = next(

        (c for c in courses if c["id"] == course_id),

        None

    )



    if course is None:

        return jsonify({"error": "Course not found"}), 404



    return jsonify(course)



@app.route("/health")

def health():

    return jsonify({"status": "healthy"}), 200





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
