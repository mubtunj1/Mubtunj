from flask import  Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Farm Manager',
        'location': 'Abeokuta, Nigeria',
        'salary': 'N. 300,000',
    },
    {
        'id' : 2,
        'title' : 'Farm Supervisor',
        'location': 'Ilorin, Nigeria',
        'salary': 'N. 80,000',
    },
    {
        'id' : 3,
        'title' : 'Agric Officer',
        'location': 'Maduguri, Nigeria',
        'salary': 'N. 500,000',
    },
    {
        'id' : 4,
        'title' : 'Livestock Manager',
        'location': 'Abeokuta, Nigeria',
        'salary': 'N. 400,000',
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name='Mubtunj')

# @app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    
if  __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)