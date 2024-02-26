from polynomials import *


def cr(fn):
    app = Tk()
    app.title("График")
    app.geometry("400x475+500+300")
    app.resizable(0, 0)

    Label(app, text = "Масштаб: 1 / ", font = "Tahoma 15 bold").place(x = 10, y = 430)
    ratio = Entry(app, font = "Tahoma 15 bold", width = 3)
    ratio.insert(END, "1")
    ratio.place(x = 160, y = 430)

    cnv = Canvas(app, width = 400, height = 400)
    cnv.pack()

    def draw():
        cnv.delete("all")
        cnv.create_line(200, 390, 200, 10, width=1, arrow=LAST)
        cnv.create_line(10, 200, 390, 200, width=1, arrow=LAST)
        cnv.create_text(215, 20, text="y", fill="blue", font="Tahoma 10 bold")
        cnv.create_text(380, 215, text="x", fill="blue", font="Tahoma 10 bold")
        try:
            cnv.create_text(215, 100, text=round(100 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(215, 300, text=round(-100 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(215, 150, text=round(50 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(215, 250, text=round(-50 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(215, 50, text=round(150 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(215, 350, text=round(-150 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(100, 215, text=round(-100 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(300, 215, text=round(100 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(150, 215, text=round(-50 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(250, 215, text=round(50 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(50, 215, text=round(-150 / float(ratio.get())), font="Tahoma 8 bold")
            cnv.create_text(350, 215, text=round(150 / float(ratio.get())), font="Tahoma 8 bold")
            for x in arange(-195, 195, 0.25): cnv.create_line(x * float(ratio.get()) + 200, -fn(x) * float(ratio.get()) + 200, x * float(ratio.get()) + 201, -fn(x + 1) * float(ratio.get()) + 200, width = 2, fill = "green")
        except ValueError: showerror("Ошибка графика", f"Нельзя построить график по масштабу: {ratio.get()}")

    draw()

    Button(app, text = "Применить", font = "Tahoma 15 bold", bg = "blue", fg = "white", command = draw).place(x = 250, y = 420)

    app.mainloop()


def create_graph(s):
    if s != "":
        try: cr(lambda x: eval(lex_to_python(s)))
        except: showerror("Ошибка постройки графика", f"Нельзя построить график функции: {lex_to_python(s)}")