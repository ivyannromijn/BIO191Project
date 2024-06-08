# from tkinter import Tk, ttk, filedialog, Text
# import tkinter


# def open_fasta():
#     global search_button, radio_var  # Declare search_button and radio_var globally

#     """Opens a FASTA file and displays its content in the text area."""
#     filename = filedialog.askopenfilename(title="Open FASTA File", filetypes=[("FASTA/FNA files", "*.fasta;*.fna")])
#     if filename:
#         try:
#             with open(filename, "r") as fasta_file:
#                 fasta_data = fasta_file.read()
#                 fasta_text.delete("1.0", tkinter.END)
#                 fasta_text.insert("1.0", fasta_data)

#             # Enable search button and create radio buttons
#             search_button.state(['!disabled'])
#             create_radio_buttons()

#         except FileNotFoundError:
#             print("File not found!")


# def create_radio_buttons():
#     global radio_var  # Access the global variable

#     # Frame to hold the radio buttons
#     radio_frame = ttk.Frame(root)
#     radio_frame.pack(padx=5, pady=5)

#     radio_var = tkinter.StringVar()  # Create a StringVar for radio button selection

#     # Define radio button labels and values
#     radio_options = [
#         ("gyrA", "value1"),
#         ("msrA_1", "value2"),
#         ("msrA_2", "value3"),
#         ("msrB", "value4"),
#     ]

#     for text, value in radio_options:
#         radio_button = ttk.Radiobutton(
#             radio_frame, text=text, variable=radio_var, value=value
#         )
#         radio_button.pack(anchor=tkinter.W)  # Pack radio buttons horizontally

#     # Add functionality to the search button based on radio button selection
#     def search_based_on_selection():
#         selected_option = radio_var.get()
#         # Implement your search logic here using the selected option and FASTA data
#         print(f"Search using option: {selected_option}")

#     search_button.config(command=search_based_on_selection)


# root = Tk()
# root.title("FASTA File Viewer")

# # Left side for FASTA data
# fasta_text = Text(root)
# fasta_text.pack(fill=tkinter.BOTH, expand=True, side=tkinter.LEFT)  # Use tkinter.BOTH

# # Button to open FASTA file
# open_button = ttk.Button(root, text="Open FASTA File", command=open_fasta)
# open_button.pack(padx=5, pady=5)

# # Initially disabled search button
# search_button = ttk.Button(root, text="Search", state='disabled')
# search_button.pack(padx=5, pady=5)

# # Global variable for radio button selection (initially set to None)
# radio_var = None

# root.mainloop()


