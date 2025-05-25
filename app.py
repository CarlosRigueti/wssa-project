import os
from flask import Flask, render_template, request, jsonify
from models import db, Track

app = Flask(__name__)

# Absolute path of the project root directory
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite database file path in the project root
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'spotify.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

@app.route('/')
def index():
    # Render the main page template
    return render_template('index.html')

@app.route('/api/tracks', methods=['GET'])
def get_tracks():
    # Retrieve all track records from the database
    tracks = Track.query.all()
    # Return the list of tracks as JSON
    return jsonify([track.to_dict() for track in tracks])

@app.route('/api/tracks', methods=['POST'])
def create_track():
    # Get JSON data from the POST request body
    data = request.json
    try:
        # Create a new Track object with the data provided
        track = Track(**data)
        db.session.add(track)
        db.session.commit()
        # Return the created track data with HTTP 201 status
        return jsonify(track.to_dict()), 201
    except Exception as e:
        # Roll back the session if an error occurs
        db.session.rollback()
        # Return error message with HTTP 400 status
        return jsonify({'error': str(e)}), 400

@app.route('/api/tracks/<int:track_id>', methods=['PUT'])
def update_track(track_id):
    # Find track by ID
    track = Track.query.get(track_id)
    if not track:
        # Return 404 if track not found
        return jsonify({'error': 'Track not found'}), 404
    try:
        # Update track attributes with data from request JSON
        for key, value in request.json.items():
            setattr(track, key, value)
        db.session.commit()
        # Return updated track data
        return jsonify(track.to_dict())
    except Exception as e:
        # Roll back session on error
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/tracks/<int:track_id>', methods=['DELETE'])
def delete_track(track_id):
    # Find track by ID
    track = Track.query.get(track_id)
    if not track:
        # Return 404 if track not found
        return jsonify({'error': 'Track not found'}), 404
    try:
        # Delete track from database
        db.session.delete(track)
        db.session.commit()
        # Confirm deletion
        return jsonify({'message': 'Track deleted'})
    except Exception as e:
        # Roll back session on error
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    with app.app_context():
        # Create all database tables before first request
        db.create_all()
    # Run Flask app in debug mode
    app.run(debug=True)
