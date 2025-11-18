# Copy selected keys with values from `defaults` to `custom`
# Combine two dicts together making a 3rd dict, making sure that values from `custom`
# will override values with the same keys from `defaults`

defaults = {
    "host": "127.0.0.1",
    "port": 6379,
    "username": "python-training",
    "password": "mypassword",
}

custom = {
    "username": "secretuser",
    "password": "pass",
}

combined = dict(defaults, **custom)

print(combined)
