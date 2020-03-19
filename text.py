import os
import cv2
input_dir = 'datafile/input/'
target_dir = 'datafile/target/'
tfrecord_dir = 'datafile/TFRecords_file'
output_dir = 'datafile/target/'

# 本地数据集文件名处理
input_files = [input_dir + filename for filename in os.listdir(input_dir)]
target_files = [target_dir + filename for filename in os.listdir(target_dir)]

img = cv2.imread('datafile/target/a0002.jpg')


img2 = cv2.imread('datafile/target/output/target_original_a0002.jpg_c61ac762-96ab-41c5-afe2-94074c975b76.jpg')
print(img2)