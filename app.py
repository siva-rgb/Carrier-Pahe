from flask import Flask , render_template, request, jsonify
import requests 
from database import fetch_all_jobs_db
app = Flask(__name__)

#creating a teemporary varable to to store the infrmation to show in job opening


@app.route('/')
def homepage():
    JOBS=fetch_all_jobs_db()
    return render_template("index.html", jobs=JOBS)

#to return json data
@app.route('/api/job')
def list_jobs():
    return jsonify(JOBS)

    
if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5002)