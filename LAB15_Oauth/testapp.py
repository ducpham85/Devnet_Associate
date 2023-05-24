from flask import Flask,redirect,request,url_for
from authlib.integrations.requests_client import OAuth2Session
# import json
# import requests
app = Flask(__name__)
app.secret_key="hello"
client_id= '3fb6dbc1b1d93a9429dc'
client_secret='94cdd8b7aaa90f355522cc1d60f21dfd58e4f614'
client = OAuth2Session(client_id=client_id,client_secret=client_secret)
code=""
state=""
token=""
host="http://localhost:5050/github1"


@app.route('/login')
def login():
    auth_endpoint= 'https://github.com/login/oauth/authorize'
    uri,state= client.create_authorization_url(auth_endpoint)
    print(f"URI: {uri}")
    return redirect(uri)

@app.route("/github1/")
def getcode():
    global code, state
    code = request.args["code"]
    state=request.args["state"]
    # return code
    redirect_uri=url_for('fetch_token', _external=True)
    print(f"redrect_url: {redirect_uri}")
    return redirect(redirect_uri)
    
    
@app.route("/fetch_token",methods=['POST','GET'])
def fetch_token():
    authen= host+"?code="+code+"&state="+state
    print(authen)
    token_endpoint= 'https://github.com/login/oauth/access_token'
    
    tokenjson=client.fetch_token(token_endpoint,authorization_response=authen)
    return tokenjson["access_token"]
    

@app.route('/get_user', methods = ["GET"])
def authorize():
    
    resp = client.get('https://api.github.com/user',headers={"Authorization": "Bearer OAUTH-TOKEN"})
    profile = resp.json()
    return profile


if __name__=="__main__":
     app.run(host="0.0.0.0",port=5050,debug=True)
    # fetch_token()