import pathlib
import glob
import shutil


path = pathlib.Path.cwd().joinpath('data')
for file in path.iterdir():
    print (file)
#
# for f in path:
#     print(f)
# print(pathlib.Path.cwd().joinpath('data'))

