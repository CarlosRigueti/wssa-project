const form = document.getElementById('trackForm');
const trackIdInput = document.getElementById('trackId');
const trackNameInput = document.getElementById('trackName');
const artistNameInput = document.getElementById('artistName');
const albumNameInput = document.getElementById('albumName');
const ratingInput = document.getElementById('rating');
const previewUrlInput = document.getElementById('previewUrl');
const cancelEditBtn = document.getElementById('cancelEdit');
const tableBody = document.querySelector('#tracksTable tbody');

let editingId = null;

function loadTracks() {
    fetch('/api/tracks')
        .then(res => res.json())
        .then(data => {
            tableBody.innerHTML = '';
            data.forEach(track => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${track.track_name}</td>
                    <td>${track.artist_name}</td>
                    <td>${track.album_name || ''}</td>
                    <td>${track.rating || ''}</td>
                    <td><a href="${track.preview_url}" target="_blank">Play</a></td>
                    <td>
                        <button class="action-btn" onclick="editTrack(${track.id})">Edit</button>
                        <button class="action-btn" onclick="deleteTrack(${track.id})">Delete</button>
                    </td>
                `;
                tableBody.appendChild(tr);
            });
        });
}

function editTrack(id) {
    fetch(`/api/tracks`)
        .then(res => res.json())
        .then(data => {
            const track = data.find(t => t.id === id);
            if (!track) return;
            editingId = id;
            trackIdInput.value = id;
            trackNameInput.value = track.track_name;
            artistNameInput.value = track.artist_name;
            albumNameInput.value = track.album_name || '';
            ratingInput.value = track.rating || '';
            previewUrlInput.value = track.preview_url || '';
            cancelEditBtn.style.display = 'inline-block';
        });
}

function deleteTrack(id) {
    if (!confirm('Are you sure you want to delete this track?')) return;

    fetch(`/api/tracks/${id}`, {
        method: 'DELETE'
    }).then(res => {
        if (res.ok) loadTracks();
        else alert('Error deleting track');
    });
}

form.addEventListener('submit', e => {
    e.preventDefault();
    const data = {
        track_name: trackNameInput.value.trim(),
        artist_name: artistNameInput.value.trim(),
        album_name: albumNameInput.value.trim(),
        rating: ratingInput.value.trim(),
        preview_url: previewUrlInput.value.trim()
    };

    if (editingId) {
        fetch(`/api/tracks/${editingId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        }).then(res => {
            if (res.ok) {
                resetForm();
                loadTracks();
            } else {
                alert('Failed to update track');
            }
        });
    } else {
        fetch('/api/tracks', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        }).then(res => {
            if (res.ok) {
                resetForm();
                loadTracks();
            } else {
                alert('Failed to create track');
            }
        });
    }
});

cancelEditBtn.addEventListener('click', resetForm);

function resetForm() {
    editingId = null;
    trackIdInput.value = '';
    form.reset();
    cancelEditBtn.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', loadTracks);