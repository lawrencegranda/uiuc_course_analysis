from flask import Flask, render_template, request
import pandas as pd
import time
from fetch import get_data


def clean_data():
    courses = get_data()
    return courses



app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1

data = clean_data()

@app.route("/")
def index():
    return render_template("bases/layout.html")

@app.route("/search", methods=['POST', 'GET'])
def search():
    query = request.form.get("query").lower()
    
    alist = []
    
    for k in data.keys():
        if query in k.lower():
            alist.append(k)
        elif query in data[k]["title"].lower():
            alist.append(k)
        else:
            for ins in data[k]["instructors"].keys():
                if query in ins.lower():
                    alist.append(k)
                    break
         
    courses = dict()       
    for k in alist:
        courses[k] = data[k]
    
    return render_template("list.html", courses=courses)



if __name__ == '__main__':
    app.run(debug=True)
