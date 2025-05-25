# Spotify Tracker

## Overview
This project is part of the Web Services and Applications module for the Data Analytics course at Atlantic Technological University, taught by Andrew Beatty. The Spotify Tracker is a web application that allows users to:

- Perform CRUD operations on Spotify track records stored locally
- Search tracks by artist name
- View track details including album, release date, popularity, duration, and preview link
- Manage a local database of tracks using a Flask backend and SQLite
- Interact with the application through a responsive web interface using Bootstrap and AJAX

## Live Demo
*(If hosted online, add your URL here)*  
🔗 [Spotify Tracker Live Demo](#)

## Features

### Local Track Management
- Add, view, update, and delete track records
- Paginated display of tracks for better navigation
- Search tracks by artist name with client-side filtering
- Responsive design using Bootstrap 5
- Interactive forms and buttons with JavaScript fetch API for RESTful interaction

### Backend and API
- Flask RESTful API with endpoints for CRUD operations
- SQLite database stored locally in the project root
- Real-time data updates without page reloads

## Project Structure

spotify-tracker/
├── app.py # Flask backend application
├── models.py # Database models using SQLAlchemy
├── templates/
│ └── index.html # Frontend HTML template
├── static/
│ ├── style.css # CSS styling with Bootstrap enhancements
│ └── script.js # JavaScript for AJAX and UI interactivity
├── spotify.db # SQLite database file (auto-generated)
├── README.md # This documentation file
└── requirements.txt # Python dependencies

## Installation Instructions

### Prerequisites
- Python 3.7+
- pip package manager

### Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spotify-tracker.git
   cd spotify-tracker

   Create and activate a virtual environment:
   python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the application:
python app.py

Usage Guide
Use the search bar to filter tracks by artist name.

Use the pagination buttons below the table to navigate large lists.

Click Update to edit a track's details.

Click Delete to remove a track.

Click Add Track (if implemented) to add new tracks to the database.

The Play button opens the track preview link in a new tab.

Troubleshooting
Make sure the SQLite database file spotify.db is writable and present in the root directory.

Verify Python packages are installed and up to date.

If the API routes fail, check your Flask app console logs for errors.

Contributing
Contributions are welcome! Please open issues or submit pull requests for bug fixes and feature enhancements.

Acknowledgments
Andrew Beatty for module instruction

Bootstrap for UI framework

Flask and SQLAlchemy for backend technology

Spotify API for track data inspiration

References
Flask Documentation

Bootstrap Documentation

SQLAlchemy Documentation