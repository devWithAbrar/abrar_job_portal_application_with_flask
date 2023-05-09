from flask import Flask, render_template, jsonify


app = Flask(__name__)


# Job List

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Dhaka, Bangladesh',
        'salary': 'BDT. 1,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Chattagram, Bangladesh',
        'salary': 'BDT. 1,02,000'
    },
    {
        'id': 3,
        'title': 'Web Developer',
        'location': 'Remote',
        'salary': 'BDT. 1,00,300'
    },
    {
        'id': 4,
        'title': 'App Developer',
        'location': 'Intern',
        'salary': 'BDT. 80,000'
    },
    {
        'id': 5,
        'title': 'Frontend Developer',
        'location': 'Remote',
        'salary': 'BDT. 1,80,000'
    },
]

# ==================== Blank/Home Route ==================


@app.route("/")
def hello_world():
    return render_template('index.html', jobs=JOBS)


# ====================== API Route =======================
@app.route("/api/jobs")
def API():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
