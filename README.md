# YouTube Downloader

A clean and simple YouTube video & playlist downloader with both a **CLI interface** and a **Streamlit web app**. Supports quality selection, playlist downloading, and in-browser file saving — built with `yt-dlp` under the hood.

## Features

- Download individual YouTube videos at your chosen quality (e.g. 1080p, 720p, 480p)
- Download entire YouTube playlists into an organized folder
- Web UI via Streamlit — no terminal needed
- CLI mode for quick local use
- Automatically detects available MP4 qualities for a video
- Supports local `ffmpeg` for video+audio merging
- Skips already-downloaded files in playlists via archive tracking
- Continues interrupted playlist downloads

## How the Program Works

Run either the CLI or the Streamlit web app — both share the same core logic from `main.py`.

- Paste in any YouTube URL (video or playlist)
- The app detects whether it's a single video or a playlist based on `list=` in the URL
- For videos: available MP4 qualities are fetched and you pick one before downloading
- For playlists: you specify a destination folder and the bot downloads all videos into it
- If `ffmpeg` is found locally at `./ffmpeg/bin/ffmpeg.exe`, it is used for merging streams

## Commands / Usage

### CLI Mode

Run the script directly:

```bash
python main.py
```

You will be prompted for:

| Prompt | Description |
|---|---|
| `Enter the url` | YouTube video or playlist URL |
| `Enter the destination path` | Local folder to save downloads |
| `Select quality` | Shown only for single videos — pick from available MP4 heights |
| `Enter the name of the folder for playlist` | Shown only for playlists |

**Example — Single Video:**
```
Enter the url: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter the destination path: C:/Downloads
Available qualities: [360, 720, 1080]
Select one: 720
Downloading: Rick Astley - Never Gonna Give You Up
```

**Example — Playlist:**
```
Enter the url: https://www.youtube.com/playlist?list=PLxxx
Enter the destination path: C:/Downloads
Enter the name of the folder for playlist: my_playlist
Downloading...
```

---

### Web App Mode

```bash
streamlit run webapp.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`).

- Paste a YouTube URL into the input field
- The video/playlist title is shown automatically
- For single videos: select quality from a dropdown and click **Download Video**
- For playlists: enter a folder name and click **Download Playlist**
- Download buttons appear for each file once complete

---
## How to Run Locally

### Prerequisites

- Python 3.10+
- `ffmpeg` (optional but recommended for merging video+audio streams)

### Setup

1. Clone the repository and navigate to the project folder.

2. Install dependencies:
```bash
   pip install yt-dlp streamlit
```

3. *(Optional)* Place `ffmpeg` at `./ffmpeg/bin/ffmpeg.exe` for local merging support.

---

### Option 1: Web App (Streamlit)

```bash
streamlit run webapp.py
```

---

### Option 2: CLI

```bash
python main.py
```

---

## File Structure

```bash
project/
│── main.py               
│── webapp.py
│── ffmpeg
│── packages.txt          
│── README.md
│── .python-version
│── pyproject.toml
│── uv.lock
```

---

## Technologies Used

- Python
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — YouTube download engine
- [Streamlit](https://streamlit.io/) — Web UI framework
- os module — File and path management

---

## Notes

- Quality selection is only available for single videos, not playlists (playlists always download at best available quality).
- `downloaded.txt` is auto-created during playlist downloads to avoid re-downloading files on resume.
- If `ffmpeg` is not available, some high-quality formats that require merging may not download correctly.
- Playlist downloads on Hugging Face Spaces use a temporary directory — files are served as individual download buttons in the browser.
- Large playlists may time out on free-tier Spaces due to resource limits.

---

## Author

Muhammad Awais Tariq

---

If you like this project, consider giving it a star ⭐