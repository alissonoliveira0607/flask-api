from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from purchase_orders.routes import PurchaseOrders


app = Flask(__name__)
api = Api(app)


    
api.add_resource(PurchaseOrders, '/purchase_orders')
    
app.run(host='0.0.0.0', port=5000, debug=True)

