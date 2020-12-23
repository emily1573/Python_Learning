import os
import time
import shutil

# 做一个函数，可以复用
def copy_func(src_files,file,type_file):
    m_time = os.path.getmtime(os.path.join(src_files, file))
    real_time = time.localtime(m_time)
    dt = time.strftime("%Y-%m-%d", real_time)
    year, month, day = dt.split('-') # 把时间split切分
    if os.path.exists(os.path.join('newWorld_2',type_file,year)): # 判断是否有年目录
        if os.path.exists(os.path.join('newWorld_2', type_file, year, month)): # 判断是否有月目录
            # 把文件复制进去
            shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', type_file, year, month))
        else: # 如果月目录不存在则创建 并复制
            os.makedirs(os.path.join('newWorld_2', type_file, year, month)) # 特别注意mkdir,makedirs
            shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', type_file, year, month))
    else: # 这种情况是年目录不存在 那么就一口气创建年月目录再复制
        os.makedirs(os.path.join('newWorld_2', type_file, year, month))
        shutil.copy(os.path.join(src_files, file), os.path.join('newWorld_2', type_file, year, month))

# 手机的数据整理，基于名字
src_files = 'files'
for file in os.listdir(src_files): # 遍历目标文件夹
    if '.jpg' in file:
        copy_func(src_files, file, 'images')

    elif '.mp4' in file:
        copy_func(src_files, file, 'videos')
