from flask import Flask, request, jsonify


app = Flask(__name__)
    
orders = []

@app.route('/novo', methods=['POST'])
def create_order():
    order = request.json
    orders.append(order)
    return jsonify({"message": "created"}),201

@app.route('/pedidos', methods=['GET'])
def fetch_order():
    return jsonify(orders)

@app.route('/pedidos/<int:id>', methods=['GET'])
def fetch_single(id):
    order={}
    for o in orders:
        if o["id"] ==id:
            order=o
            
    if order=={}:
        return jsonify({"message": "not found"}), 404
    
    return jsonify(order)

@app.route('/pedidos/<int:id>', methods=['DELETE'])
def delete_single(id):
    order={}
    for i in range(len(orders)):
        if orders[i]["id"] ==id:
          order = orders.pop(i)
            
    if order=={}:
        return jsonify({"message": "not found"}), 404
    
    return jsonify({"message": "deleted"}),204

@app.route('/pedidos/<int:id>', methods=['PUT'])
def update_single(id):
    order = request.json
    _order = False
    for i in range(len(orders)):
        if orders[i]["id"] ==id:
            _order = True
            orders[i]=order
            
    if _order==False:
        return jsonify({"message": "not found"}), 404

    return jsonify({"message": "updated"})

if __name__ == '__main__':
    app.run(debug=False)