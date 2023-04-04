import utils.scrap as scrap
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/divar', methods=['POST'])
def index():
    products = scrap.get_products()
    return products
 
if __name__ == '__main__':
    app.run()