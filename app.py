from flask import Flask , render_template, request, jsonify
import requests 

app = Flask(__name__)

#creating a teemporary varable to to store the infrmation to show in job opening

JOBS= [
    {
        'id': 1,
        'title': 'Data Analytics',
        'location': 'Bengaluru, India',
        'salary': '10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bengaluru, India',
        'salary': '12,00,000'
    },
    {
        'id': 3,
        'title': 'Dev-Ops Engineer',
        'location': 'Hydrabad, India',
        'salary': '8,00,000'
    },
    {
        'id': 5,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': '12,00,000'
    },
    {
        'id': 6,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '12,00,000'
    },
    {
        'id': 7,
        'title': 'System Engineer',
        'location': 'Remote',
        'salary': '12,00,000'
    }

]

@app.route('/')
def homepage():
    return render_template("index.html", jobs=JOBS)

@app.route('/api/job')
def list_jobs():
    return jsonify(JOBS)

    
if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5002)