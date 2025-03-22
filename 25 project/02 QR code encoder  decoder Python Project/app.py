import streamlit as st
import qrcode
from PIL import Image

st.title("QR Code Generator & Decoder")

text = st.text_input("Enter text or URL:")
if st.button("Generate QR Code"):
    qr = qrcode.make(text)
    qr.save("qrcode.png")
    st.image("qrcode.png")

uploaded_file = st.file_uploader("Upload QR Code to Decode", type=["png", "jpg", "jpeg"])
if uploaded_file:
    from pyzbar.pyzbar import decode
    img = Image.open(uploaded_file)
    result = decode(img)
    if result:
        st.write("Decoded Text:", result[0].data.decode())
    else:
        st.write("No QR code found.")
