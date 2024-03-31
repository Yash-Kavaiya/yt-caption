from flask import Flask, render_template_string, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

app = Flask(__name__)

# HTML template to display the results and include Bootstrap CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>YouTube Transcript API</title>
    <!-- Include Bootstrap CSS from CDN -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        pre {
            max-height: 400px; /* Adjust based on your preference */
            overflow-y: scroll; /* Enable vertical scrolling */
            overflow-x: hidden; /* Hide horizontal scrollbar */
            white-space: pre-wrap; /* Ensure long lines wrap */
            word-wrap: break-word; /* Break words to prevent horizontal overflow */
        }
    </style>
</head>
<body class="container">
    <h1 class="mt-5">YouTube Transcript Fetcher</h1>
    <p class="lead">To use this application, simply append the YouTube video ID to the URL.</p>
    <p>For example, if the video ID is <code>abcd1234</code>, navigate to <code>http://127.0.0.1:5000/abcd1234</code>.</p>
    
    {% if transcript %}
        <h2 class="mt-4">Transcript for Video ID: {{ video_id }}</h2>
        <pre>{{ transcript|safe }}</pre>
    {% else %}
        <p class="text-danger">Error: {{ error }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    # Display instructions on how to use the app
    return render_template_string(HTML_TEMPLATE)

@app.route('/<video_id>', methods=['GET'])
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Convert the transcript list to pretty JSON format
        pretty_transcript = jsonify(transcript).json
        return render_template_string(HTML_TEMPLATE, transcript=pretty_transcript, video_id=video_id)
    except (TranscriptsDisabled, NoTranscriptFound) as e:
        return render_template_string(HTML_TEMPLATE, error=str(e), video_id=video_id)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")