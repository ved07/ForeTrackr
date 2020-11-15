import os
import pymongo
import json

def dummy(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if request.method == 'OPTIONS':
        # Allows GET requests from origin https://mydomain.com with
        # Authorization header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': '3600',
            'Access-Control-Allow-Credentials': 'true'
        }
        return ('', 204, headers)

    # Set CORS headers for main requests
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    request_json = request.get_json()
    mongostr = os.environ.get('MONGOSTR')
    client = pymongo.MongoClient(mongostr)
    db = client["hackumbc"]
    col = db.users 
    results = []
    payload = {}
    maxid = 0
    
    filename = "myfile.txt"
    
    if request_json:
        id = request_json['user']
        pw = request_json['pass']
        
        if 'filename' in request_json:
          filename = request_json['filename']
        for x in col.find():
            if id == x["uid"] and pw == request_json['pass']:
              
              os.system("python blockmain.py " + filename + " Log-In " + id)
            
              retjson = {}

              ##change required header

              retjson['status'] = "success"
              retjson['accesslevel'] = x["accesslevel"]
              retjson['id'] = id

              return json.dumps(retjson)
        
                
       
        retjson['mongoresult'] = "credentials error"
        retjson['details'] = payload
        retjson['id'] = id

        return json.dumps(retjson)


    retstr = "action not done"

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return retstr
