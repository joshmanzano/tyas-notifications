from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Store the latest notification (in-memory, no persistence)
latest_notification = {
    'message': None,
    'timestamp': None
}

@app.route('/')
def index():
    return "Notification Service is running"

@app.route('/sender')
def sender():
    return render_template('sender.html')

@app.route('/receiver')
def receiver():
    return render_template('receiver.html')

@app.route('/api/send', methods=['POST'])
def send_notification():
    data = request.json
    message = data.get('message', '')

    if not message:
        return jsonify({'error': 'Message is required'}), 400

    latest_notification['message'] = message
    latest_notification['timestamp'] = datetime.now().isoformat()

    return jsonify({'success': True, 'message': 'Notification sent'})

@app.route('/api/check', methods=['GET'])
def check_notification():
    # Get the last check timestamp from client
    last_check = request.args.get('last_check')

    # If there's a notification and it's newer than the last check
    if latest_notification['message'] and latest_notification['timestamp']:
        if not last_check or latest_notification['timestamp'] > last_check:
            return jsonify({
                'has_notification': True,
                'message': latest_notification['message'],
                'timestamp': latest_notification['timestamp']
            })

    return jsonify({'has_notification': False})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
