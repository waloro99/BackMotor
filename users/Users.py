from pyexpat import model
from flask import Flask, request, Blueprint

users = [];

usersModule = Blueprint('simple_page', __name__, template_folder='templates')

@usersModule.route('/users', methods=['GET'])
def getUsers():
  return {
    'data': list(map(lambda x: x['name'], users))
  }, 200

@usersModule.route('/users/<name>', methods=['GET'])
def getUser(name):
  for user in users:
    if user['name'] == name:
      return { 'data': user["rates"] }, 200;
  return { 'data': 'User not found' }, 404;


@usersModule.route('/users/signin', methods=['POST'])
def signin():
  data = request.json
  newUser = {
    'id': len(users) + 1,
    'name': data['username'],
    'rates': [],
    'model': {}
  };
  for user in users: 
    if user['name'] == data['username']: return { 'data': 'User Already exists' }, 409;
  users.append(newUser);
  return { 'data': 'User register correctly' }, 201;


@usersModule.route('/users/login/<name>', methods=['POST'])
def login(name):
  for user in users:
    if user['name'] == name: return { 'data': True }, 200;
  return { 'data': False }, 404;


@usersModule.route('/users/addReview/<name>', methods=['POST'])
def addReview(name):
  for user in users:
    if user['name'] == name:
      for rate in user['rates']: 
        if request.json["movie"] == rate["movie"]: return { 'data': 'review already exists' }, 409;
      
      # Train model according to user review
      user['rates'].append(request.json);
      return { 'data': 'Review added' }, 200;
  return { 'data': 'User doesnt exists' }, 404;

@usersModule.route('/users/updateReview/<name>', methods=['PUT'])
def updateReview(name):
  for user in users:
    if user['name'] == name:
      for rate in user['rates']: 
        if request.json["movie"] == rate["movie"]: 
          rate["liked"] = request.json["liked"];
          return { 'data': 'Review updated' }, 200;
      return { 'data': 'Review doesnt exists' }, 404;
  return { 'data': 'User doesnt exists' }, 404;


@usersModule.route('/users/getRecomendation/<name>', methods=['GET'])
def getRecomendation(name):
  for user in users:
    if user['name'] == name:
      # recomendations = user['model'].getRecomendation();
      return { 'data': "Waifus :)" }, 200;
  return { 'data': 'User not found' }, 404;