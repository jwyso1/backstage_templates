import subprocess
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print("hello")
process = subprocess.Popen(
    ["python", "-m", "poetry", "update", "--lock"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    shell=True,
    cwd=dir_path + "/template_1"
)
for line in process.stdout:
    print(line.decode("utf-8").strip())
