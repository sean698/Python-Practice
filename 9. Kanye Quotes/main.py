from tkinter import *
import requests

def get_quotes():
    res = requests.get(url="https://api.kanye.rest")
    res.raise_for_status()
    quote = res.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=400)
quote_img = PhotoImage(file="9. Pomodoro/quote.png")
canvas.create_image(200, 200, image=quote_img)
quote_text = canvas.create_text(200, 200, text="Kanye Quotes Goes Here", width=200)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="9. Pomodoro/Kanye.png")
button = Button(image=kanye_img, command=get_quotes, highlightthickness=0)
button.grid(row=1, column=0)

window.mainloop()

