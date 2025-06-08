import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os
import threading

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        output_path.set(folder_selected)

def update_status(message):
    status_text.config(state='normal')
    status_text.delete(1.0, tk.END)
    status_text.insert(tk.END, message)
    status_text.config(state='disabled')
    root.update()

def download_audio():
    url = url_entry.get().strip()
    fmt = format_var.get()
    path = output_path.get().strip()

    if not url or not path:
        messagebox.showwarning("Missing Input", "Please provide both a URL and a save location.")
        return

    # Disable download button during download
    download_btn.config(state='disabled', bg='#666666')
    progress_bar.start()
    
    def download_thread():
        try:
            update_status("🔍 Analyzing video and preparing download...")
            
            # Construct output template
            output_template = os.path.join(path, "%(title)s.%(ext)s")

            # Build yt-dlp command
            cmd = [
                "yt-dlp",
                "-f", "bestaudio",
                "-x",
                "--audio-format", fmt,
                "--audio-quality", "0",
                "-o", output_template,
                url
            ]

            update_status("⬇️ Downloading and converting audio...")
            subprocess.run(cmd, check=True)
            
            update_status("✅ Download completed successfully!")
            messagebox.showinfo("Success", f"🎉 Download completed and saved to:\n{path}")
            
        except subprocess.CalledProcessError as e:
            update_status("❌ Download failed - check URL or yt-dlp setup")
            messagebox.showerror("Error", "Download failed. Check the URL or yt-dlp setup.")
        except Exception as e:
            update_status(f"❌ Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            # Re-enable download button
            download_btn.config(state='normal', bg='#ef4444')
            progress_bar.stop()
    
    # Run download in separate thread to prevent UI freezing
    thread = threading.Thread(target=download_thread)
    thread.daemon = True
    thread.start()

# GUI Setup
root = tk.Tk()
root.title("YouTube Audio Downloader")
root.geometry("1100x900")
root.configure(bg='#0a0a0a')

# Configure style for ttk widgets
style = ttk.Style()
style.theme_use('clam')
style.configure('Dark.TCombobox', 
                fieldbackground='#2a2a2a', 
                background='#2a2a2a',
                foreground='#ffffff',
                arrowcolor='#ffffff',
                bordercolor='#444444',
                lightcolor='#2a2a2a',
                darkcolor='#2a2a2a',
                focuscolor='#22c55e')
style.map('Dark.TCombobox',
          fieldbackground=[('readonly', '#2a2a2a')],
          selectbackground=[('readonly', '#22c55e')],
          selectforeground=[('readonly', '#ffffff')])


# Main container
main_frame = tk.Frame(root, bg='#0a0a0a', padx=35, pady=25)
main_frame.pack(fill='both', expand=True)

# Header with gradient effect
header_frame = tk.Frame(main_frame, bg='#1a1a1a', height=120, relief='flat')
header_frame.pack(fill='x', pady=(0, 25))
header_frame.pack_propagate(False)

title_label = tk.Label(header_frame, text="YouTube Audio Downloader", 
                      font=('Segoe UI', 26, 'bold'), 
                      bg='#1a1a1a', fg='#ffffff')
title_label.pack(expand=True, pady=(15, 5))

subtitle_label = tk.Label(header_frame, text="High-Quality Audio Downloads", 
                         font=('Segoe UI', 12), 
                         bg='#1a1a1a', fg='#dc2626')
subtitle_label.pack(pady=(0, 15))

# URL Section
url_frame = tk.Frame(main_frame, bg='#1a1a1a', relief='flat')
url_frame.pack(fill='x', pady=(0, 20), ipady=20, ipadx=25)

url_label = tk.Label(url_frame, text="🔗 YouTube URL", 
         font=('Segoe UI', 14, 'bold'), 
         bg='#1a1a1a', fg='#dc2626')
url_label.pack(anchor='w', pady=(0, 10))

url_entry = tk.Entry(url_frame, font=('Segoe UI', 12), 
                    relief='flat', bd=0, highlightthickness=2,
                    highlightcolor='#dc2626', highlightbackground='#444444',
                    bg='#2a2a2a', fg='#ffffff', insertbackground='#ffffff')
url_entry.pack(fill='x', ipady=12)

# Format Section
format_frame = tk.Frame(main_frame, bg='#1a1a1a', relief='flat')
format_frame.pack(fill='x', pady=(0, 20), ipady=20, ipadx=25)

format_label = tk.Label(format_frame, text="🎵 Audio Format", 
         font=('Segoe UI', 14, 'bold'), 
         bg='#1a1a1a', fg='#dc2626')
format_label.pack(anchor='w', pady=(0, 10))

format_var = tk.StringVar(value="mp3")
format_menu = ttk.Combobox(format_frame, textvariable=format_var, 
                          values=["mp3", "wav", "flac", "m4a", "aac"], 
                          state="readonly", font=('Segoe UI', 12),
                          style='Dark.TCombobox', width=20)
format_menu.pack(anchor='w')

# Output Path Section
path_frame = tk.Frame(main_frame, bg='#1a1a1a', relief='flat')
path_frame.pack(fill='x', pady=(0, 25), ipady=20, ipadx=25)

path_label = tk.Label(path_frame, text="📁 Save Location", 
         font=('Segoe UI', 14, 'bold'), 
         bg='#1a1a1a', fg='#dc2626')
path_label.pack(anchor='w', pady=(0, 10))

path_input_frame = tk.Frame(path_frame, bg='#1a1a1a')
path_input_frame.pack(fill='x')

output_path = tk.StringVar()
# Set default to Desktop
desktop_path = os.path.expanduser("~/Desktop")
output_path.set(desktop_path)

path_entry = tk.Entry(path_input_frame, textvariable=output_path, 
                     font=('Segoe UI', 12), relief='flat', bd=0,
                     highlightthickness=2, highlightcolor='#dc2626',
                     highlightbackground='#444444', bg='#2a2a2a', 
                     fg='#ffffff', insertbackground='#ffffff')
path_entry.pack(side='left', fill='x', expand=True, ipady=12)

browse_btn = tk.Button(path_input_frame, text="Browse", command=browse_folder,
                      font=('Segoe UI', 11, 'bold'), bg='#444444', fg='#ffffff',
                      relief='flat', bd=0, padx=25, pady=12,
                      activebackground='#555555', cursor='hand2')
browse_btn.pack(side='right', padx=(15, 0))

# Download Button - Main CTA
download_btn = tk.Button(main_frame, text="🚀 Download Audio", command=download_audio,
                        font=('Segoe UI', 16, 'bold'), bg='#ef4444', fg='#ffffff',
                        relief='flat', bd=0, padx=60, pady=18,
                        activebackground='#dc2626', cursor='hand2')
download_btn.pack(pady=(5, 20))

# Progress Bar
progress_bar = ttk.Progressbar(main_frame, mode='indeterminate', length=500)
progress_bar.pack(pady=(0, 20))

# Status Section
status_frame = tk.Frame(main_frame, bg='#1a1a1a', relief='flat')
status_frame.pack(fill='both', expand=True, ipady=20, ipadx=25)

status_label = tk.Label(status_frame, text="📊 Status", 
         font=('Segoe UI', 14, 'bold'), 
         bg='#1a1a1a', fg='#dc2626')
status_label.pack(anchor='w', pady=(0, 10))

status_text = tk.Text(status_frame, height=6, font=('JetBrains Mono', 11),
                     bg='#0a0a0a', fg='#ffffff', relief='flat', bd=0,
                     wrap='word', state='disabled', insertbackground='#ffffff',
                     selectbackground='#dc2626', selectforeground='#ffffff')
status_text.pack(fill='both', expand=True)

# Initialize status
update_status("🚀 Ready to download! Paste a YouTube URL above and hit Download.")

# Add hover effects
def on_enter_download(event):
    download_btn.config(bg='#dc2626')

def on_leave_download(event):
    if download_btn['state'] != 'disabled':
        download_btn.config(bg='#ef4444')

def on_enter_browse(event):
    browse_btn.config(bg='#555555')

def on_leave_browse(event):
    browse_btn.config(bg='#444444')

download_btn.bind("<Enter>", on_enter_download)
download_btn.bind("<Leave>", on_leave_download)
browse_btn.bind("<Enter>", on_enter_browse)
browse_btn.bind("<Leave>", on_leave_browse)

root.mainloop()
