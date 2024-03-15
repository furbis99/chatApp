# Test code
import requests

def test_1():
    messages = requests.get("http://167.99.63.70/messages").json()
    for message_content in messages:
        print(message_content['date'])
        


if __name__ == "__main__":
    test_1()