
import streamlit as st
import qrcode
from PIL import Image
import io

def main():
    st.title("QR Code Generator")

    text_input = st.text_input("Enter text or URL to generate QR code")

    if st.button("Generate QR Code"):
        if text_input:
            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text_input)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            # Save image to a buffer
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            byte_im = buf.getvalue()

            # Display the image
            st.image(byte_im, caption="Generated QR Code", use_column_width=True)

            # Add a download button
            st.download_button(
                label="Download QR Code",
                data=byte_im,
                file_name="qr_code.png",
                mime="image/png",
            )
        else:
            st.warning("Please enter some text or a URL.")

if __name__ == '__main__':
    main()
