import tkinter

class MyGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.canvas = tkinter.Canvas(self.main_window, width=300, height=300)
		self.canvas.create_line(150,150,200,250,100,250,150,150)
		self.canvas.pack()

		tkinter.mainloop()


my_gui = MyGUI()