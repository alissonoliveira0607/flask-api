from flask import jsonify
from flask_restful import Resource

purchase_orders = [
    {
        "id": 1,
        "description": "Pedido de compra 1",
        'items': [
            {
                "id": 1,
                "description": "Item do pedido 1",
                "price": 100
            }
        ]
    }

]

class PurchaseOrders(Resource):
    def get(self):
        return jsonify(purchase_orders)