import os

path = '6.华为审核'

# for filepath, folders, files in os.walk(path):
#     # print(filepath, folders, files)
#     for file in files:
#         print(os.path.join(filepath, file))

for file in os.listdir(path):
    # print(file)
    if 'xlsx' in file:
        print(file)
