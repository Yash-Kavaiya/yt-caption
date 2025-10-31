#!/usr/bin/env python3
"""
Demo script to show YouTube Transcript Agent capabilities
This script demonstrates the agent without requiring a web server
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import json


def fetch_transcript_demo(video_id):
    """
    Fetch and display a YouTube transcript
    
    Args:
        video_id: YouTube video ID (e.g., 'dQw4w9WgXcQ')
    """
    print(f"\n{'='*60}")
    print(f"Fetching transcript for video ID: {video_id}")
    print(f"{'='*60}\n")
    
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        
        print(f"✓ Successfully fetched transcript!")
        print(f"  Total entries: {len(transcript)}")
        print(f"\n{'='*60}")
        print("First 3 entries:")
        print(f"{'='*60}\n")
        
        for entry in transcript[:3]:
            print(json.dumps(entry, indent=2))
            print()
        
        if len(transcript) > 3:
            print(f"... and {len(transcript) - 3} more entries\n")
        
        return True
        
    except TranscriptsDisabled:
        print("✗ Error: Transcripts are disabled for this video")
        return False
        
    except NoTranscriptFound:
        print("✗ Error: No transcript found for this video")
        return False
        
    except Exception as e:
        print(f"✗ Error: {type(e).__name__}: {e}")
        return False


if __name__ == '__main__':
    print("""
╔════════════════════════════════════════════════════════════╗
║         YouTube Transcript Agent - Demo Script            ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    print("This demo shows how the YouTube Transcript Agent works.")
    print("Note: Requires internet connection to fetch transcripts.\n")
    
    # Example video IDs (these are real YouTube videos with transcripts)
    example_videos = [
        ('dQw4w9WgXcQ', 'Rick Astley - Never Gonna Give You Up'),
        ('jNQXAC9IVRw', 'Me at the zoo (First YouTube video)'),
    ]
    
    print("\nExample Usage:")
    print("-" * 60)
    print("Video ID: dQw4w9WgXcQ")
    print("Web URL: http://127.0.0.1:5000/dQw4w9WgXcQ")
    print("-" * 60)
    
    print("\nTo test with real data, run:")
    print("  python demo.py fetch <video_id>")
    print("\nTo start the web server:")
    print("  python main.py")
    print()
    
    import sys
    if len(sys.argv) > 2 and sys.argv[1] == 'fetch':
        video_id = sys.argv[2]
        fetch_transcript_demo(video_id)
    else:
        print("Run with 'fetch <video_id>' to test fetching a transcript")
        print("Example: python demo.py fetch dQw4w9WgXcQ")
