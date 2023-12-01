import subprocess
import os
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
print("hello")
print(os.listdir(dir_path + "/template_1"))
process = subprocess.Popen(
    ["python", "-m", "poetry", "update", "--lock"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    shell=True,
    cwd=dir_path + "/template_1"
)
print(os.listdir(dir_path + "/template_1"))
time.sleep(10)
print(os.listdir(dir_path + "/template_1"))
