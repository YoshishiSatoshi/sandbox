from flask import Flask, request, Response
import json
import sqlite3

app = Flask(__name__)

@app.route("/block", methods=["POST","GET"])
def block():
    con = sqlite3.connect("blockdb") #TODO factor DB ops into their own module
    cursor = con.cursor()
    try:
        cursor.execute("CREATE TABLE block(amount, owner)")
    except:
        pass
    if request.method == "GET":
        data = request.get_json()
        amount = json.loads(data).get('amount')
        result = cursor.execute("SELECT * FROM block where amount = ?", (amount,))
        blocks = result.fetchone()
        # Query database for amount and return block with ammount
        if blocks is False:
            r = Response(response=data, status=404, mimetype="application/json")
            # Return 404 if the block with given amount does not exist
        else:
            r = Response(response=data, status=200, mimetype="application/json")
        r.headers["Content-Type"] = "text/json; charset=utf-8"
        return r
    elif request.method == "POST":
        return "Post"
    else:
        return "Don't do that", 400