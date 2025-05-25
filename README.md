# Spotify Tracker

![Spotify Tracker Screenshot](https://github.com/user-attachments/assets/a558894e-971a-4112-818f-897f5d3cbb20)

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#) 

---

## Table of Contents
- [Overview](#overview)  
- [Live Demo](#live-demo)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Installation Instructions](#installation-instructions)  
- [Usage Guide](#usage-guide)  
- [Troubleshooting](#troubleshooting)  
- [Contributing](#contributing)  
- [Acknowledgments](#acknowledgments)  
- [License](#license)  
- [References](#references)  

---

## Overview

Spotify Tracker is a web application developed as part of the **Web Services and Applications** module for the Data Analytics course at Atlantic Technological University, taught by Andrew Beatty.

The app enables users to efficiently manage a local database of Spotify tracks by providing:

- Full CRUD (Create, Read, Update, Delete) functionality on track records.
- Real-time client-side search filtering by artist name.
- Detailed track views including album, release date, popularity, duration, and preview links.
- A Flask backend coupled with a SQLite database.
- A responsive, Bootstrap-powered web interface with AJAX support for seamless interaction.

---

## Live Demo

Access the live application here:  
🔗 [https://carlosrigueti.pythonanywhere.com/](https://carlosrigueti.pythonanywhere.com/)

---

## Features

### Local Track Management

- Add, update, view, and delete track records.
- Paginated display for easy navigation of large track lists.
- Responsive UI designed with Bootstrap 5.
- Client-side filtering by artist name for quick searching.
- Interactive forms and buttons powered by JavaScript Fetch API.

### Backend and API

- RESTful API implemented using Flask.
- SQLite database stored locally within the project.
- Real-time data updates without requiring page reloads.

---

## Project Structure

![Project Structure](https://github.com/user-attachments/assets/0f272613-2700-42de-a006-86a1ebcaeb95)

---

## Installation Instructions

### Prerequisites
- Python 3.7 or newer  
- pip (Python package manager)

### Setup Steps

1. **Clone the repository:**

    ![Image](https://github.com/user-attachments/assets/22d850e5-29c2-4747-aae5-7271969b9135)


2. **Create and activate a virtual environment:**

   ![Image](https://github.com/user-attachments/assets/f53342d4-0c46-40c8-8f32-e2f438bdbff0)

3. **Install dependencies:**

   ![Image](https://github.com/user-attachments/assets/74186c03-394b-4ba9-aa5b-c33502fb7e78)

4. **Run the application:**

  ![Image](https://github.com/user-attachments/assets/96aec753-5e14-4ce7-b2c5-ffcd563b026e)

---

## Usage Guide

- Use the **search bar** to filter tracks by artist name.
- Navigate through paginated results using the controls below the track list.
- Click **Update** to edit details of a track.
- Click **Delete** to remove a track from the database.
- Use **Add Track** to insert new tracks (if enabled).
- Click **Play** to open the track preview in a new tab.

---

## Troubleshooting

- Ensure the SQLite database file `spotify.db` is present and writable.
- Verify all required Python packages are installed and updated.
- Check Flask console logs for errors if API endpoints do not function correctly.

---

## Contributing

Contributions are highly welcome! Please:

- Open issues for bugs or feature requests.
- Submit pull requests for improvements or fixes.

---

## Acknowledgments

- Andrew Beatty for the course instruction.
- Bootstrap for the responsive UI framework.
- Flask and SQLAlchemy for backend technology.
- Spotify API for data inspiration.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## References

- [Flask Documentation](https://flask.palletsprojects.com/)  
- [Bootstrap Documentation](https://getbootstrap.com/docs/)  
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/) 