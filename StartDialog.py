from tkinter import *
from tkinter import filedialog
import pickle

class ParameterInput:
	def __init__(self):
		self.w = w = Tk()
		self.fn = ""
		self.inputs = []
		Label(w, text="Alpha: ").grid(row=0, column=0)
		self.inputs.append(Entry(w))

		Label(w, text="Gamma: ").grid(row=1, column=0)
		self.inputs.append(Entry(w))

		Label(w, text="Lambda: ").grid(row=2, column=0)
		self.inputs.append(Entry(w))

		Label(w, text="Epsilon Decay: ").grid(row=3, column=0)
		self.inputs.append(Entry(w))

		for i in range(len(self.inputs)):
			self.inputs[i].grid(row=i, column=1)

		Button(w, text="OK", command=self.ok).grid(row=4)
		w.mainloop()
	
	def ok(self):
		try:
			for entry in self.inputs:
				float(entry.get())
		except ValueError:
			Label(self.w, text="Invalid input", fg="red").grid(row=5, column=0)
			return

		params = []
		for i in self.inputs:
			params.append(float(i.get()))
		if self.fn == "":
			self.fn = filedialog.asksaveasfilename(filetypes=[('save files', '.save'), ('all files', '.*')])
		if self.fn != "":
			pickle.dump(params, open(self.fn, "wb"))
			self.w.destroy()

if __name__ == "__main__":
	sd = ParameterInput()
	
