import os
import Augmentor

input_dir = 'datafile/input/'
target_dir = 'datafile/target/'
tfrecord_dir = 'datafile/TFRecords_file'

input_files = [input_dir + filename for filename in os.listdir(input_dir)]
target_files = [target_dir + filename for filename in os.listdir(target_dir)]

# 对文件夹里所有照片依次做如下操作，会生成一个output文件夹装处理结果图像
p = Augmentor.Pipeline(target_dir)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
p.process()
