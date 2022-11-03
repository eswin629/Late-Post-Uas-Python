import tkinter

class MyGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.canvas = tkinter.Canvas(self.main_window, width=300, height=300)
		self.canvas.create_oval(50, 50, 280, 280)
		self.canvas.pack()
		tkinter.mainloop()

my_gui = MyGUI()