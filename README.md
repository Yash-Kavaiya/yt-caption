# YouTube Screenshot & Transcript Generator

An automated GitHub Actions-powered tool that processes YouTube videos to generate high-quality PDFs with screenshots and text transcripts.

## Features

- **Automatic Processing**: Triggered when `.txt` files are added or modified
- **HD Quality**: Downloads videos in 1080p or 720p quality
- **Smart Screenshot Extraction**: Captures frames at custom intervals
- **Duplicate Removal**: Automatically removes duplicate screenshots
- **High-Quality PDFs**: Generates 600 DPI PDFs from screenshots
- **Text Transcripts**: Extracts and formats video captions/subtitles
- **Batch Processing**: Process multiple videos from multiple `.txt` files

## How It Works

### 1. Create a `.txt` File

Create any `.txt` file in the repository with YouTube URLs and intervals:

```
# my_videos.txt
https://youtu.be/VIDEO_ID,10
https://youtu.be/ANOTHER_VIDEO,5
```

**Format:** `URL,INTERVAL`
- `URL`: YouTube video URL (youtu.be or youtube.com format)
- `INTERVAL`: Screenshot interval in seconds (optional, defaults to 5)

### 2. Commit and Push

```bash
git add my_videos.txt
git commit -m "Add videos to process"
git push
```

### 3. Automatic Processing

GitHub Actions will automatically:
1. Detect the `.txt` file change
2. Download each video in HD quality
3. Extract screenshots at specified intervals
4. Generate transcript from video captions
5. Create high-quality PDF from screenshots
6. Commit results back to the repository

### 4. Access Results

Results are saved in the `output/` directory:

```
output/
├── Video_Title_1/
│   ├── images/               # PNG screenshots
│   ├── Video_Title_1_HD.pdf  # PDF document
│   └── Video_Title_1_transcript.txt  # Text transcript
├── Video_Title_2/
│   └── ...
└── README.md                  # Index of all processed videos
```

## Examples

### Single Video

Create `videos.txt`:
```
https://youtu.be/dQw4w9WgXcQ,5
```

This will:
- Download the video in HD
- Take a screenshot every 5 seconds
- Generate a PDF with all screenshots
- Extract the transcript

### Multiple Videos with Different Intervals

Create `batch_videos.txt`:
```
# Educational content (100-second intervals)
https://youtu.be/pOFcwcwtv3k,100

# Music video (10-second intervals)
https://youtu.be/dQw4w9WgXcQ,10

# Tutorial (5-second intervals for detailed capture)
https://youtu.be/WNAkSAuhYhw,5
```

### Organized by Topic

Create separate files for different topics:

**unfold_data_science/llm.txt:**
```
https://www.youtube.com/watch?v=VIDEO_ID_1,8
https://www.youtube.com/watch?v=VIDEO_ID_2,8
```

**tutorials/python.txt:**
```
https://youtu.be/TUTORIAL_1,10
https://youtu.be/TUTORIAL_2,10
```

## Output Details

### PDF Features
- **Resolution**: 600 DPI
- **Format**: Multi-page PDF
- **Quality**: 95% JPEG quality
- **Optimization**: Enabled for smaller file sizes
- **Max Dimension**: 3000px (automatically scaled)

### Transcript Features
- **Format**: Plain text, 80 characters per line
- **Encoding**: UTF-8
- **Source**: Auto-generated or manual captions
- **Cleaning**: HTML tags removed, properly formatted

### Screenshot Features
- **Format**: PNG (high quality)
- **Naming**: `VideoTitle_0000s.png`, `VideoTitle_0005s.png`, etc.
- **Duplicate Removal**: SHA256 hash-based detection
- **Progress**: Real-time percentage updates

## GitHub Actions Workflow

The workflow (`/.github/workflows/youtube-screenshot.yml`) runs when:

1. **Push to main/master branch** with changes to `.txt` files
2. **Manual trigger** via GitHub Actions UI

### Workflow Features
- **Timeout**: 4 hours maximum
- **Environment**: Ubuntu-latest with Python 3.11
- **Dependencies**: FFmpeg, yt-dlp, Pillow, NumPy
- **Artifacts**: PDFs, transcripts, and complete output uploaded
- **Auto-commit**: Results committed back to repository

## Usage Tips

### Best Practices

1. **Choose Appropriate Intervals**
   - Lectures/Tutorials: 30-100 seconds
   - Music Videos: 5-10 seconds
   - Presentations: 10-20 seconds

2. **File Organization**
   - Group videos by topic in subdirectories
   - Use descriptive filenames (e.g., `ml_tutorials.txt`)
   - Add comments to explain video categories

3. **URL Formats**
   Both formats work:
   - Short: `https://youtu.be/VIDEO_ID`
   - Long: `https://www.youtube.com/watch?v=VIDEO_ID`
   - With parameters: `https://youtu.be/VIDEO_ID?si=XXXX`

### Comments

Use `#` for comments:
```
# Machine Learning Course - Week 1
https://youtu.be/VIDEO_1,10

# Machine Learning Course - Week 2
https://youtu.be/VIDEO_2,10
```

## Troubleshooting

### No Screenshots Generated
- Check if the video URL is correct
- Ensure the video is publicly accessible
- Verify the interval is not larger than video duration

### No Transcript Generated
- Some videos don't have captions available
- The workflow will still generate PDF screenshots
- Check the Actions log for details

### Workflow Not Triggering
- Ensure you're pushing to `main` or `master` branch
- Verify the file extension is `.txt`
- Check that the file is not in excluded paths (`.git`, `.github`)

## Manual Testing

To test locally without GitHub Actions:

```bash
# Install dependencies
pip install yt-dlp pillow numpy

# Run the processor
python process.py "https://youtu.be/VIDEO_ID" 10 output
```

## File Exclusions

The following `.txt` files are automatically excluded:
- `requirements.txt`
- `requirements-*.txt`
- `deps.txt`
- Files in `.git/` directory
- Files in `.github/` directory
- Files in `output/` directory

## Repository Structure

```
yt-caption/
├── .github/
│   └── workflows/
│       └── youtube-screenshot.yml  # Main workflow
├── output/                          # Generated results (auto-created)
├── videos.txt                       # Your video lists
├── example.txt                      # Example format
├── unfold_data_science/             # Organized by topic
│   ├── llm.txt
│   └── slm.txt
├── main.py                          # Flask API (optional)
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Advanced Features

### HD Quality Guarantee
The processor tries multiple quality formats in order:
1. 1080p MP4 video + M4A audio
2. 720p MP4 video + M4A audio
3. Best available quality

### Duplicate Detection
- Uses SHA256 hashing to identify identical frames
- Automatically removes duplicates
- Reports number of duplicates removed

### Rate Limiting
- 5-second delay between video processing
- Prevents YouTube rate limiting
- Ensures stable downloads

## Contributing

To add new features or fix bugs:

1. Fork the repository
2. Make your changes
3. Test with sample videos
4. Submit a pull request

## License

This project is open source. Feel free to use and modify.

## Credits

Built with:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video downloading
- [FFmpeg](https://ffmpeg.org/) - Video processing
- [Pillow](https://python-pillow.org/) - Image/PDF manipulation
- [GitHub Actions](https://github.com/features/actions) - Automation

---

**Happy Video Processing!** 🎬📸📄
