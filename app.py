from flask import Flask, render_template, request, jsonify
from models import db, Track

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spotify.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

# Get all tracks
@app.route('/api/tracks', methods=['GET'])
def get_tracks():
    tracks = Track.query.all()
    return jsonify([track.to_dict() for track in tracks])

# Create a new track
@app.route('/api/tracks', methods=['POST'])
def create_track():
    data = request.json
    track = Track(**data)
    db.session.add(track)
    db.session.commit()
    return jsonify(track.to_dict()), 201

# Update a track
@app.route('/api/tracks/<int:track_id>', methods=['PUT'])
def update_track(track_id):
    track = Track.query.get(track_id)
    if not track:
        return jsonify({'error': 'Track not found'}), 404
    for key, value in request.json.items():
        setattr(track, key, value)
    db.session.commit()
    return jsonify(track.to_dict())

# Delete a track
@app.route('/api/tracks/<int:track_id>', methods=['DELETE'])
def delete_track(track_id):
    track = Track.query.get(track_id)
    if not track:
        return jsonify({'error': 'Track not found'}), 404
    db.session.delete(track)
    db.session.commit()
    return jsonify({'message': 'Track deleted'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
