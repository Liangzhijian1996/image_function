# 本地数据集文件名处理
import os

input_dir = 'datafile/input/'
target_dir = 'datafile/target/'

input_files = [input_dir + filename for filename in os.listdir(input_dir)]
target_files = [target_dir + filename for filename in os.listdir(target_dir)]


def image_rename(input_files, target_files):
    for input_file, target_file in zip(input_files, target_files):
        input_name = input_file.split('/')[2].split('-')[0]
        input_name = input_dir + input_name + '.jpg'
        os.rename(input_file, input_name)

        target_name = target_file.split('/')[2].split('-')[0]
        target_name = target_dir + target_name + '.jpg'
        os.rename(target_file, target_name)
