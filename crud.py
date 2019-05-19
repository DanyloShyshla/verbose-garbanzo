from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class BabyShop(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=100), unique=False)
    brand = db.Column(db.String(length=100), unique=False)

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand


class BabyShopSchema(ma.Schema):
    class Meta:
        fields = ("name", "brand")


baby_shop_schema = BabyShopSchema()
baby_shop_goods_schema = BabyShopSchema(many=True)


@app.route("/user", methods=["POST"])
def add_baby_shop():
    name = request.json['name']
    brand = request.json['brand']
    new_baby_shop = BabyShop(name, brand)
    db.session.add(new_baby_shop)
    db.session.commit()
    return jsonify(new_baby_shop)


@app.route("/user", methods=["GET"])
def get_baby_shop():
    all_baby_shop_goods = BabyShop.query.all()
    results = baby_shop_goods_schema.dump(all_baby_shop_goods)
    return jsonify(results.data)


@app.route("/user/<id>", methods=["GET"])
def baby_shop_detail(id):
    baby_shop = BabyShop.query.get(id)
    return baby_shop_schema.jsonify(baby_shop)


@app.route("/user/<id>", methods=["PUT"])
def baby_shop_update(id):
    baby_shop = BabyShop.query.get(id)
    name = request.json['name']
    brand = request.json['brand']
    baby_shop.name = name
    baby_shop.brand = brand
    db.session.commit()
    return baby_shop_schema.jsonify(baby_shop)


@app.route("/user/<id>", methods=["DELETE"])
def baby_shop_delete(id):
    baby_shop = BabyShop.query.get(id)
    db.session.delete(baby_shop)
    db.session.commit()
    return baby_shop_schema.jsonify(baby_shop)


if __name__ == '__main__':
    app.run(debug=True)
