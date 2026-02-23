# Intelligent Video Data Collection & Behavioural Analysis System

1. Project Overview

This project implements an AI-driven video analytics pipeline that automatically collects public YouTube videos and converts unstructured video content into structured behavioural insights.

The system:
- Scrapes public YouTube videos (Hindi/English, Indian context)
- Downloads short clips (≤30 seconds)
- Analyzes video and audio using AI + rule-based methods
- Generates ethical, approximate behavioural descriptions
- Stores results in a structured video repository and CSV file

The pipeline follows responsible AI practices and does not perform identity recognition.

2. Key Features

- Automated YouTube video scraping (post-processing based)
- Video trimming and preprocessing
- Face-based age, gender, and emotion inference (approximate)
- Audio-based speech and loudness analysis
- Accessory detection (spectacles, helmet, bag, etc.)
- Posture inference (standing / sitting)
- Natural language behavioural description generation
- CSV-based tracking and analysis (mandatory requirement)

3. Project Structure
pipeline/
│
├── main.py
│
├── data/
│   ├── raw_videos/
│   ├── processed_videos/
│   └── metadata.csv
│
├── scripts/
│   ├── scrape_youtube.py
│   ├── download_video.py
│   ├── extract_frames.py
│   ├── extract_audio.py
│   ├── analyze_faces.py
│   ├── analyze_audio.py
│   ├── detect_objects.py
│   ├── infer_clothing.py
│   ├── infer_activity.py
│   ├── fuse_behaviour.py
│   ├── generate_description.py
│   └── update_csv.py
│
├── requirements.txt
└── README.txt


4. System Requirements

Operating System
- Windows 10 / 11 (tested)
- Linux / macOS should also work with minor path changes

Python
- Python 3.9 or 3.10 (recommended)
- Python 3.11+ not recommended due to ML library compatibility

5. Dependency Installation

Step 1: Create Virtual Environment
``` python -m venv behav_env ```

Activate:
Windows

``` behav_env\Scripts\activate```

Linux / macOS
```source behav_env/bin/activate```

Step 2: Install Python Dependencies
```pip install -r requirements.txt```

Step 3: Install FFmpeg (Mandatory)
FFmpeg is required for video trimming and audio extraction.

Windows (Manual – Recommended)

- Download FFmpeg from:
https://www.gyan.dev/ffmpeg/builds/

- Extract and move to:
``` C:\ffmpeg ```
- Ensure this path exists:
```C:\ffmpeg\bin\ffmpeg.exe```
- Add ```C:\ffmpeg\bin``` to System PATH
- Open a new terminal and verify:
```ffmpeg -version```

6. How the Pipeline Works

- Scrapes YouTube videos using a generic search query
- Downloads videos (≤30 seconds)
- Extracts frames and audio
- Runs AI-based visual and audio analysis
- Infers behaviour using fusion logic
- Generates a natural language description
- Appends results to metadata.csv
Filtering based on age, gender, emotion, etc. is done after analysis, not at search time.

7. Execution Instructions (IMPORTANT)
Step 1: Ensure Environment Is Active
```behav_env\Scripts\activate```
Step 2: Run the Complete Pipeline
From the pipeline/ directory:
```python main.py```

What Happens Automatically
- Videos are searched and downloaded
- AI analysis is performed
- Descriptions are generated
- data/metadata.csv is updated row-by-row
Console output will display processing progress and generated descriptions.

8. Output Files
8.1 Video Repository
- data/raw_videos/ → downloaded video clips
- data/processed_videos/ → frames and audio per video

8.2 CSV Tracking File (Mandatory)
- data/metadata.csv

Sample row:
```
Video ID,Video method,Language,Gender,Age Group,Region,Description
LuZV9kkzscg,scraped,Hindi/English,Man,26-35,Unknown,"The video likely shows a 26–35 man standing, speaking calmly, appearing happy, wearing casual or traditional attire and spectacles."
```

9. Ethical & Responsible AI Practices
- Only publicly available YouTube videos are used
- No face recognition or identity tracking
- All attributes are approximate
- No personal data is stored
- Descriptions use probabilistic language (e.g., likely, appearing)

10. Limitations
- Clothing classification is coarse (rule-based)
- Region inference is indirect
- Emotion detection is approximate
- Designed for analysis, not surveillance

11. Future Enhancements
- Pose estimation using MediaPipe
- Improved clothing classification
- Query-based filtering interface
- Dashboard visualization

12. How to Verify Correct Execution (For Judges)

After running main.py:
- Check console output for generated descriptions
- Open data/metadata.csv
- Verify new rows are appended
- Confirm video folders are created under processed_videos/

If these are present, the system is functioning correctly.


