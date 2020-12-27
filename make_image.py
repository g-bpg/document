from PIL import ImageFont, ImageDraw, Image
from random import randint

import argparse

def get_rand_color(hi, lo):
    return (randint(hi, lo), randint(hi, lo), randint(hi,lo))

def get_rand_light():
    return get_rand_color(25, 75)

def get_rand_dark():
    return get_rand_color(175, 225)

def create_bpg_image(filename, fg_color, bg_color, thread_num, font_path):
    dimensions = (500, 500)

    image = Image.new("RGBA", dimensions, bg_color)
    image_center = (dimensions[0] / 2, dimensions[1] / 2)

    draw = ImageDraw.Draw(image)

    # Figure out locations of the /bpg/ and thread number texts
    bpg_font = ImageFont.truetype(font_path, 100)
    bpg_str = "/bpg/"
    bpg_strsize = draw.textsize(bpg_str, bpg_font)
    bpg_location = (image_center[0] - bpg_strsize[0] / 2, image_center[1] - bpg_strsize[1], )

    num_font = ImageFont.truetype(font_path, 60)
    threadnum_str = f"#{thread_num}"
    threadnum_strsize = draw.textsize(threadnum_str, num_font)

    threadnum_location = (image_center[0] - threadnum_strsize[0] / 2 - 10,
                          bpg_location[1] + bpg_strsize[1] + threadnum_strsize[1]/ 2)

    # Draw the text at the appropriate locations
    draw.text(bpg_location, bpg_str, font=bpg_font, fill=fg_color, align="center")
    draw.text(threadnum_location, threadnum_str, font=num_font, fill=fg_color, align="center")

    image.save(filename + ".png", format="png")

def setup_args():
    parser = argparse.ArgumentParser(description="Output the /bpg/ image")
    parser.add_argument("--threadnum", type=int, help='Display the thread number in the image.', required=True)
    parser.add_argument("--out", type=str, help='Output filename for image.', default="out")
    parser.add_argument("--font", type=str, help="Name of Font used to display text.", default="LiberationSerif-Bold.ttf")

    return parser.parse_args()

args = setup_args()

create_bpg_image(args.out + "_light", get_rand_light(), get_rand_dark(), args.threadnum, args.font)
create_bpg_image(args.out + "_dark", get_rand_dark(), get_rand_light(), args.threadnum, args.font)
