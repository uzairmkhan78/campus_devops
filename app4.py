from flask import Flask, jsonify, request

import socket



app = Flask(__name__)



tickets = [

    {

        "id": 1,

        "issue": "Computer not starting",

        "department": "Computer Lab",

        "status": "Open"

    },

    {

        "id": 2,

        "issue": "Internet connection problem",

        "department": "Networking Lab",

        "status": "In Progress"

    }

]



@app.route("/")

def home():

    return jsonify({

        "app": "App 4 - IT Helpdesk",

        "status": "Running",

        "served_by": socket.gethostname()

    })



@app.route("/tickets")

def get_tickets():

    return jsonify(tickets)



@app.route("/tickets", methods=["POST"])

def create_ticket():

    data = request.get_json(silent=True) or {}



    if not data.get("issue") or not data.get("department"):

        return jsonify({

            "error": "Issue and department are required"

        }), 400



    ticket = {

        "id": max([t["id"] for t in tickets], default=0) + 1,

        "issue": da
