import tkinter

class MyGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.canvas = tkinter.Canvas(self.main_window, width=300, height=300)
		self.canvas.create_line(80,220,95,170,110,220,125,170,140,220,155,170,170,220,185,170,200,220,215,170,230,220)
		self.canvas.pack()
		tkinter.mainloop()

# Create an instance of the MyGUI class.
my_gui = MyGUI()