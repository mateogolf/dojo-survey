from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def whatName():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    #rest of assigned values
    location = request.form['location']
    fav_lang = request.form['favorite']
    nameMessage = "Name cannot be empty!"
    emptyComment = "Comments cannot be empty!"
    bigComments = "Comments is too long!"
    #validation conditionals
    if len(request.form['name']) < 1 and (len(request.form['comments']) < 1 or len(request.form['comments']) > 120):
        session['name'] = ""
        session['comments'] = ""
        noName = nameMessage
        if len(request.form['comments']) < 1:
            noComments = emptyComment
        else:
            noComments = bigComments
        return render_template('index.html', noName=noName, noComments=noComments)
    elif len(request.form['name']) < 1:
        noName = nameMessage
        session['name'] = ""
        session['comments'] = request.form['comments']
        return render_template('index.html',noName=noName)
    elif len(request.form['comments']) < 1:
        noComments = emptyComment
        session['comments'] = ""
        session['name'] = request.form["name"]
        return render_template('index.html', noComments=noComments)
    elif len(request.form['comments']) > 120:
        noComments = bigComments
        session['comments'] = request.form['comments']
        session['name'] = request.form["name"]
        return render_template('index.html', noComments=noComments)
    else:
        session['name'] = request.form["name"]
        session['comments'] = request.form['comments']
    return render_template('result.html', location=location, fav_lang=fav_lang)


app.run(debug=True)
