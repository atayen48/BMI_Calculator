import tkinter

window = tkinter.Tk()
window.minsize(width=400, height=400)
window.title("VKI Hesaplama")


#hesaplama
def calc():
    kg = int(weight_entry.get())
    cm = int(height_entry.get()) / 100
    cm_2 = cm * cm
    sonuc = kg / cm_2
    sonuc = round(sonuc,1)
    result_label.config(text=sonuc)

    if sonuc < 18.5:
        last_label.config(text="Underwight!\nHealt Risk:Minimal", bg="light yellow")
    elif (sonuc > 18.5) and (sonuc<= 24.9):
        last_label.config(text="Normal!\nHealt Risk:Minimal", bg="light green")
    elif (sonuc > 25) and (sonuc <= 29.9):
        last_label.config(text="Overweight!\nHealt Risk:Increased", bg="orange")
    elif (sonuc > 30) and (sonuc <= 34.9):
        last_label.config(text="Obese!\nHealt Risk:Increased", bg="red")
    else:
        last_label.config(text="Health is at risk!\n Need to lose", bg="red")

my_label = tkinter.Label(text="BMI Calculator", font=("arial", 15, "bold"), width=30)
my_label.config(bg="light grey", fg="dark blue")
my_label.pack()

weight_label = tkinter.Label(text="Weight: ", font=("arial", 15, "bold"))
weight_label.config(bg="light grey", fg="dark blue")
weight_label.place(x=20, y=50)

weight_kg = tkinter.Label(text="Enter Kg.", font=("arial", 12, "italic"))
weight_kg.place(x=300, y=50)

weight_entry = tkinter.Entry(width=15, font=("arial",15, "bold"))
weight_entry.place(x=120, y=50)

height_label= tkinter.Label(text="Height: ", font=("arial", 15, "bold"))
height_label.config(bg="light grey",fg="dark blue")
height_label.place(x=20, y=100)

height_cm = tkinter.Label(text="Enter Cm.", font=("arial", 12, "italic"))
height_cm.place(x=300, y=100)

height_entry = tkinter.Entry(width=15, font=("arial",15, "bold"))
height_entry.place(x=120, y=100)

result_label = tkinter.Label(text="....", font=("arial", 20, "bold"), width=22,)
result_label.config(bg="light grey", fg="red")
result_label.place(x=10, y=200)

last_label = tkinter.Label(text="......", font=("arial", 20, "bold"), width=22,)
last_label.config(bg="light grey", fg="dark blue")
last_label.place(x=10, y=270)


result_buton = tkinter.Button(text="Calculate", font=("arial",15, "bold"), command=calc)
result_buton.place(x=150, y=150)


tkinter.mainloop()
