from flask import Flask, jsonify

app = Flask(__name__)

# To Do:
# Create routes, 
# GET purchasse_orders
# GET purchase_orders_by_id
# POST purchase_orders
# GET purchase_orders_items
# POST purchase_orders_items
@app.route('/')
def home():
    return 'Hello World!'


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


@app.route('/purchase_orders', methods=['GET'])
def get_purchase_orders():
    return jsonify(purchase_orders)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)