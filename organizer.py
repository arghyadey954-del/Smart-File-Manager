import os
import shutil
import argparse
from pathlib import Path
from datetime import datetime


FILE_CATEGORIES = {
    "Images": {
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".svg", ".tiff"
    },
    "Documents": {
        ".pdf", ".doc", ".docx", ".txt", ".odt",
        ".rtf", ".md"
    },
    "Spreadsheets": {
        ".xls", ".xlsx", ".csv", ".ods"
    },
    "Presentations": {
        ".ppt", ".pptx", ".odp"
    },
    "Audio": {
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"
    },
    "Videos": {
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".webm"
    },
    "Archives": {
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"
    },
    "Code": {
        ".py", ".java", ".c", ".cpp", ".js", ".ts",
        ".html", ".css", ".php", ".go", ".rs", ".json"
    }
}


def get_category(file_path):
    """Return the category based on file extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    """Prevent overwriting an existing file."""
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_destination = destination.parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_folder(folder_path, dry_run=False):
    """Organize files inside the selected folder."""

    folder = Path(folder_path)

    if not folder.exists():
        print("❌ Folder does not exist.")
        return

    if not folder.is_dir():
        print("❌ The provided path is not a folder.")
        return

    files = [
        item for item in folder.iterdir()
        if item.is_file()
    ]

    if not files:
        print("📂 No files found to organize.")
        return

    moved_count = 0

    print("\n🔎 Scanning folder...")
    print("-" * 45)

    for file_path in files:
        category = get_category(file_path)

        category_folder = folder / category
        destination = category_folder / file_path.name

        destination = get_unique_destination(destination)

        if dry_run:
            print(
                f"[DRY RUN] {file_path.name} "
                f"→ {category}/"
            )
            continue

        try:
            category_folder.mkdir(
                parents=True,
                exist_ok=True
            )

            shutil.move(
                str(file_path),
                str(destination)
            )

            print(
                f"✓ {file_path.name} "
                f"→ {category}/"
            )

            moved_count += 1

        except PermissionError:
            print(
                f"⚠ Permission denied: "
                f"{file_path.name}"
            )

        except OSError as error:
            print(
                f"⚠ Could not move "
                f"{file_path.name}: {error}"
            )

    print("-" * 45)

    if dry_run:
        print("👀 Dry run completed. No files were moved.")
    else:
        print(
            f"✅ Successfully organized "
            f"{moved_count} file(s)."
        )

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        print(f"🕒 Completed: {timestamp}")


def main():
    parser = argparse.ArgumentParser(
        description="Smart File Organizer - "
                    "Automatically organize files by type."
    )

    parser.add_argument(
        "folder",
        help="Path of the folder to organize"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without moving files"
    )

    args = parser.parse_args()

    organize_folder(
        args.folder,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()