# TG-auto-replies

Getting started
We’ll use version 0.18.1 of Telethon, a Python 3 implementation of the Telegram API:

pip3 install telethon==0.18.1
Authenticating to the Telegram API
To interact with the Telegram API using Telethon, we first need to create a Telethon client object (docs). We’ll need several pieces of information to do this:

An api_id and api_hash for a Telegram application. Read about this here: https://core.telegram.org/api/obtaining_api_id
Your phone number
Your password if you have two-step verification turned on
Telethon creates a local file to persist your session so you don’t have to keep authenticating; in the code fragment below, the username variable is the name of the file representing your saved session, and does not necessarily have to be your Telegram username.

All credits goes to https://github.com/yi-jiayu
