## File Organizer

A simple Python command-line application that organizes files in a selected directory based on their file extensions.

### Features

- Validates the directory path
- Categorizes files by extension
- Creates category folders automatically
- Moves files into the appropriate folders
- Places unknown file types in `Others`
- Handles file-related errors
- Displays a summary after organizing

### Categories

- Images: `.jpg`, `.jpeg`, `.png`, `.bmp`
- Documents: `.pdf`, `.doc`, `.docx`, `.txt`
- Audio: `.mp3`, `.wav`
- Videos: `.mp4`, `.mov`
- Programming Languages: `.py`, `.js`, `.java`, `.cs`, `.cpp`, `.html`, `.css`
- Others: other file types

### How to Run

```bash
python main.py

Then enter the path of the directory you want to organize.

```markdown
### Technologies

- Python
- pathlib
- shutil