# 📸 Live Photo Merger

⚡ *Quick Start (Lazy Mode)*  
1. [Download latest release](../../releases)  
2. Run live_photo_merger.exe  
3. Select: *Image folder → Video folder → Output folder*  
4. Click *Start Merge* → Done 🎉  

---

## ✨ Features
- 🔄 Automatically pairs *photos & videos* by filename  
- 📂 Recursively scans subfolders  
- 🖼 Converts images to *JPG* (for Apple Photos)  
- 🎥 Converts videos to *MOV* (for Apple Photos)  
- 🗂 Organizes into:  
  - merged/ → paired Live Photos  
  - unmerged_images/ → leftover images  
  - unmerged_videos/ → leftover videos  
- ⚡ *FFmpeg auto-download* (no setup needed)  
- ✅ Options:  
  - Copy merged pairs  
  - Copy unmerged files  
  - Delete originals after merge  

---

## 📂 Included Files
- requirements.bat → installs required Python packages  
- live_photo_merger.py → full source code  
- live_photo_merger.exe → ready-to-use Windows app (no terminal needed)  

---

## 🚀 Usage
1. Run live_photo_merger.exe  
2. Select your *Image Folder, **Video Folder, and **Output Folder*  
3. Choose options (copy merged, copy unmerged, delete originals)  
4. Click *Start Merge*  
5. Finished Live Photos will be in the merged/ folder  

---

## ⚠ Notes
- Ensure filenames match between photos/videos (e.g., IMG_1234.JPG ↔ IMG_1234.MP4)  
- Unpaired files will be copied separately if enabled  
- Supports: .JPG, .JPEG, .PNG, .MP4, .MOV  

---

## ☕ Support Development
If this tool saved you time, consider buying me a coffee ❤  

*USDT (TRC20)*:  
TQtJAPn2Bsr8CZLnVBjDMnqWgyUzrwphjg

---

## 📚 Related Tools
- [Google-Photos-Media-JSON-Merger](https://github.com/0XJOEX0/Google-Photos-Media-JSON-Merger)  

- [Media-Sorter-Pro-Plus](https://github.com/0XJOEX0/media-sorter-pro-plus)
-----------------------------
Upload Without a Mac

Option A: iCloud Web (Easiest)
	1.	Go to iCloud.com/photos.
	2.	Log in with your Apple ID.
	3.	Click the Upload button (top-right).
	4.	Select everything in your merged/ folder.
	5.	Wait for upload → photos & videos will appear in the iPhone/iPad Photos app as Live Photos.

⸻

Option B: iCloud for Windows
	1.	Install iCloud for Windows.
	2.	Sign in with your Apple ID.
	3.	Enable iCloud Photos in the settings.
	4.	Copy your merged/ folder into the iCloud Photos > Uploads folder in File Explorer.
	5.	They’ll sync automatically.

⸻

Option C: iPhone/iPad Direct Import
	1.	Transfer the merged/ folder to your iPhone/iPad (via USB, AirDrop-like tools, or cloud storage).
	2.	Open the Files app.
	3.	Select the JPG + MOV pairs → Share → Save to Photos.
	4.	They’ll appear as Live Photos inside Apple Photos.

⸻

✅ Important Notes
	•	Apple Photos requires JPG + MOV pairs with the same filename (IMG_1234.JPG + IMG_1234.MOV) → your tool already handles this.
	•	JSON files from Google Photos are not needed for Apple Photos.
	•	Large uploads (tens of GBs) are usually smoother with iCloud for Windows instead of iCloud web.
