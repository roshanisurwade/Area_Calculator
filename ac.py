from tkinter import *
from tkinter.messagebox import *
from math import pi

root = Tk()
root.title("Area Calculator App")
root.geometry("800x700+50+50")
root.iconbitmap("calci.ico")
f = ("Century", 15, "bold")
root.configure(bg="hot pink")

lab_title = Label(root, text="Area Calculator", font=f, bg="hot pink")
lab_title.pack(pady=5)

lab_length = Label(root, text="Length:", font=f, bg="hot pink")
ent_length = Entry(root, font=f, width=10, bg="azure2")
lab_length.place(x=300,y=100)
ent_length.place(x=420,y=100)

lab_breadth = Label(root, text="breadth:", font=f, bg="hot pink")
ent_breadth = Entry(root, font=f, width=10, bg="azure2")
lab_breadth.place(x=300, y=150)
ent_breadth.place(x=420, y=150)

lab_height = Label(root, text="Height:", font=f, bg="hot pink")
ent_height = Entry(root, font=f, width=10, bg="azure2")
lab_height.place(x=300, y=200)
ent_height.place(x=420, y=200)

lab_radius = Label(root, text="Radius:", font=f, bg="hot pink")
ent_radius = Entry(root, font=f, width=10, bg="azure2")
lab_radius.place(x=300, y=250)
ent_radius.place(x=420, y=250) 


def rectangle():
	length = ent_length.get()
	breadth = ent_breadth.get()
	if length == "" or breadth == "":
		showerror("error", "input cannot be empty")
		return
	if length.isspace() or breadth.isspace():
		showerror("error", "input cannot contain spaces")
		return

	try:
		length = float(length)
		breadth = float(breadth)
	except Exception:
		showerror("error", "inputs cannot be text")
		return
	if length <= 0 or breadth<=0:
		showerror("Error", "Inputs cannot be negative")
		return

	min_limit = 1
	max_limit = 1000
	if length < min_limit or breadth > max_limit or length > max_limit or breadth < min_limit:
		showerror("invalid Input", f"length and breadtg must be betn {min_limit} and {max_limit}")
		return
	
	area = length * breadth
	msg = "Area of reactangle = " + str(area) 
	lab_result.configure(text=msg)
	showinfo("Sucess", "success")
	ent_length.delete(0, END)
	ent_breadth.delete(0, END)
	ent_length.focus()


def triangle():
	breadth = ent_breadth.get()
	height = ent_height.get()
	if breadth == "" or height == "":
		showerror("error", "input cannot be empty")
		return
	if breadth.isspace or height.isspace():
		showerror("error", "input cannot contain spaces")
		return
	
	try:
		breadth = float(breadth)
		height = float(height)
	except Exception:
		showerror("error", "inputs cannot be text")
		return
	if breadth <= 0 or height <= 0:
		showerror("Error", "inputs cannot be negative")
		return
	
	min_limit = 1
	max_limit = 1000
	if breadth < min_limit or height > max_limit or breadth > max_limit or height < min_limit:
		showerror("invalid Input", f"length and breadth must be betn {min_limit} and {max_limit}")
		return
	area = 0.5 * breadth * height
	msg = "Area of triangle = " + str(area) 
	lab_result1.configure(text=msg)
	showinfo("Sucess", "success")
	ent_breadth.delete(0, END)
	ent_height.delete(0, END)
	ent_breadth.focus()

def square():
	length = ent_length.get()
	if length == "":
		showerror("error", "length cannot be empty")
		return
	if length.isspace():
		showerror("error", "length cannot conatin spaces")
		return
	try:
		length = float(length)
	except Exception:
		showerror("Error", "length cannot be text")
		return
	if length <=0:
		showerror("error", "length cannot be negative")
		return

	min_limit = 1
	max_limit = 1000
	if length < min_limit or length > max_limit:
		showerror("invalid Input", f"length  must be betn {min_limit} and {max_limit}")
		return
	area = length ** 2


	msg = "Area of square = " + str(area)
	lab_result2.configure(text=msg)
	showinfo("Sucess", "success")
	ent_length.delete(0, END)
	ent_length.focus()

def circle():

	radius = ent_radius.get()
	if radius == "":
		showerror("error", "input cannot be empty")
		return
	if radius.isspace():
		showerror("error", "radius cannot contain spaces")
		return
	try:
		radius = float(radius)
	except Exception:
		showerror("Error", "input cannot be text")
		return
	if radius <=0:
		showerror("error", "input cannot be negative")
		return

	min_limit = 1
	max_limit = 1000
	if radius < min_limit or radius > max_limit:
		showerror("invalid Input", f"radius  must be betn {min_limit} and {max_limit}")
		return

	area = 3.14 * radius ** 2
	msg = "Area of circle = " + str(area)
	lab_result3.configure(text=msg)
	showinfo("Sucess", "success")
	ent_radius.delete(0, END)
	ent_radius.focus()


def clear():
	ent_length.delete(0, END)
	ent_breadth.delete(0, END)
	ent_height.delete(0, END)
	ent_radius.delete(0, END)
	lab_result.configure(text="")
	lab_result1.configure(text="")
	lab_result2.configure(text="")
	lab_result3.configure(text="")
	ent_length.focus()
	

btn_rectangle = Button(root,text = "Calculate Rectangle",font = f,fg="black",bg="lightblue",width=17, command=rectangle)
btn_rectangle.place(x=350, y=310)

btn_triangle = Button(root,text = "Calculate Triangle",font = f,fg="black",bg="lightblue", width=17, command=triangle)
btn_triangle.place(x=350, y=400)

btn_square = Button(root,text = "Calculate Square",font = f,fg="black",bg="lightblue", width=17, command=square)
btn_square.place(x=350, y=490)

btn_circle = Button(root,text = "Calculate Circle",font = f,fg="black",bg="lightblue", width=17, command=circle)
btn_circle.place(x=350, y=580)

btn_clear = Button(root,text = "Clear",font = f,fg="black", bg="lightblue", width=12, command=clear)
btn_clear.place(x=370,y=670)



lab_result = Label(root, font=f, bg="hot pink")
lab_result.place(x=350, y=350)

lab_result1 = Label(root, font=f, bg="hot pink")
lab_result1.place(x=350, y=440)

lab_result2 = Label(root, font=f, bg="hot pink")
lab_result2.place(x=350, y=530)

lab_result3 = Label(root, font=f, bg="hot pink")
lab_result3.place(x=350, y=620)


root.mainloop()