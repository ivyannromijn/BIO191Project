from tkinter import *

def show_text():
  # Update the label text to show the message
  search_result_label.config(text="Search results will appear here!")

root = Tk()

# Create the search button
search_button = Button(root, text="Search", command=show_text)
search_button.pack(pady=10)

# Create an empty label for search results (initially hidden)
search_result_label = Label(root, text="")
search_result_label.pack()

root.mainloop()
