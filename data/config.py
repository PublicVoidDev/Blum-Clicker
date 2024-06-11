# api id, hash
API_ID = 70484356
API_HASH = 'b763e1f3bsd23906ff71c4e7d2130e219'

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'PLAY': [5, 15],   # delay between play in seconds
    'ERROR_PLAY': [60, 180],    # delay between errors in the game in seconds
}

# points with each play game; max 280
POINTS = [210, 240]

# proxy type
PROXY_TYPE = "socks5"  # "socks4", "socks5" and "http" are supported

# title blacklist tasks (do not change)
BLACKLIST_TASKS = ['Farm points']

# session folder (do not change)
WORKDIR = "sessions/"
