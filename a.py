import subprocess

# command to be run
cmd = "wget https://www.example.com/file.zip"

# run the command and open a pipe to read its output
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# read the output line by line
while True:
    line = process.stderr.readline()
    line = line.decode().strip()
    print(line)
    if "%" in line:
        # parse the percentage information
        percentage = int(line.split()[-1].replace("%", ""))
        print(f'Current percentage: {percentage}%')
    if line == '' and process.poll() is not None:
        break
