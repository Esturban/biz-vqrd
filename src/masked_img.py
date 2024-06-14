from PIL import Image, ImageDraw

def masked_inner_img(inner_img_path: str, qr_img: Image):
    img = Image.open(inner_img_path).convert("RGBA")
    img = img.resize((int(qr_img.width * 0.3), int(qr_img.height * 0.3)))
    img_width, img_height = img.size

    mask = Image.new("L", (img_width, img_height), 0)
    draw = ImageDraw.Draw(mask)
    circle_center = (img_width // 2, img_height // 2)
    circle_radius = min(img_width, img_height) // 2
    draw.ellipse(
        (
            circle_center[0] - circle_radius,
            circle_center[1] - circle_radius,
            circle_center[0] + circle_radius,
            circle_center[1] + circle_radius,
        ),
        fill=255,
    )
    img = Image.composite(
        img,
        Image.new("RGBA", img.size),
        mask
    )
    return img