# Spotify Tracker

![Spotify Tracker Screenshot](https://github.com/user-attachments/assets/a558894e-971a-4112-818f-897f5d3cbb20)

---

## Overview

Spotify Tracker is a web application developed as part of the Web Services and Applications module for the Data Analytics course at Atlantic Technological University, taught by Andrew Beatty.

The app enables users to:

- Perform full CRUD operations on Spotify track records stored locally.
- Search tracks by artist name with client-side filtering.
- View detailed track information including album, release date, popularity, duration, and preview link.
- Manage a local SQLite database through a Flask backend.
- Interact via a responsive web interface built with Bootstrap and AJAX for seamless user experience.

---

## Live Demo

🔗 [https://carlosrigueti.pythonanywhere.com/](https://carlosrigueti.pythonanywhere.com/)

---

## Features

### Local Track Management
- Add, view, update, and delete track records.
- Paginated track listing for improved navigation.
- Search functionality filtering tracks by artist name in real-time.
- Responsive UI implemented with Bootstrap 5.
- Interactive forms and controls leveraging JavaScript Fetch API for RESTful communication.

### Backend and API
- RESTful API built with Flask providing endpoints for CRUD operations.
- Local SQLite database stored within the project root.
- Real-time updates reflected without full page reloads.

---

## Project Structure

![Project Structure](https://github.com/user-attachments/assets/0f272613-2700-42de-a006-86a1ebcaeb95)

---

## Installation Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. Clone the repository:

![Image](https://github.com/user-attachments/assets/22d850e5-29c2-4747-aae5-7271969b9135)

2. Create and activate a virtual environment:

![Image](https://github.com/user-attachments/assets/f53342d4-0c46-40c8-8f32-e2f438bdbff0)

3. Install dependencies:

![Image](https://github.com/user-attachments/assets/74186c03-394b-4ba9-aa5b-c33502fb7e78)

4. Run the application: 

![Image](https://github.com/user-attachments/assets/96aec753-5e14-4ce7-b2c5-ffcd563b026e)

# Usage Guide

* Use the search bar to filter tracks by artist name.
* Navigate through paginated results with the pagination controls below the track list.
* Click Update to edit track details.
* Click Delete to remove a track from the database.
* Use Add Track to insert new tracks (if available).
* Click Play to open the track preview in a new browser tab.

# Troubleshooting

* Ensure the SQLite database file spotify.db exists and has write permissions.
* Confirm all required Python packages are installed and up to date.
* Check Flask console logs for any API errors if functionality breaks.

# Contributing

* Contributions are welcome! Please open issues for bugs or feature requests, and submit pull requests for improvements.

# Acknowledgments

* Andrew Beatty for module instruction.
* Bootstrap for the UI framework.
* Flask and SQLAlchemy for backend technology.
* Spotify API for track data inspiration.

# References

* Flask Documentation
* Bootstrap Documentation
* SQLAlchemy Documentation