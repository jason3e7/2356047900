#!/usr/bin/env python3
import os
from Crypto.Cipher import AES
from base64 import b64decode, b64encode

key = os.urandom(16)

def decrypt(text):
    iv, text = text[:16], text[16:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.decrypt(text)

def encrypt(text):
    iv, text = text[:16], text[16:]
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(text)


initIV = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

for i in range(10) :
    text = (i).to_bytes(16, byteorder="big")
    text = initIV+encrypt(initIV+text)
    text = b64encode(text)
    
    print(int.from_bytes(decrypt(b64decode(text))[:16],'big'))






