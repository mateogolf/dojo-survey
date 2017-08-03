from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def whatName():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    name = request.form["name"]
    print name
    location = request.form['location']
    print location
    fav_lang = request.form['favorite']
    print fav_lang
    comments = request.form['comments']
    print comments
    # , location=location,fav_lang=fav_lang,comments=comments)
    return render_template('result.html', name=name, location=location, fav_lang=fav_lang, comments=comments)


app.run(debug=True)
