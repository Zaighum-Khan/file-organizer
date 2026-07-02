# File Organizer

A simple command-line tool that automatically organizes files in a folder by type — sorting them into `Documents`, `Images`, `Videos`, `Audios`, `Archives`, or `Others` subfolders.

## Why

Messy folders (Downloads, Desktop, etc.) pile up with mixed file types over time. This tool cleans that up automatically, with zero setup beyond Python itself.

## Requirements

- Python 3.x (no external libraries needed — uses only built-in modules)

## How to Run

```bash
python3 organizer.py
```

You'll see a menu:

```
1. Organize Folder
2. Exit
Enter your choice:
```

Choose `1`, then enter the full path of the folder you want organized. You'll be asked to confirm before anything is moved.

## What It Does

Files are sorted based on extension:

| Folder      | Extensions |
|-------------|------------|
| Documents   | .pdf, .docx, .txt |
| Images      | .jpg, .png, .gif |
| Videos      | .mp4, .mov, .mkv, .avi |
| Audios      | .mp3, .wav, .ogg, .m4a |
| Archives    | .zip, .rar |
| Others      | anything else |

Subfolders are created automatically if they don't already exist. The script also skips itself if it's placed inside the target folder, and skips any folders (only moves files).

## Notes
