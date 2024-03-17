import threading
import redis
from redis_server import R

def send_message(name): #send message 
    while True:
        try:
            message = input(f"{name}: ")
            R.publish('chat', f"{name}: {message}")
        except redis.exceptions.ConnectionError:
            print("Error: Could not connect to Redis server.")
            break

def receive_messages(name): #recieve message
    p = R.pubsub()
    p.subscribe('chat')

    # Print subscription confirmation message
    print(f"Subscribed to channel: chat")

    for message in p.listen():
        if message['type'] == 'message':
            data = message['data'].decode()
            sender, msg = data.split(':', 1)  # Split sender and message
            print(sender,msg)
            if sender.strip() != name:  # Don't print own messages
                print(f"{sender.strip()}: {msg.strip()}")

if __name__ == "__main__":
    name = input("Enter your name: ")

    send_thread = threading.Thread(target=send_message, args=(name,))
    recv_thread = threading.Thread(target=receive_messages, args=(name,))

    send_thread.start()
    recv_thread.start()

    send_thread.join()
    recv_thread.join()

