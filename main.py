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
    download_btn.config(state='disabled')
    progress_bar.start()
    
    def download_thread():
        try:
            update_status("Preparing download...")
            
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

            update_status("Downloading and converting audio...")
            subprocess.run(cmd, check=True)
            
            update_status("Download completed successfully!")
            messagebox.showinfo("Success", f"Download completed and saved to:\n{path}")
            
        except subprocess.CalledProcessError as e:
            update_status("Download failed - check URL or yt-dlp setup")
            messagebox.showerror("Error", "Download failed. Check the URL or yt-dlp setup.")
        except Exception as e:
            update_status(f"Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            # Re-enable download button and stop progress bar
            download_btn.config(state='normal')
            progress_bar.stop()
    
    # Run download in separate thread to prevent UI freezing
    thread = threading.Thread(target=download_thread)
    thread.daemon = True
    thread.start()

# GUI Setup
root = tk.Tk()
root.title("YouTube Audio Downloader")
root.geometry("800x600")
root.configure(bg='#f0f0f0')

# Configure style
style = ttk.Style()
style.theme_use('clam')

# Main container
main_frame = tk.Frame(root, bg='#f0f0f0', padx=30, pady=20)
main_frame.pack(fill='both', expand=True)

# Title
title_label = tk.Label(main_frame, text="YouTube Audio Downloader", 
                      font=('Helvetica', 18, 'bold'), 
                      bg='#f0f0f0', fg='#333333')
title_label.pack(pady=(0, 30))

# URL Section
url_frame = tk.Frame(main_frame, bg='#f0f0f0')
url_frame.pack(fill='x', pady=(0, 20))

tk.Label(url_frame, text="YouTube URL:", 
         font=('Helvetica', 12, 'bold'), 
         bg='#f0f0f0', fg='#333333').pack(anchor='w')

url_entry = tk.Entry(url_frame, width=70, font=('Helvetica', 11), 
                    relief='solid', bd=1, highlightthickness=1,
                    highlightcolor='#4a90e2')
url_entry.pack(fill='x', pady=(5, 0), ipady=8)

# Format Section
format_frame = tk.Frame(main_frame, bg='#f0f0f0')
format_frame.pack(fill='x', pady=(0, 20))

tk.Label(format_frame, text="Audio Format:", 
         font=('Helvetica', 12, 'bold'), 
         bg='#f0f0f0', fg='#333333').pack(anchor='w')

format_var = tk.StringVar(value="mp3")
format_menu = ttk.Combobox(format_frame, textvariable=format_var, 
                          values=["mp3", "wav", "flac", "m4a"], 
                          state="readonly", font=('Helvetica', 11))
format_menu.pack(anchor='w', pady=(5, 0))

# Output Path Section
path_frame = tk.Frame(main_frame, bg='#f0f0f0')
path_frame.pack(fill='x', pady=(0, 20))

tk.Label(path_frame, text="Save To Folder:", 
         font=('Helvetica', 12, 'bold'), 
         bg='#f0f0f0', fg='#333333').pack(anchor='w')

path_input_frame = tk.Frame(path_frame, bg='#f0f0f0')
path_input_frame.pack(fill='x', pady=(5, 0))

output_path = tk.StringVar()
path_entry = tk.Entry(path_input_frame, textvariable=output_path, 
                     font=('Helvetica', 11), relief='solid', bd=1,
                     highlightthickness=1, highlightcolor='#4a90e2')
path_entry.pack(side='left', fill='x', expand=True, ipady=8)

browse_btn = tk.Button(path_input_frame, text="Browse", command=browse_folder,
                      font=('Helvetica', 10, 'bold'), bg='#e6e6e6', fg='#333333',
                      relief='solid', bd=1, padx=20, pady=8,
                      activebackground='#d6d6d6')
browse_btn.pack(side='right', padx=(10, 0))

# Download Button
download_btn = tk.Button(main_frame, text="Download", command=download_audio,
                        font=('Helvetica', 14, 'bold'), bg='#4a90e2', fg='white',
                        relief='solid', bd=0, padx=40, pady=12,
                        activebackground='#357abd', cursor='hand2')
download_btn.pack(pady=(20, 20))

# Progress Bar
progress_bar = ttk.Progressbar(main_frame, mode='indeterminate', length=400)
progress_bar.pack(pady=(0, 10))

# Status Section
status_frame = tk.Frame(main_frame, bg='#f0f0f0')
status_frame.pack(fill='both', expand=True)

tk.Label(status_frame, text="Status:", 
         font=('Helvetica', 12, 'bold'), 
         bg='#f0f0f0', fg='#333333').pack(anchor='w')

status_text = tk.Text(status_frame, height=8, font=('Consolas', 10),
                     bg='#ffffff', fg='#333333', relief='solid', bd=1,
                     wrap='word', state='disabled')
status_text.pack(fill='both', expand=True, pady=(5, 0))

# Initialize status
update_status("Ready to download. Enter a YouTube URL and select your preferences.")

root.mainloop()
