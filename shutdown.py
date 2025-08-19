import os
import platform
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def schedule_shutdown():
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())

        now = datetime.now()
        shutdown_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        if shutdown_time <= now:
            shutdown_time = shutdown_time.replace(day=now.day + 1)

        delay_seconds = int((shutdown_time - now).total_seconds())

        system_platform = platform.system()

        if system_platform == "Windows":
            os.system(f"shutdown /s /t {delay_seconds}")
        elif system_platform in ["Linux", "Darwin"]:  # Darwin = macOS
            minutes = max(1, delay_seconds // 60)
            os.system(f"sudo shutdown -h +{minutes}")
        else:
            messagebox.showerror("Error", "Unsupported OS")
            return

        messagebox.showinfo("Scheduled", 
            f"Shutdown scheduled for {shutdown_time.strftime('%Y-%m-%d %H:%M:%S')}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for hour and minute.")

def cancel_shutdown():
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("shutdown /a")
    elif system_platform in ["Linux", "Darwin"]:
        os.system("sudo shutdown -c")
    messagebox.showinfo("Cancelled", "Shutdown has been cancelled.")

# Create UI
root = tk.Tk()
root.title("Shutdown Scheduler")
root.geometry("300x200")

tk.Label(root, text="Hour (0-23):").pack(pady=5)
hour_entry = tk.Entry(root, width=10)
hour_entry.pack()

tk.Label(root, text="Minute (0-59):").pack(pady=5)
minute_entry = tk.Entry(root, width=10)
minute_entry.pack()

tk.Button(root, text="Schedule Shutdown", command=schedule_shutdown).pack(pady=10)
tk.Button(root, text="Cancel Shutdown", command=cancel_shutdown).pack()

root.mainloop()
