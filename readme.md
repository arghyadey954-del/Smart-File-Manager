# 📂 Smart File Manager

**Smart File Manager** is a lightweight Python-based file organization tool that automatically sorts files into categorized folders based on their file extensions.

Built to keep folders like **Downloads, Desktop, and personal project directories** clean and organized.

## ✨ Features

- 📁 Automatic file organization
- 🖼️ Image categorization
- 📄 Document categorization
- 📊 Spreadsheet categorization
- 🎞️ Presentation categorization
- 🎵 Audio categorization
- 🎬 Video categorization
- 📦 Archive categorization
- 💻 Code file categorization
- 📂 Unknown files → `Others`
- 👀 Dry-run mode to preview changes
- 🛡️ Duplicate file protection
- 🍎 macOS support
- 🪟 Windows support

## 🛠️ Tech Stack

- **Python 3**
- `pathlib`
- `shutil`
- `argparse`

No external Python packages are required.

## 📂 Project Structure

```text
Smart-File-Manager/
│
├── organizer.py
├── README.md
├── LICENSE
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Smart-File-Manager.git
cd Smart-File-Manager
```

### 2. Check Python

**macOS:**

```bash
python3 --version
```

**Windows:**

```bash
python --version
```

Python 3.x is recommended.

## ▶️ Usage

### macOS

```bash
python3 organizer.py "/path/to/folder"
```

### Windows

```bash
python organizer.py "C:\path\to\folder"
```

## 👀 Preview Changes

Before moving files, you can use **Dry Run** mode.

### macOS

```bash
python3 organizer.py "/path/to/folder" --dry-run
```

### Windows

```bash
python organizer.py "C:\path\to\folder" --dry-run
```

Dry Run shows which files will be moved without actually moving them.

## 📁 Example

### Before

```text
Downloads/
├── photo.jpg
├── resume.pdf
├── song.mp3
├── movie.mp4
├── data.csv
└── project.py
```

### After

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── movie.mp4
├── Spreadsheets/
│   └── data.csv
└── Code/
    └── project.py
```

## 🛡️ Duplicate Protection

Smart File Manager prevents existing files from being overwritten.

If a file with the same name already exists, the program automatically generates a unique filename such as:

```text
photo.jpg
photo_1.jpg
photo_2.jpg
```

## ⚠️ Recommendation

Use `--dry-run` before organizing important folders.

Always keep backups of important files.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Test the project
5. Submit a Pull Request

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Arghya Kamal Dey**

Made with Python.
