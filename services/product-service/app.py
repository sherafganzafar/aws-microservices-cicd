from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "product-service"
    })

@app.route("/products")
def get_products():
    products = [
        {"id": 1, "name": "Laptop", "price": 800},
        {"id": 2, "name": "Keyboard", "price": 50}
    ]
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
