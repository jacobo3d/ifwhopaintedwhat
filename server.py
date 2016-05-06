#!/usr/bin/env python3.4

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from wand.image import Image
# from wand.display import display
import os
from styler import Styler_Class

if os.getcwd().endswith("static/uploads"):
    UPLOAD_FOLDER = os.getcwd() + "/"
    os.chdir(os.getcwd() + "/../../")
else:
    UPLOAD_FOLDER = os.getcwd() + "/static/uploads/"
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__, static_url_path = "", static_folder = "static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/stylize', methods=['POST'])
def stylize():
    upload_types = ["content_image", "style_image"]
    for upload_type in upload_types:
        file = request.files[upload_type]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(os.getcwd())
            os.rename("static/uploads/" + filename, "static/uploads/" + upload_type.split("_")[0] + ".jpg")
    styler = Styler_Class()
    styler.spawnImages()
    return render_template('done.html')


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
