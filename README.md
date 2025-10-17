# 📸 Sync RAWs with JPEGs

A lightweight Python tool to **keep only RAW files that have matching JPEGs** — perfect for photographers who shoot **RAW+JPEG** and later clean up their JPEGs.

## 🧩 Overview

After editing or deleting unwanted JPEGs, this script helps you automatically remove (or move) any **unmatched RAW files**.  
It works with the following folder structure:

YourPhotoFolder/
│
├── IMG_0001.JPG
├── IMG_0002.JPG
├── IMG_0003.JPG
│
└── RAW/
    ├── IMG_0001.CR2
    ├── IMG_0002.CR2
    ├── IMG_0004.CR2   ← deleted (no matching JPEG)

## ⚙️ Features

- ✅ Safe dry-run preview before any changes  
- 🧹 Option to delete or move unmatched RAWs  
- 📂 Works on any folder (you can even drag & drop)  
- 🪶 No external dependencies — pure Python  

## 🪄 Usage

1. Place your JPEGs in the root folder and your RAWs inside a subfolder named RAW.
2. Ensure these files are together:
   - sync_raws_with_jpegs.py
   - sync_raws_with_jpegs.bat
3. Run options:

Option A — In the photo folder
- Copy both files into your photo folder.
- Double-click sync_raws_with_jpegs.bat (it processes the current directory).

Option B — Drag & Drop
- Drag your photo folder onto sync_raws_with_jpegs.bat.
- It will process the dropped folder.

## ⚙️ Configuration

Inside sync_raws_with_jpegs.py, you can change:

move_unmatched = False  # Set True to move instead of delete
unmatched_folder_name = "_unmatched"  # Destination folder for moved RAWs

If move_unmatched is True, unmatched RAWs will be placed in RAW/_unmatched/

## 🧠 Example Output

📁 Working folder: D:\Photos\Vacation
📸 DRY RUN REPORT
Found 325 JPEGs
Found 330 RAWs
→ 325 will be kept
→ 5 will be deleted

Proceed with changes? (y/N): y

✅ Done! 5 RAW files deleted.

## 🧰 Requirements

- Python 3.7+
- Works on Windows, macOS, and Linux

## 🪶 Author

Created for photographers who like keeping things clean and organized.  
Simple, fast, and safe.
