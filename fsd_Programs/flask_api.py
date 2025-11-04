"""
flask_api.py
Tiny Flask API. To run: pip install flask && python flask_api.py
"""
try:
    from flask import Flask, jsonify, request
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Hello from Flask!'

    @app.route('/api/add', methods=['POST'])
    def add():
        data = request.get_json() or {}
        a = data.get('a', 0)
        b = data.get('b', 0)
        return jsonify({'result': a + b})

    if __name__ == '__main__':
        app.run(port=5000, debug=True)
except Exception:
    if __name__ == '__main__':
        print('Flask not installed. Install with: pip install flask')
