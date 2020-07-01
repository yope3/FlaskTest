import requests

# inpput
def input_message():
    message = input("メッセージを入力してください")
    payload = {"value1":message}
    return payload

# IFTTT_Webhook
def webhook(eventid, payload):
    url = "https://maker.ifttt.com/trigger/" + eventid + "/with/key/dCm7Vg5DJEyLdAMxREVHdGAAWU0zwxPoru8tTH_1vC5"
    response = requests.post(url, data=payload)
    return response.status_code

if __name__ == "__main__":
    payload = input_message()

    print("メール送信開始")

    if webhook("message_post", payload) == 200:
        print("メール送信完了")
    else:
        print("メール送信失敗")