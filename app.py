import os
from flask import Flask, flash, request, redirect
from users.Users import usersModule
# from files.uploadfile import fileModule

UPLOAD_FOLDER = './data/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'super secret key'
app.register_blueprint(usersModule)
# app.register_blueprint(fileModule)

@app.route('/file', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    # check if the post request has the file part
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file:
      # filename = secure_filename(file.filename)
      filename = "uploaded_file.csv"
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return { 'data': 'File uploaded succesfully' }, 200
      # return redirect(url_for('download_file', name=filename))
  return ''''''

