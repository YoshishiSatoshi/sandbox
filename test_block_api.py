import requests
import json
# Send post request to add a block

def test_query_nonexistant_block():
    url = "http://127.0.0.1:5000/block"
    owner = "Bob"
    blockobj = {"owner": owner, "amount":9000} #TODO move to a fixture
    # Confirm block doesn't exist
    x = requests.get(url, json = json.dumps(blockobj))
    assert x.status_code == 404

def test_create_block():
    url = "http://127.0.0.1:5000/block"
    owner = "Bob"
    blockobj = {"owner": owner, "amount":9000}
    # Create the block
    x = requests.post(url, json = json.dumps(blockobj))
    assert x.status_code == 201
    # TODO fail to create duplicate blocks

def test_query_new_block():
    url = "http://127.0.0.1:5000/block"
    owner = "Bob"
    blockobj = {"owner": owner, "amount":9000}
    # Query to confirm block does now exist
    x = requests.get(url, json = json.dumps(blockobj))
    load = json.loads(x.text)
    load["owner"] == owner
    load["amount"] == blockobj["amount"]
    assert x.status_code == 200

def test_delete_block():
    url = "http://127.0.0.1:5000/block"
    owner = "Bob"
    blockobj = {"owner": owner, "amount":9000}
    # Delete the block
    x = requests.delete(url, json = json.dumps(blockobj))
    assert x.status_code == 200
    # Query to confirm the block was deleted
    x = requests.get(url, json = json.dumps(blockobj))
    assert x.status_code == 404