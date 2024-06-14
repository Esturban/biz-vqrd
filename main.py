from datetime import datetime
from PIL import Image
from src.masked_img import masked_inner_img
from typing import Optional
from src.vcard import VCARD
import qrcode
import uuid
import os
import base64



def create_qr_code(output_directory: str, output_prefix: str, inner_img_path: str):
    qr_object = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_object.add_data(VCARD)
    qr_object.make(fit=False)
    img = qr_object.make_image(fill_color="black", back_color="white").convert("RGBA")

    inner_img = masked_inner_img(inner_img_path, img)
    img.paste(
        inner_img,
        (
            img.width // 2 - inner_img.width // 2,
            img.height // 2 - inner_img.height // 2
        ),
        mask=inner_img,
    )

    filename = f"{output_prefix}_{uuid.uuid4().hex}.png"
    output_path = os.path.join(output_directory, filename)
    inner_img.save(os.path.join(output_directory,"inner-output.png"))
    
    img.save(output_path)

def print_image_base64(image_path: str):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        print(f"PHOTO;ENCODING=base64;TYPE=PNG:{encoded_string}")

def compress_image(image_path, output_path, quality):
    # Open the image
    img = Image.open(image_path)
    
    # Save the image again with lower quality
    img.save(output_path, "PNG", quality=quality)

if __name__ == "__main__":
    create_qr_code("output","vcard", "headshot.png")
    # compress_image("headshot.png", "compressed_headshot.png", 50)
    # print_image_base64("compressed_headshot.png")
