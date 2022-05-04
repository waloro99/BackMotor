import os
from flask import Flask, flash, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename
from app import app

fileModule = Blueprint('simple_page', __name__, template_folder='templates')

UPLOAD_FOLDER = '../data/'

# app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@fileModule.route('/file', methods=['POST'])
def upload_file():
  # check if the post request has the file part
  if 'file' not in request.files:
    flash('No file part')
    return redirect(request.url)
  file = request.files['file']
  if file.filename == '':
    # flash('No selected file')
    return {'data': 'No selected file'}, 400
  if file:
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  return { 'data': 'File uploaded succesfully' }, 200