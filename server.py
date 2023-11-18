from flask import Flask, render_template, request, redirect
import json
from datetime import date
import time
import csv

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/<page>')
def page_nav(page):
    return render_template(page)

def write_to_csv(data):
    Date = date.today()
    Time = time.strftime('%H:%M:%S')

    email = data['email']
    subject = data['subject']
    msg = data['message']

    with open('./database.csv', mode = 'a', newline = '') as csvdata:
        writer = csv.writer(csvdata , delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL) # delimiter --> the seperating char
        writer.writerow([Date, Time, email, subject, msg])

def write_to_file(data):
    Date = date.today()
    Time = time.strftime('%H:%M:%S')
    with open('./database.txt', mode = 'a') as database:
        database.write(f'{Date} | {Time} \n')
        database.write(json.dumps(data))
        database.write('\n\n')


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)        
            return redirect('thankyou.html')
        except:
            return 'Did not save to the database'
    else:
        return redirect('oops.html')