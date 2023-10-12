import os
import subprocess

# 获取Git仓库的根目录
git_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('utf-8').strip()

# 构建bugreport文件夹的路径
bugreport_folder = os.path.join(git_root, 'bugreport')

print(bugreport_folder)