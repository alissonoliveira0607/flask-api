from flask import Flask, jsonify, request

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

# Return all purchase_orders
@app.route('/purchase_orders', methods=['GET'])
def get_purchase_orders():
    return jsonify(purchase_orders)

# Return purchase_order from id
@app.route('/purchase_orders/<int:id>', methods=['GET'])
def get_purchase_orders_by_id(id):
    try:
        for orders in purchase_orders:
            if orders['id'] == id:
                return jsonify(orders)
            else:
                return jsonify({'message': f'Purchase order id {id} Not found'})
    except Exception as e:
        print(e)

# Create purchase order
@app.route('/purchase_orders', methods=['POST'])
def post_purchase_orders():
    request_data = request.get_json() # resgatando os dados do request
    for order in purchase_orders:
        if order['id'] == request_data['id']:
            return jsonify({'message': f'Purchase order id {request_data["id"]} already exists'}), 400
    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'items': []
        }
    purchase_orders.append(purchase_order)
    return jsonify(purchase_orders), 201



@app.route('/purchase_orders/<int:id>/items')
def get_items_purchase_orders(id):
    try:
        for order in purchase_orders:
            if order['id'] == id:
                return jsonify(order['items']), 200
            
        return jsonify({'message': f'Purchase order id {id} Not found'}), 400
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)