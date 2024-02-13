from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Tool, Tool_schema, Tools_schema

api = Blueprint('api',__name__, url_prefix='/api')

# @api.route('/getdata')
# def getdata():
#     return {'yee': 'haw'}

def jls_extract_def():
    
    return 


def jls_extract_def():
    
    return 


def jls_extract_def():
    
    return 


@api.route('/tool', methods = ['POST'])
@token_required
def create_tool(current_user_token):
    t_type = request.json['t_type']
    dia = request.json['dia']
    flutes = request.json['flutes'] = jls_extract_def()
    oal = request.json['oal'] = jls_extract_def()
    f_length = request.json['f_length'] = jls_extract_def()
    link = request.json['link']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    tool = Tool(t_type, dia, flutes, oal, f_length, link, user_token=user_token)

    db.session.add(tool)
    db.session.commit()

    response = Tool_schema.dump(tool)
    return jsonify(response)

@api.route('/tool', methods = ['GET'])
@token_required
def get_tool(current_user_token):
    a_user = current_user_token.token
    tools = Tool.query.filter_by(user_token = a_user).all()
    response = Tools_schema.dump(tools)
    return jsonify(response)

# Optional! Might not work 
# @api.route('/contacts/<id>', methods = ['GET'])
# @token_required
# def get_single_contact(current_user_token, id):
#     contact = Contact.query.get(id)
#     repsonse = contact_schema.dump(contact)
#     return jsonify(response)


#Updating
@api.route('/tool/<id>', methods = ['POST', 'PUT'])
@token_required
def update_tool(current_user_token, id):
    tool = Tool.query.get(id)
    tool.t_type = request.json['t_type']
    tool.dia = request.json['dia']
    tool.flutes = request.json['flutes']
    tool.oal = request.json['oal']
    tool.f_length = request.json['f_length']
    tool.link = request.json['link']
    tool.user_token = current_user_token.token 

    db.session.commit()
    response = Tool_schema.dump(tool)
    return jsonify(response)


#Delete Endpoint
@api.route('/tool/<id>', methods = ['DELETE'])
@token_required
def delete_tool(current_user_token, id):
    tool = Tool.query.get(id)
    db.session.delete(tool)
    db.session.commit()
    response = Tool_schema.dump(tool)
    return jsonify(response)
