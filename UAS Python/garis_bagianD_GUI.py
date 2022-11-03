import tkinter

class MyGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.canvas = tkinter.Canvas(self.main_window, width=450, height=450)
		self.canvas.create_line(20,300,420,300)
		self.canvas.create_line(20,150,420,150)
		self.canvas.create_line(20,200,420,200)
		self.canvas.create_line(20,100,420,100)
		self.canvas.create_line(20,50,420,50)
		self.canvas.create_line(20,250,420,250)

		self.canvas.create_line(100,50,100,300)
		self.canvas.create_line(420,50,420,300)
		self.canvas.create_line(180,50,180,300)
		self.canvas.create_line(20,50,20,300)
		self.canvas.create_line(340,50,340,300)
		self.canvas.create_line(260,50,260,300)

		self.canvas.pack()

		tkinter.mainloop()


my_gui = MyGUI()