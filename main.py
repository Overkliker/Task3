from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<list>')
def nextlvl(list):
    if 'ol' in list:
        return render_template('list_prof_num.html')

    elif 'ul' in list:
        return render_template('list_prof_marks.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)