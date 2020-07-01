import requests
import tkinter
from tkinter import messagebox

# 入力値
def input_message():
    message = input_box.get()
    payload = {"value1":message}
    return payload

# IFTTT_Webhook
def webhook(eventid, payload):
    url = "https://maker.ifttt.com/trigger/" + eventid + "/with/key/dCm7Vg5DJEyLdAMxREVHdGAAWU0zwxPoru8tTH_1vC5"
    response = requests.post(url, data=payload)
    return response.status_code

def button_click():
    payload = input_message()

    if(webhook("message_post", payload) == 200):
        messagebox.showinfo("メッセージ送信","メッセージ送信完了しました")
    else:
        messagebox.showerror("エラー","メッセージ送信に失敗しました")   

root = tkinter.Tk()
root.title("MainSender")
root.geometry("360x240")

input_label = tkinter.Label(text="メッセージ")
input_label.place(x=10, y=70)
input_box = tkinter.Entry(width=40)
input_box.place(x=10, y=100)
button = tkinter.Button(text="送信", command=button_click)
button.place(x=10, y=130)

root.mainloop()
