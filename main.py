import json
from  flask import request
from config import app
from servise import *
from models import Order, User, Offer

@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_date_user(request.json)
        elif isinstance(request.json, dict):
            insert_date_user([request.json])
        else:
            print("Неизвестный тип данных!")

        return app.response_class(
            response=json.dumps(request.json, indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Order), indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_date_order(request.json)
        elif isinstance(request.json, dict):
            insert_date_order([request.json])
        else:
            print("Неизвестный тип данных!")

        return app.response_class(
            response=json.dumps(request.json, indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(Offer), indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_date_offer(request.json)
        elif isinstance(request.json, dict):
            insert_date_offer([request.json])
        else:
            print("Неизвестный тип данных!")

        return app.response_class(
            response=json.dumps(request.json, indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


@app.route("/users/<int:user_id>/", methods=['GET', 'PUT', 'DELETE'])
def get_user(user_id):
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all_by_id(User, user_id), indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal_2(User, user_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(User, user_id)
        return app.response_class(
            response=json.dumps(['OK'], indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

@app.route("/orders/<int:user_id>/", methods=['GET', 'PUT', 'DELETE'])
def get_order(user_id):
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all_by_id(Order, user_id), indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal_2(Order, user_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(Order, user_id)
        return app.response_class(
            response=json.dumps(['OK'], indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )

@app.route("/offers/<int:user_id>/", methods=['GET', 'PUT', 'DELETE'])
def get_offer(user_id):
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all_by_id(Offer, user_id), indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'PUT':
        update_universal_2(Offer, user_id, request.json)
        return app.response_class(
            response=json.dumps(['OK'], indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'DELETE':
        delete_universal(Offer, user_id)
        return app.response_class(
            response=json.dumps(['OK'], indent=2, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8080, debug=True)