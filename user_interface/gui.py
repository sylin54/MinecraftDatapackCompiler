from tkinter import *
from tkinter import ttk
from tkinter import filedialog

# These functions take arbitrary *args
# because the Tkinter tutorial's function
# did. The tutorial didn't say why,
# but I assume there's a reason.

# VOID, changes file_path_in Tkinter variable
def browse_for_file_in(*args):
    """
    Opens system file dialog
    and assigns the user-selected
    file to file_path_in

    (which puts it in the entry box
    as well)
    """

    file_path_str = filedialog.askopenfilename(filetypes=[("Orthophosphate Files", "*.txt *.orph")])
    
    if file_path_str:
        pass
    else:
        file_path_str = "No file selected"
    file_path_in.set(file_path_str)

# VOID, changes file_path_out Tkinter variable
def browse_for_file_out(*args):
    """
    Opens system file dialog
    and assigns the user-selected
    directory to file_path_out

    (which puts it in the entry box
    as well)
    """

    file_path_str = filedialog.askdirectory()
    
    if file_path_str:
        pass
    else:
        file_path_str = "No file selected"
    file_path_out.set(file_path_str)

# VOID
def open_window(root):
    """
    Opens the GUI for
    choosing input and output
    paths; sets up
    file_path_in and file_path_out
    Tkinter variables
    """
    root.title("Orthophosphate")

    # Main grid
    (mainframe := ttk.Frame(root)).grid(column=0, row=0, sticky=NSEW)

    # Make everything stretch with the window if it is enlarged
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    for x in (1, 2, 3):
        for y in (1, 2, 3):
            mainframe.columnconfigure(x, weight=1)
            mainframe.rowconfigure(y)
    
    # Input button, entry, and labels
    global file_path_in
    ttk.Label(mainframe, text="Input File", justify="center").grid(column=1, row=1, columnspan=2, sticky=NSEW)
    ttk.Button(mainframe, text="Select file", command=browse_for_file_in).grid(column=1, row=2, sticky=EW)
    file_path_in = StringVar(value="No file selected")
    (file_path_entry := ttk.Entry(mainframe, textvariable=file_path_in, width=100)).grid(column=2, row=2, sticky=EW)

    # Output button, entry, and labels
    global file_path_out
    ttk.Label(mainframe, text="Output Directory", justify="center").grid(column=1, row=3, columnspan=2, sticky=NSEW)
    ttk.Button(mainframe, text="Select directory", command=browse_for_file_out).grid(column=1, row=4, sticky=EW)
    file_path_out = StringVar(value="No directory selected")
    (file_path_entry := ttk.Entry(mainframe, textvariable=file_path_out, width=100)).grid(column=2, row=4, sticky=EW)

    # User instructions
    ttk.Label(mainframe, text="- Leave this blank to use input file compileTo line.\n- "
              "The datapack .zip will go inside the output directory. "
              "If you want it\n to compile straight into a world, select "
              "that world's datapacks folder.").grid(column=2, row=5, sticky=NSEW)
    
    # Compilation button (and maybe settings in the future)
    ttk.Button(mainframe, text="This button will eventually compile the file,\nbut it does nothing right now").grid(column=2,row=6, sticky=EW)

    # Required Tkinter thing
    root.mainloop()