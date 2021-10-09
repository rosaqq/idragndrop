import json, time, random

from flask import Flask, render_template

import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/media'
ALLOWED_EXTENSIONS = {'png', 'jpg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = f'{random.randint(0, 99999)}yeet{random.randint(0, 99999)}yeet{random.randint(0, 99999)}'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():  # put application's code here
    return render_template('index.html', timestamp=str(int(time.time())))


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        print()
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return json.dumps({'success': False, 'error': 'Something went wrong. File has not been received.'})

        file = request.files.getlist('file')[-1]

        if file and allowed_file(file.filename):
            filename = 'menu.png'  # secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return json.dumps({'success': False, 'error': f'Formato não suportado'})

        return json.dumps({'success': True, 'error': ''})
    return render_template('upload.html')


if __name__ == '__main__':
    app.run()
