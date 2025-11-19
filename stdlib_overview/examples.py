# HTTP Server

## python3.14 -m http.server

# Random
import random
random.random()  # e.g. 0.4942866406918549

## random.randint(start, stop)
random.randint(0, 20)  # random number, between 0 and 20 (inclusive on both ends)

## Choose a random element from a sequence
random.choice(["A", "B", "C", "D", "E"])  # e.g. C

## Reorder a sequence randomly
a_list = list(range(16))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
random.shuffle(a_list)  # no result, change is in-place
print(a_list)  # e.g. [3, 2, 1, 12, 0, 6, 13, 14, 11, 9, 10, 8, 4, 5, 7, 15]

# Secrets
import secrets

## Generate a random string in hexadecimal
secrets.token_hex()

## Generate a URL-safe string
secrets.token_urlsafe()

## Generate password of length 8, safely
import string
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))

# csv
import csv

with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])


# datetime
from datetime import datetime, timedelta, timezone

dt = datetime.now(tz=timezone.utc)
print(dt)

print(dt + timedelta(days=1, hours=3))

# socket - UDP sending
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

print(f"UDP target {UDP_IP}:{UDP_PORT}, message: {MESSAGE.decode()}")

sock = socket.socket(
    socket.AF_INET, # Internet
    socket.SOCK_DGRAM,  # UDP
)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# logging
import logging


logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s',
    level=logging.INFO,
)


logging.info("Hello, world!")

