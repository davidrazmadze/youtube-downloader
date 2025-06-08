# 🎵 YouTube Audio Downloader

A sleek, modern desktop application for downloading high-quality audio from YouTube videos with an intuitive black and red themed GUI.

![YouTube Audio Downloader](screenshot.png)

## ✨ Features

- **Modern Dark UI**: Sleek black and red interface design
- **High-Quality Downloads**: Extract audio in multiple formats (MP3, WAV, FLAC, M4A, AAC)
- **Real-time Status**: Live progress updates and status messages
- **Background Processing**: Non-blocking downloads with progress indication
- **Default Desktop Save**: Automatically sets save location to Desktop
- **Easy Folder Selection**: Browse and select custom download directories
- **Error Handling**: Comprehensive error messages and status updates

## 🔧 Prerequisites

Before running the application, ensure you have the following installed:

### 1. Python 3.7+

```bash
# Check your Python version
python3 --version
```

### 2. yt-dlp

```bash
# Install yt-dlp using pip
pip3 install yt-dlp

# Or using Homebrew (macOS)
brew install yt-dlp

# Or download binary from: https://github.com/yt-dlp/yt-dlp/releases
```

### 3. FFmpeg (Required for audio conversion)

```bash
# macOS (using Homebrew)
brew install ffmpeg

# Ubuntu/Debian
sudo apt update
sudo apt install ffmpeg

# Windows (using Chocolatey)
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

## 📥 Installation

1. **Clone or download** this repository

```bash
git clone <repository-url>
cd youtube-downloader
```

2. **Verify dependencies** are installed

```bash
# Test yt-dlp
yt-dlp --version

# Test ffmpeg
ffmpeg -version
```

3. **Run the application**

```bash
python3 main.py
```

## 🚀 How to Use

### Basic Usage

1. **Launch the Application**

   ```bash
   python3 main.py
   ```

2. **Enter YouTube URL**

   - Paste any YouTube video URL in the "YouTube URL" field
   - Supports various URL formats:
     - `https://www.youtube.com/watch?v=VIDEO_ID`
     - `https://youtu.be/VIDEO_ID`
     - `https://m.youtube.com/watch?v=VIDEO_ID`

3. **Select Audio Format**

   - Choose from: MP3, WAV, FLAC, M4A, AAC
   - MP3 is selected by default (most compatible)

4. **Choose Save Location**

   - Default: `~/Desktop`
   - Click "Browse" to select a different folder

5. **Download**
   - Click the red "🚀 Download Audio" button
   - Monitor progress in the status section
   - Wait for completion message

### Status Messages

- 🚀 **Ready**: Application is ready for input
- 🔍 **Analyzing**: Processing the YouTube URL
- ⬇️ **Downloading**: Downloading and converting audio
- ✅ **Success**: Download completed successfully
- ❌ **Error**: Something went wrong (check URL or setup)

## 🎨 Interface Overview

The application features a modern dark theme with:

- **Header Section**: Application title and subtitle
- **URL Input**: Large text field for YouTube URLs
- **Format Selection**: Dropdown menu for audio formats
- **Save Location**: Path display with browse button
- **Download Button**: Prominent red download button
- **Progress Bar**: Visual download progress indicator
- **Status Area**: Real-time status updates and messages

## 🔧 Troubleshooting

### Common Issues

#### 1. "yt-dlp not found" error

```bash
# Install yt-dlp
pip3 install yt-dlp

# Or update if already installed
pip3 install --upgrade yt-dlp
```

#### 2. "ffmpeg not found" error

- Install FFmpeg (see Prerequisites section)
- Ensure FFmpeg is in your system PATH

#### 3. Download fails with network error

- Check your internet connection
- Verify the YouTube URL is valid and accessible
- Some videos may be region-restricted or private

#### 4. "Permission denied" error

- Check write permissions for the selected download folder
- Try selecting a different download directory

#### 5. Application won't start

- Ensure Python 3.7+ is installed
- Check that tkinter is available (usually included with Python)

### Advanced Troubleshooting

#### Update yt-dlp

```bash
# Update to latest version
pip3 install --upgrade yt-dlp

# Check version
yt-dlp --version
```

#### Test yt-dlp manually

```bash
# Test download (audio only)
yt-dlp -f bestaudio -x --audio-format mp3 "https://youtu.be/VIDEO_ID"
```

## 📋 Supported Formats

| Format   | Quality   | Compatibility | File Size |
| -------- | --------- | ------------- | --------- |
| **MP3**  | Good      | Excellent     | Medium    |
| **WAV**  | Excellent | Good          | Large     |
| **FLAC** | Excellent | Good          | Large     |
| **M4A**  | Very Good | Very Good     | Medium    |
| **AAC**  | Very Good | Very Good     | Small     |

## 🖥️ System Requirements

- **Operating System**: macOS, Linux, Windows
- **Python**: 3.7 or higher
- **Memory**: 100MB+ available RAM
- **Storage**: 50MB+ for application, additional space for downloads
- **Network**: Internet connection for downloads

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## ⚠️ Disclaimer

This application is for personal use only. Please respect YouTube's Terms of Service and copyright laws. Only download content you have permission to download.

## 📞 Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all dependencies are properly installed
3. Verify the YouTube URL is valid and accessible
4. Check your internet connection and permissions

---

**Enjoy downloading high-quality audio from YouTube! 🎵**
