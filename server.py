#!/usr/bin/env python2.7

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from wand.image import Image
from wand.display import display
import os

UPLOAD_FOLDER = '/home/cbobco/src/ifwhopaintedwhat/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    img = Image(request.files['file'])
    img.format='png'
    img.save(os.path.join(app.config['UPLOAD_FOLDER'], "background.png"))
    # file = request.files['file']
    # if file and allowed_file(file.filename):
    #     filename = secure_filename(file.filename)
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #     print('here')
    #     return redirect(url_for('uploaded_file',
    #                             filename=filename))
        
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
