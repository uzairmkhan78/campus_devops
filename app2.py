from flask import Flask, jsonify, request

import socket



app = Flask(__name__)



students = [

    {"id": 1, "name": "Ali", "department": "IT"},

    {"id": 2, "name": "Ahmed", "department": "Computer Science"},

    {"id": 3, "name": "Sara", "department": "Software Engineering"}

]



@app.route("/")

def home():

    return jsonify({

        "app": "App 2 - Student Management",

        "status": "Running",

        "served_by": socket.gethostname()

    })



@app.route("/students")

def get_students():

    return jsonify(students)



@app.route("/students", methods=["POST"])

def add_student():

    data = request.get_json(silent=True) or {}



    if not data.get("name") or not data.get("department"):

        return jsonify({"error": "Name and department required"}), 400



    student = {

        "id": max([s["id"] for s in students], default=0) + 1,

        "name": data["name"],

        "department": data["department"]

    }



    students.append(student)



    return jsonify({

        "m
