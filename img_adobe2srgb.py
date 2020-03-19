import io
import os
from PIL import Image, ImageCms


def adobe2srgb(img):
    f = io.BytesIO(img.info.get('icc_profile'))
    prf = ImageCms.ImageCmsProfile(f)
    srgb = ImageCms.createProfile('sRGB')
    img = ImageCms.profileToProfile(img, prf, srgb)
    return img


def Adobe2srgb(input_path, output_path):
    img = adobe2srgb(Image.open(input_path))
    img.save(output_path)


input_dir = 'datafile/input/'
target_dir = 'datafile/target/'
output_dir = 'datafile/target/'

input_files = [input_dir + filename for filename in os.listdir(input_dir)]
target_files = [target_dir + filename for filename in os.listdir(target_dir)]

for input_file, target_file in zip(input_files, target_files):
    # datafile/target/a0002.jpg
    image_name = target_file.split('/')[2]
    image_dir = output_dir + image_name
    Adobe2srgb(target_file, image_dir)
