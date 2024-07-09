from flask import Blueprint, jsonify, request
from .models import User, List
from .schema import UserSchema
from . import db

main = Blueprint('main', __name__)


@main.route('/user/create', methods=['POST'])
def create_user():
    user = request.get_json()
    user_persist = User(**user)
    db.session.add(user_persist)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201


@main.route('/user/get_all', methods=['GET'])
def get_all_user():
    all_users = User.query.all()
    return jsonify(
        {
            "data": [user.to_dict() for user in all_users],
            "total_users": len(all_users)
        }
    )


@main.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            return jsonify(user.to_dict()), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main.route('/list/<int:list_id>', methods=['GET'])
def get_list_by_id(list_id):
    try:
        list_ = List.query.get(list_id)
        if list_:
            return jsonify(list_.to_dict())
        else:
            return jsonify({'error': 'List does not exist'})
    except Exception as e:
        return jsonify({'error': str(e)})


@main.route('/list/create', methods=['POST'])
def create_list():
    list_ = request.get_json()
    list_persist = List(**list_)
    db.session.add(list_persist)
    db.session.commit()
    return jsonify({'message': 'List created successfully'}), 201
