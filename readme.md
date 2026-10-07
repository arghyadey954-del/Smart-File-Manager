# 📂 Smart File Organizer

A simple, lightweight Python command-line utility that automatically organizes files into categorized folders based on their file extensions.

It works on **macOS and Windows** and is designed to make messy folders such as `Downloads`, `Desktop`, or custom directories easier to manage.

---

## ✨ Features

- 📁 Automatically categorizes files
- 🖼️ Supports images
- 📄 Supports documents
- 📊 Supports spreadsheets
- 📊 Supports presentations
- 🎵 Supports audio files
- 🎬 Supports video files
- 📦 Supports archive files
- 💻 Supports programming/code files
- 📂 Unknown file types are placed in `Others`
- 👀 **Dry Run** mode to preview changes before moving files
- 🛡️ Prevents overwriting existing files
- 🔢 Automatically renames duplicate files
- ⚠️ Handles permission and operating-system errors
- 🍎 Works on macOS
- 🪟 Works on Windows

---

## 🗂️ Supported File Categories

| Category | Examples |
|---|---|
| `Images` | JPG, JPEG, PNG, GIF, BMP, WEBP, SVG, TIFF |
| `Documents` | PDF, DOC, DOCX, TXT, ODT, RTF, MD |
| `Spreadsheets` | XLS, XLSX, CSV, ODS |
| `Presentations` | PPT, PPTX, ODP |
| `Audio` | MP3, WAV, FLAC, AAC, OGG, M4A |
| `Videos` | MP4, MKV, AVI, MOV, WMV, WEBM |
| `Archives` | ZIP, RAR, 7Z, TAR, GZ, BZ2 |
| `Code` | PY, JAVA, C, CPP, JS, TS, HTML, CSS, PHP, GO, RS, JSON |
| `Others` | Unsupported/unknown extensions |

---

# 🚀 Installation

## Requirements

You need:

- Python 3
- Terminal / Command Prompt
- The `organizer.py` file

No external Python packages are required.

---

# 🍎 macOS Installation

### 1. Check Python

Open **Terminal** and run:

```bash
python3 --version
```

You should see something similar to:

```text
Python 3.x.x
```

If Python is installed, you're ready.

### 2. Download or clone the project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Enter the project folder:

```bash
cd YOUR_REPOSITORY
```

You should see:

```text
organizer.py
README.md
LICENSE
```

---

# 🪟 Windows Installation

### 1. Check Python

Open **Command Prompt** or **PowerShell**:

```powershell
python --version
```

If that doesn't work, try:

```powershell
py --version
```

### 2. Clone the repository

```powershell
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Enter the project folder:

```powershell
cd YOUR_REPOSITORY
```

---

# ▶️ Usage

The basic command is:

### macOS

```bash
python3 organizer.py "PATH_TO_FOLDER"
```

### Windows

```powershell
python organizer.py "PATH_TO_FOLDER"
```

---

# 👀 Preview Before Organizing

It is strongly recommended to use **dry-run mode first**.

Dry-run shows what will happen without moving any files.

### macOS

```bash
python3 organizer.py "~/Downloads" --dry-run
```

### Windows

```powershell
python organizer.py "C:\Users\YourName\Downloads" --dry-run
```

Example output:

```text
🔎 Scanning folder...
---------------------------------------------
[DRY RUN] photo.jpg → Images/
[DRY RUN] resume.pdf → Documents/
[DRY RUN] song.mp3 → Audio/
[DRY RUN] movie.mp4 → Videos/
---------------------------------------------
👀 Dry run completed. No files were moved.
```

---

# 📦 Organize the Files

After checking the dry-run output, run the command without `--dry-run`.

### macOS

```bash
python3 organizer.py "~/Downloads"
```

### Windows

```powershell
python organizer.py "C:\Users\YourName\Downloads"
```

The program will create category folders automatically and move the files into them.

---

# 📁 Example

Before:

```text
Downloads/
├── photo.jpg
├── resume.pdf
├── music.mp3
├── movie.mp4
├── data.csv
├── project.py
└── archive.zip
```

After:

```text
Downloads/
├── Images/
│   └── photo.jpg
│
├── Documents/
│   └── resume.pdf
│
├── Audio/
│   └── music.mp3
│
├── Videos/
│   └── movie.mp4
│
├── Spreadsheets/
│   └── data.csv
│
├── Code/
│   └── project.py
│
└── Archives/
    └── archive.zip
```

---

# 🛡️ Duplicate File Protection

The organizer does not overwrite an existing file.

For example, if:

```text
Images/photo.jpg
```

already exists and another `photo.jpg` is moved into the folder, it will automatically create:

```text
Images/photo_1.jpg
```

If that also exists:

```text
Images/photo_2.jpg
```

This protects existing files from being overwritten.

---

# ⚠️ Important Notes

### Backup important files

Although the program is designed to safely move files, always keep backups of important data.

### Use Dry Run First

Before organizing an important folder:

```bash
python3 organizer.py "PATH_TO_FOLDER" --dry-run
```

On Windows:

```powershell
python organizer.py "PATH_TO_FOLDER" --dry-run
```

### Avoid system folders

Do not use the program on operating-system directories or folders containing critical system files.

Recommended folders include:

- Downloads
- Desktop
- Documents
- Personal project folders
- Custom test folders

---

# 🧪 Recommended First Test

Create a folder called:

```text
FileOrganizerTest
```

Put a few different files inside it:

```text
FileOrganizerTest/
├── photo.jpg
├── document.pdf
├── song.mp3
├── video.mp4
└── test.py
```

Then run:

### macOS

```bash
python3 organizer.py "~/Desktop/FileOrganizerTest" --dry-run
```

### Windows

```powershell
python organizer.py "C:\Users\YourName\Desktop\FileOrganizerTest" --dry-run
```

If everything looks correct, run it without `--dry-run`.

---

# 🧰 Project Structure

```text
Smart-File-Organizer/
│
├── organizer.py
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🔧 How It Works

The program:

1. Receives a folder path from the command line.
2. Checks whether the folder exists.
3. Finds files directly inside the selected folder.
4. Checks each file's extension.
5. Determines its category.
6. Creates the appropriate category folder.
7. Checks for duplicate filenames.
8. Moves the file.
9. Reports the result in the terminal.

---

# 💻 Command Reference

| Command | Purpose |
|---|---|
| `python3 organizer.py PATH` | Organize a folder on macOS/Linux |
| `python organizer.py PATH` | Organize a folder on Windows |
| `python3 organizer.py PATH --dry-run` | Preview on macOS/Linux |
| `python organizer.py PATH --dry-run` | Preview on Windows |

---

# 🤝 Contributing

Contributions are welcome.

You can:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the changes.
5. Submit a Pull Request.

---

# 📜 License

This project is released under the **MIT License**.

See the `LICENSE` file for details.

---

# 👨‍💻 Author

**Arghya Kamal Dey**

Built with ❤️ using Python.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
