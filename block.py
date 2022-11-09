from flask import Flask, request, Response
import json
import sqlite3

app = Flask(__name__)

@app.route("/block", methods=["POST","GET"])
def block():
    data = request.get_json()
    data_dict = json.loads(data)
    amount = data_dict.get('amount')
    con = sqlite3.connect("block.db") #TODO factor DB ops into their own module
    cursor = con.cursor()
    try:
        cursor.execute("CREATE TABLE block(amount, owner)")
    except:
        pass
    if request.method == "GET":       
        result = cursor.execute("SELECT * FROM block where amount = ?", (amount,))
        blocks = result.fetchone()
        # Query database for amount and return block with ammount
        if not blocks:
            r = Response(status=404, mimetype="application/json")
            # Return 404 if the block with given amount does not exist
        else:
            r = Response(response=data, status=200, mimetype="application/json")
        r.headers["Content-Type"] = "text/json; charset=utf-8"
        return r
    elif request.method == "POST":
        owner = data_dict.get('owner')
        result = cursor.execute("INSERT into block VALUES(?,?)", (amount, owner,))
        con.commit()
        return "Posted", 201
    else:
        return "Don't do that", 400