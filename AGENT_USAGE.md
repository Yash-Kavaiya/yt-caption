# YouTube Transcript Agent Usage

## Overview
The YouTube Transcript Agent is a Flask web application that fetches and displays transcripts from YouTube videos using the YouTube Transcript API.

## Requirements
- Python 3.8+
- Flask
- youtube-transcript-api

## Installation

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Agent

Start the Flask application:
```bash
python main.py
```

The agent will start on `http://127.0.0.1:5000` (localhost) and `http://0.0.0.0:5000` (all network interfaces).

## Usage

### Web Interface

1. **Homepage**: Navigate to `http://127.0.0.1:5000/` to see usage instructions

2. **Fetch Transcript**: Navigate to `http://127.0.0.1:5000/<VIDEO_ID>` where `<VIDEO_ID>` is the YouTube video ID

### Examples

For a video with URL `https://www.youtube.com/watch?v=dQw4w9WgXcQ`:
- Video ID is: `dQw4w9WgXcQ`
- Transcript URL: `http://127.0.0.1:5000/dQw4w9WgXcQ`

The transcript will be displayed in a formatted JSON view with Bootstrap styling.

## API Endpoints

### `GET /`
Returns the homepage with usage instructions.

### `GET /<video_id>`
Fetches and displays the transcript for the specified video ID.

**Parameters:**
- `video_id` (path parameter): The YouTube video ID

**Response:**
- HTML page with transcript in JSON format
- Error message if transcript is not available

## Features

- Clean Bootstrap-based UI
- Scrollable transcript display
- Error handling for videos without transcripts
- Support for both auto-generated and manual captions

## Notes

- Some videos may not have transcripts available
- The API fetches English transcripts by default
- The application runs in debug mode by default (not suitable for production)

## Production Deployment

For production use, deploy with a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

Or use a reverse proxy like Nginx in front of the Flask application.
