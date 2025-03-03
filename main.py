from tkinter import Tk, Entry, Label, Button

BACKGROUND_COLOR = "#C4D9FF"

# Setup the main screen
window= Tk()
window.title("Miles to KM Converter")
window.minsize(width=100, height=100)
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

def converter():
    miles= user_input.get()
    # convert the miles to km and round the result to 2 digit
    km= round((float(miles) * 1.608), 2)
    result_label.config(text=km)

user_input= Entry()
user_input.grid(column= 1, row= 0)

miles_label= Label(text= "Miels", padx=10, bg=BACKGROUND_COLOR)
miles_label.grid(column= 2, row= 0)

is_equal= Label(text="Is equal to:", bg=BACKGROUND_COLOR)
is_equal.grid(column= 0, row=1)

km_label= Label(text= "KM", bg= BACKGROUND_COLOR)
km_label.grid(column= 2,row= 1)

result_label= Label(text="0", padx=10, bg= BACKGROUND_COLOR)
result_label.grid(column= 1, row= 1)

button= Button(text="Calculate", bg= BACKGROUND_COLOR, command=converter)
button.grid(column=1, row= 2)



window.mainloop()