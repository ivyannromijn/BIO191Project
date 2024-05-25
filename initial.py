import tkinter as tk
from tkinter import filedialog

def open_fasta():
  """Opens a file dialog and displays FASTA file contents in text widget."""
  filename = filedialog.askopenfilename(title="Select FASTA File", filetypes=[("FASTA files", "*.fasta")])
  if filename:
    try:
      with open(filename, 'r') as f:
        fasta_content = f.read()
      txt_content.delete(1.0, tk.END)
      txt_content.insert(tk.END, fasta_content)
    except FileNotFoundError:
      print("File not found!")

def run_fasta (filename):
  """Placeholder function for future functionality related to running the FASTA file."""
  # Add functionality related to processing or running the FASTA data here.
  # For now, it just prints a message
  print("Running FASTA file:", filename)

root = tk.Tk()
root.title("FASTA File Viewer")

# File selection button
btn_open = tk.Button(root, text="Open File", command=open_fasta)
btn_open.pack(side=tk.LEFT, pady=10)

# Run button (initially disabled)
btn_run = tk.Button(root, text="Run", state=tk.DISABLED, command=lambda: run_fasta(filename=""))
btn_run.pack(side=tk.LEFT, padx=(10, 0), pady=10)  # Add padding on the left side

# Text widget to display FASTA content
txt_content = tk.Text(root)
txt_content.pack(side=tk.LEFT, expand=True, fill=tk.Y)

# Update "Run" button state based on opened file
def update_run_button_state():
  # Enable "Run" button only if a file is loaded
  if filename:
    btn_run.config(state=tk.NORMAL)  # Enable button
  else:
    btn_run.config(state=tk.DISABLED)  # Disable button

filename = ""  # Keep track of opened filename

# Bind opening a file to update button state
root.bind("<ButtonRelease-1>", update_run_button_state)

# Main loop
root.mainloop()
