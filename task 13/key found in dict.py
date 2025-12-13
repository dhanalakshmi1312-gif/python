print(" 1. Find the Key Found in Dictionary using Arbitrary Keyword Argument")
def find_key(**kwargs):
    for key in kwargs:
        print("Key Found:", key)
