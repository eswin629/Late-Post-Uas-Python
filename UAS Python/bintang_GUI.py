import tkinter

class MyGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.canvas = tkinter.Canvas(self.main_window, width=300, height=300)
		self.canvas.create_line(125,125,225,225,5,175,245,175,25,225,125,125)
		self.canvas.pack()
		tkinter.mainloop()

# Create an instance of the MyGUI class.
my_gui = MyGUI()