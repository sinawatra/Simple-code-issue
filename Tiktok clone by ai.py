import tkinter as tk

def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("TikTok Clone")
    
    # Create the widgets
    title_label = tk.Label(window, text="TikTok Clone", font=("Arial", 24))
    title_label.pack(pady=20)
    
    video_frame = tk.Frame(window, width=640, height=480, bg="black")
    video_frame.pack(pady=10)
    
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)
    
    like_button = tk.Button(button_frame, text="Like", padx=10, pady=5)
    like_button.grid(row=0, column=0, padx=5)
    
    comment_button = tk.Button(button_frame, text="Comment", padx=10, pady=5)
    comment_button.grid(row=0, column=1, padx=5)
    
    share_button = tk.Button(button_frame, text="Share", padx=10, pady=5)
    share_button.grid(row=0, column=2, padx=5)
    
    # Run the GUI
    window.mainloop()

# Create the GUI
create_gui()
