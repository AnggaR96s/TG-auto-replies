import time
from telethon import TelegramClient, events

# or use your own
api_id = 00000
api_hash = 'YOUR_API_HASH'

# fill in your own details here
phone = 'YOUR_PHONE_NUMBER'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'  # if you have two-step verification enabled

# content of the automatic reply
message = "YOUR_MESSAGE_FOR_AUTO_REPLY"


def main():
    # Create the client and connect
    client = TelegramClient(username, api_id, api_hash, update_workers=1, spawn_read_thread=False)
    client.start(phone, password)

    @client.on(events.NewMessage(incoming=True))
    def _(event):
        if event.is_private:
            print(time.asctime(), '-', event.message)  # optionally log time and message
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            client.send_message(event.message.from_id, message)

    print(time.asctime(), '-', 'Auto-replying...')
    client.idle()
    client.disconnect()
    print(time.asctime(), '-', 'Stopped!')


if __name__ == '__main__':
    main()
