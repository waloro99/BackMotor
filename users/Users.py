from pyexpat import model
from flask import Flask, request, Blueprint

users = [];

# app = Flask(__name__)

usersModule = Blueprint('simple_page', __name__, template_folder='templates')

@usersModule.route('/users', methods=['GET'])
def getUsers():
  return {
    'data': list(map(lambda x: x['name'], users))
  }, 200


@usersModule.route('/users/signin', methods=['POST'])
def signin():
  data = request.json
  newUser = {
    'id': len(users) + 1,
    'name': data['username'],
    'rates': [],
    'model': {}
  };
  users.append(newUser);
  print(users);
  return { 'data': 'User register correctly' }, 201;


@usersModule.route('/users/login/<name>', methods=['POST'])
def login(name):
  for user in users:
    if user['name'] == name: return { 'data': 'User found' }, 200;
  return { 'data': 'User doesnt exists' }, 404;


@usersModule.route('/users/addReview/<name>', methods=['POST'])
def addReview(name):
  for user in users:
    if user['name'] == name:
      # Train model according to user review
      user['rates'].append(request.json);
      return { 'data': 'Review added' }, 200;
  return { 'data': 'User doesnt exists' }, 404;


@usersModule.route('/users/getRecomendation/<name>', methods=['GET'])
def getRecomendation(name):
  for user in users:
    if user['name'] == name:
      recomendations = user['model'].getRecomendation();
      return { 'data': recomendations }, 200;
  return { 'data': 'User not found' }, 404;