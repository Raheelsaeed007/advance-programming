# import tkinter as tk.
import tkinter as tk
# The root
root = tk.Tk()

# left frame
left_frame = tk.Frame(root, borderwidth=5, background='Light grey')
left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

# This label will have a text of A inside and background as blue.
label_a = tk.Label(left_frame, text='A', background='blue')
label_a.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# This label will have a text of B inside and background as white.
label_b = tk.Label(left_frame, text='B', background='White')
label_b.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

# C and B.
MyRight_frame = tk.Frame(root, borderwidth=5, background='Light Grey')
MyRight_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# background as white.
label_c = tk.Label(MyRight_frame, text='C', background='White')
label_c.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

# This label will have a text of D inside and background as blue.
label_d = tk.Label(MyRight_frame, text='D', background='blue')
label_d.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

# running the mainloop.
root.mainloop()