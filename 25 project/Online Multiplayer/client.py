import streamlit as st
import socket
import threading

st.title("🎮 Online Multiplayer Game")
st.write("Connect with other players and chat in real-time!")

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False

if st.button("Start Game"):
    try:
        client.connect((HOST, PORT))
        connected = True
        st.session_state["messages"] = ["Connected to Server!"]
    except:
        st.error("Failed to connect to server.")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                st.session_state["messages"].append(message)
        except:
            break

if connected:
    threading.Thread(target=receive_messages, daemon=True).start()
    
    user_input = st.text_input("Type your message:")
    if st.button("Send"):
        client.send(user_input.encode())
        st.session_state["messages"].append(f"You: {user_input}")

    for msg in st.session_state.get("messages", []):
        st.write(msg)
