# Notification System

A simple Flask-based notification system with a sender interface and receiver interface that plays an audio alert when notifications are received.

## Features

- Send notifications through a web interface
- Receive notifications with audio alerts (plays 3 times)
- Works even when the receiver tab is not focused
- No authentication required
- Polls for new notifications every 2 seconds
- All receivers get the same notification

## Requirements

- Python 3.7+
- notification.mp3 file in the `static/` directory

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add your notification sound:
   - Place your `notification.mp3` file in the `static/` directory
   - The sound will play 3 times when a notification is received

3. Run the application:
```bash
python app.py
```

The server will start on `http://0.0.0.0:5000`

## Usage

### Sender Interface
Open `http://YOUR_SERVER_IP:5000/sender` in a web browser to send notifications.

1. Enter your notification message
2. Click "Send Notification"
3. All receivers will get the notification

### Receiver Interface
Open `http://YOUR_SERVER_IP:5000/receiver` in a web browser to receive notifications.

1. Click anywhere on the page when you first open it (required to enable sound)
2. Keep the tab open (can be in the background)
3. When a notification arrives, you'll hear the alarm sound play 3 times

## Deployment Notes

- The server runs on port 5000 by default
- All receivers will get the same notification
- Only the latest notification is stored (no history)
- No authentication is implemented
- For production, consider:
  - Using a production WSGI server (gunicorn, uWSGI)
  - Setting up a reverse proxy (nginx, Apache)
  - Adding authentication if needed
  - Changing `debug=True` to `debug=False` in app.py

## File Structure

```
tyas-notifications/
├── app.py                    # Flask backend
├── requirements.txt          # Python dependencies
├── static/
│   └── notification.mp3      # Audio file (you need to add this)
├── templates/
│   ├── sender.html          # Notification sender interface
│   └── receiver.html        # Notification receiver interface
└── README.md                # This file
```

## API Endpoints

- `GET /sender` - Sender interface
- `GET /receiver` - Receiver interface
- `POST /api/send` - Send a notification (JSON: `{"message": "text"}`)
- `GET /api/check` - Check for new notifications (optional param: `last_check`)
