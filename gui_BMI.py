import tkinter
import tkinter.ttk
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title('BMI calculator')
window.geometry('470x580+1000+0')
window.resizable(False, False)
window.config(bg='#f0f1f5')

# Icon
icon_image = tkinter.PhotoImage(file='bin/icon.png')
window.iconphoto(False, icon_image)


# top
top_image = tkinter.PhotoImage(file='bin/top.png')
top = tkinter.Label(master=window, image=top_image)
top.place(x=-10, y=0)

# bottom
bottom = tkinter.Label(
    master=window,
    bg='lightblue',
    width=72,
    height=18
)
bottom.place(x=0, y=310)

# 2 boxes

box_img = tkinter.PhotoImage(file='bin/box.png')
tkinter.Label(master=window, image=box_img).place(x=20, y=100)
tkinter.Label(master=window, image=box_img).place(x=230, y=100)

# 2 entries
height_var = tkinter.StringVar()
height_var.set('0')

height_entry = tkinter.Entry(
    master=window,
    width=5,
    font=('arial', 50),
    bd=0,
    bg='#fff',
    fg='black',
    justify=tkinter.CENTER,
    textvariable=height_var
    
    
)
height_entry.place(x=35, y=160)

weight_var = tkinter.StringVar()
weight_var.set('0')

weight_entry = tkinter.Entry(
    master=window,
    width=5,
    font=('arial', 50),
    bd=0,
    bg='#fff',
    fg='black',
    justify=tkinter.CENTER,
    textvariable=weight_var
)
weight_entry.place(x=250, y=160)


# 2 sliders
def slider_changed(value):
    #print(value, current_height_value.get())
    height_var.set(f'{current_height_value.get():.0f}')
    weight_var.set(f'{current_weight_value.get():.0f}')

    height_v = int(current_height_value.get())
    weight_v = int(current_weight_value.get())
    

    person_img_pil = Image.open('bin/man.png')
    #person_img_pil.show()
    person_img_pil = person_img_pil.resize([10 + int(weight_v*0.5), 10 + height_v])


    person_img_pil = ImageTk.PhotoImage(person_img_pil)

    man_image['image'] = person_img_pil
    man_image.image = person_img_pil
    man_image.place(x=115  - int(weight_v*0.19), y=570 - height_v)
    

    

    

current_height_value = tkinter.DoubleVar()

scale_style = tkinter.ttk.Style()
scale_style.configure('TScale', background='white')

slider_h = tkinter.ttk.Scale(
    master=window,
    command=slider_changed,
    variable=current_height_value,
    from_=0,
    to=220
)
slider_h.place(x=80, y=250)


current_weight_value = tkinter.DoubleVar()

slider_w = tkinter.ttk.Scale(
    master=window,
    command=slider_changed,
    variable=current_weight_value,
    from_=0,
    to=220
)
slider_w.place(x=300, y=250)



# Scale
scale_img = tkinter.PhotoImage(file='bin/scale.png')
tkinter.Label(master=window, image=scale_img, bg='lightblue').place(x=-25, y=320)

# Man Image
man_image = tkinter.Label(master=window, bg='lightblue')
man_image.place(x=70, y=530)


# Result Button
def result_BMI():
    h = int(height_var.get())
    w = int(weight_var.get())
    
    result = w / (h/100) ** 2
    print(result)
    
    result_label['text'] = f'{result:>4.0f}'


result_button = tkinter.Button(
    master=window,
    text='Result',
    font=('arial', 10, 'bold'),
    width=15,
    height=1,
    bg='#cf0e38',
    fg='white',
    command=result_BMI
)
result_button.place(x=280, y=340)

# Result
result_label = tkinter.Label(master=window, text='0',
                    font=('arial', 45, 'bold'),
                    bg='lightblue',
                    fg='gray90')
result_label.place(x=280, y=370)









window.mainloop()














































