#!usr/bin/python3
# coding:utf-8
import os
import pytest
import requests as rq
from botlegram.utils.send import Send

#token = os.environ['TOKEN']
#chat_id = os.environ['CHAT_ID']
token = "1356390042:AAH9lgjFdlIq9eQsqoxxYRXzx3XchVfPAvs"
chat_id = 1304217168
api = "https://api.telegram.org/bot" + token + "/"
test = Send()
test.API = api

def test_send_message():
    res = test.send_message(chat_id, "test")
    assert res['ok'] == True

def test_send_photo():
    photo = "https://github.com/laplacetw/laplacetw.github.io/blob/master/images/avatar.png"
    res = test.send_photo(chat_id, photo, "laplacetw")
    assert res['ok'] == True