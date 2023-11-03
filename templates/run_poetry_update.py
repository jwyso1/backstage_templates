import subprocess

grep_process = subprocess.Popen(
    ["python", "-m", "poetry", "update", "--lock"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, cwd="template_1"
)
for line in grep_process.stdout:
    print(line.decode("utf-8").strip())
