import os
import shutil
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import subprocess
import urllib.request
import zipfile
import sys

class LivePhotoMerger:
    def __init__(self, root):
        self.root = root
        self.root.title("📸 Live Photo Merger")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.jpg_dir = ""
        self.vid_dir = ""
        self.out_dir = ""
        self.running = False
        self.ffmpeg_path = os.path.join(os.path.dirname(sys.executable), "ffmpeg.exe") if getattr(sys, 'frozen', False) else "ffmpeg.exe"

        # Options
        self.opt_copy_merged = tk.BooleanVar(value=True)
        self.opt_copy_unmerged = tk.BooleanVar(value=True)
        self.opt_delete_originals = tk.BooleanVar(value=False)

        # UI
        self.create_widgets()
        self.ensure_ffmpeg()

    def create_widgets(self):
        frame_paths = tk.LabelFrame(self.root, text="Select Folders", padx=10, pady=10)
        frame_paths.pack(fill="x", padx=10, pady=5)
        tk.Button(frame_paths, text="📂 Select Image Folder", command=self.select_jpg).pack(fill="x", pady=3)
        tk.Button(frame_paths, text="📂 Select Video Folder", command=self.select_vid).pack(fill="x", pady=3)
        tk.Button(frame_paths, text="📂 Select Output Folder", command=self.select_out).pack(fill="x", pady=3)

        frame_opts = tk.LabelFrame(self.root, text="Options", padx=10, pady=10)
        frame_opts.pack(fill="x", padx=10, pady=5)
        tk.Checkbutton(frame_opts, text="Copy merged pairs", variable=self.opt_copy_merged).pack(anchor="w")
        tk.Checkbutton(frame_opts, text="Copy unmerged files", variable=self.opt_copy_unmerged).pack(anchor="w")
        tk.Checkbutton(frame_opts, text="Delete originals after merge", variable=self.opt_delete_originals).pack(anchor="w")

        frame_actions = tk.Frame(self.root)
        frame_actions.pack(fill="x", padx=10, pady=10)
        self.start_button = tk.Button(frame_actions, text="🚀 Start Merge", command=self.start_merge, bg="#4CAF50", fg="white")
        self.start_button.pack(side="left", expand=True, fill="x", padx=5)
        self.stop_button = tk.Button(frame_actions, text="🛑 Stop", command=self.stop_merge, state=tk.DISABLED, bg="#f44336", fg="white")
        self.stop_button.pack(side="left", expand=True, fill="x", padx=5)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=500, mode="determinate")
        self.progress.pack(pady=10)
        self.status_text = tk.Text(self.root, height=12, wrap="word", state="disabled")
        self.status_text.pack(fill="both", expand=True, padx=10, pady=5)

    # --- Folder Selection ---
    def select_jpg(self):
        self.jpg_dir = filedialog.askdirectory(title="Select Image Folder")
        if self.jpg_dir:
            self.log_status(f"📂 Image Folder: {self.jpg_dir}")

    def select_vid(self):
        self.vid_dir = filedialog.askdirectory(title="Select Video Folder")
        if self.vid_dir:
            self.log_status(f"📂 Video Folder: {self.vid_dir}")

    def select_out(self):
        self.out_dir = filedialog.askdirectory(title="Select Output Folder")
        if self.out_dir:
            self.log_status(f"📂 Output Folder: {self.out_dir}")

    # --- Logging & Progress ---
    def log_status(self, msg):
        self.status_text.config(state="normal")
        self.status_text.insert(tk.END, msg + "\n")
        self.status_text.see(tk.END)
        self.status_text.config(state="disabled")
        self.root.update_idletasks()

    def update_progress(self, value, maximum, msg=""):
        self.progress["maximum"] = maximum
        self.progress["value"] = value
        if msg:
            self.log_status(msg)
        self.root.update_idletasks()

    # --- Start/Stop ---
    def start_merge(self):
        if self.running:
            messagebox.showwarning("Warning", "Merge is already running!")
            return
        if not self.jpg_dir or not self.vid_dir or not self.out_dir:
            messagebox.showwarning("Warning", "Please select all folders first!")
            return
        self.running = True
        self.stop_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.log_status("🚀 Starting merge...")
        threading.Thread(target=self.merge_live_photos, daemon=True).start()

    def stop_merge(self):
        self.running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.log_status("🛑 Merge stopped by user.")

    # --- FFmpeg ---
    def ensure_ffmpeg(self):
        if not os.path.exists(self.ffmpeg_path):
            self.log_status("⬇ Downloading FFmpeg...")
            url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
            local_zip = os.path.join(os.path.dirname(sys.argv[0]), "ffmpeg.zip")
            urllib.request.urlretrieve(url, local_zip)
            with zipfile.ZipFile(local_zip, 'r') as zip_ref:
                for file in zip_ref.namelist():
                    if "bin/ffmpeg.exe" in file:
                        zip_ref.extract(file, os.path.dirname(sys.argv[0]))
                        shutil.move(os.path.join(os.path.dirname(sys.argv[0]), file), self.ffmpeg_path)
                        break
            os.remove(local_zip)
            self.log_status("✅ FFmpeg ready!")

    # --- Merge Logic ---
    def merge_live_photos(self):
        try:
            jpg_files = {}
            vid_files = {}
            for root_dir, _, files in os.walk(self.jpg_dir):
                for f in files:
                    if f.lower().endswith((".jpg", ".jpeg", ".png")):
                        name = os.path.splitext(f)[0]
                        jpg_files[name] = os.path.join(root_dir, f)
            for root_dir, _, files in os.walk(self.vid_dir):
                for f in files:
                    if f.lower().endswith((".mov", ".mp4")):
                        name = os.path.splitext(f)[0]
                        vid_files[name] = os.path.join(root_dir, f)

            total_files = len(jpg_files) + len(vid_files)
            processed = 0

            merged_dir = os.path.join(self.out_dir, "merged")
            unmerged_img_dir = os.path.join(self.out_dir, "unmerged_images")
            unmerged_vid_dir = os.path.join(self.out_dir, "unmerged_videos")
            os.makedirs(merged_dir, exist_ok=True)
            os.makedirs(unmerged_img_dir, exist_ok=True)
            os.makedirs(unmerged_vid_dir, exist_ok=True)

            matched = set()
            for name, jpg_path in jpg_files.items():
                if not self.running:
                    return
                if name in vid_files:
                    vid_path = vid_files[name]
                    try:
                        img = Image.open(jpg_path)
                        if img.mode != "RGB":
                            img = img.convert("RGB")
                        jpg_out_path = os.path.join(merged_dir, f"{name}.jpg")
                        img.save(jpg_out_path, "JPEG", quality=100)
                    except Exception as e:
                        self.log_status(f"⚠ Image error: {e}")
                        continue

                    vid_out_path = os.path.join(merged_dir, f"{name}.MOV")
                    try:
                        startupinfo = subprocess.STARTUPINFO()
                        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                        subprocess.run([self.ffmpeg_path, "-i", vid_path, "-c", "copy", vid_out_path], startupinfo=startupinfo)
                    except Exception as e:
                        self.log_status(f"⚠ Video error: {e}")
                        continue

                    if self.opt_delete_originals.get():
                        try:
                            os.remove(jpg_path)
                            os.remove(vid_path)
                        except:
                            pass
                    matched.add(name)
                    processed += 2
                    self.update_progress(processed, total_files, f"✅ Merged: {name}")

            # Unmerged files
            for name, jpg_path in jpg_files.items():
                if not self.running:
                    return
                if name not in matched and self.opt_copy_unmerged.get():
                    try:
                        img = Image.open(jpg_path)
                        if img.mode != "RGB":
                            img = img.convert("RGB")
                        jpg_out_path = os.path.join(unmerged_img_dir, f"{name}.jpg")
                        img.save(jpg_out_path, "JPEG", quality=100)
                        if self.opt_delete_originals.get():
                            os.remove(jpg_path)
                    except Exception as e:
                        self.log_status(f"⚠ Unmerged image error: {e}")
                    processed += 1
                    self.update_progress(processed, total_files, f"⚠ Unpaired image: {name}")

            for name, vid_path in vid_files.items():
                if not self.running:
                    return
                if name not in matched and self.opt_copy_unmerged.get():
                    vid_out_path = os.path.join(unmerged_vid_dir, f"{name}.MOV")
                    try:
                        startupinfo = subprocess.STARTUPINFO()
                        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                        subprocess.run([self.ffmpeg_path, "-i", vid_path, "-c", "copy", vid_out_path], startupinfo=startupinfo)
                        if self.opt_delete_originals.get():
                            os.remove(vid_path)
                    except Exception as e:
                        self.log_status(f"⚠ Unmerged video error: {e}")
                    processed += 1
                    self.update_progress(processed, total_files, f"⚠ Unpaired video: {name}")

            self.log_status("🎉 Merge complete!")
        except Exception as e:
            self.log_status(f"❌ Error: {e}")
        finally:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = LivePhotoMerger(root)
    root.mainloop()