from flask import Flask, request, render_template
import ngl
import random
import string

app = Flask(__name__)
n = ngl.NGLWrapper()


def random_text(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    n.set_username(username)
    mode = request.form.get('mode')
    if mode == "1":
        length = int(request.form.get('length'))
        times = int(request.form.get('times'))
        for i in range(times):
            n.send_question(random_text(length))
    elif mode == "2":
        text = request.form.get('text')
        times = int(request.form.get('times'))
        for i in range(times):
            n.send_question(text)
    else:
        return 'Invalid mode', 400
    return 'questions sent successfully'


if __name__ == '__main__':
    app.run()
