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
    tracks = Track.query.all()
    return jsonify([track.to_dict() for track in tracks])

@app.route('/api/tracks', methods=['POST'])
def create_track():
    data = request.json
    try:
        track = Track(**data)
        db.session.add(track)
        db.session.commit()
        return jsonify(track.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/tracks/<int:track_id>', methods=['PUT'])
def update_track(track_id):
    track = Track.query.get(track_id)
    if not track:
        return jsonify({'error': 'Track not found'}), 404
    try:
        for key, value in request.json.items():
            setattr(track, key, value)
        db.session.commit()
        return jsonify(track.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/tracks/<int:track_id>', methods=['DELETE'])
def delete_track(track_id):
    track = Track.query.get(track_id)
    if not track:
        return jsonify({'error': 'Track not found'}), 404
    try:
        db.session.delete(track)
        db.session.commit()
        return jsonify({'message': 'Track deleted'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080)
