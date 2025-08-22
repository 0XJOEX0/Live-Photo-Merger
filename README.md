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

🚀 How to Upload Merged Live Photos to Apple Photos (Without macOS)

Once you’ve used Live Photo Merger to create .JPG + .MOV pairs in the merged/ folder, follow one of these methods to upload them into Apple Photos (iCloud Photos).

⸻

Method 1: iCloud Web (Easiest, Works Anywhere)
	1.	Open a web browser and go to iCloud.com/photos.
	2.	Sign in with your Apple ID.
	3.	Click the Upload button (top-right).
	4.	Select all files in your merged/ folder.
	5.	Wait for the upload to finish → your Live Photos will appear in the Photos app on iPhone/iPad.

⸻

Method 2: iCloud for Windows (Best for Large Uploads)
	1.	Download and install iCloud for Windows.
	2.	Open the app and sign in with your Apple ID.
	3.	In iCloud settings, check Photos → enable iCloud Photos.
	4.	Open File Explorer → find the iCloud Photos folder.
	5.	Copy your merged/ folder into the Uploads subfolder.
	6.	Files will sync automatically in the background.

⸻

Method 3: iPhone/iPad Direct Import
	1.	Transfer your merged/ folder to your iPhone/iPad (via cable, AirDrop-alternative, or cloud storage).
	2.	Open the Files app and locate the folder.
	3.	Select the .JPG + .MOV pairs.
	4.	Tap Share → choose Save to Photos.
	5.	The Live Photos will be added to your library and synced with iCloud (if enabled).

⸻

✅ Tips & Notes
	•	Make sure .JPG and .MOV filenames match exactly (e.g., IMG_1234.JPG ↔ IMG_1234.MOV).
	•	JSON files from Google Photos are not needed.
	•	For very large libraries, Method 2 (Windows app) is more stable than the iCloud website.

⸻

👉 After uploading, you’ll be able to browse, edit, and share your Live Photos in the Apple Photos app across all your devices.