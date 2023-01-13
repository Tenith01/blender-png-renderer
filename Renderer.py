import subprocess


def ImageRenderer(blenderFilePath, exportType, selectedFrame, exportPath):
    cmd = "blender -b " + blenderFilePath + " -F " + exportType + " -f " + selectedFrame + " -o " + exportPath

    # run the command and open a pipe to read its output
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    progressbarValue = 0;
    rendererStat = "";
    # read the output line by line
    for line in iter(process.stdout.readline, b''):
        outPutLine = line.decode().strip().split('|')[-1]

        outPutLine = outPutLine.split(" ")
        if outPutLine[1] == "Syncing":
            rendererStat = "Syncing..."
            a = 0
        elif outPutLine[1] == "Rendering":
            max_value = outPutLine[-2]
            value = outPutLine[-4]
            progressbarValue = int(int(value) / int(max_value) * 100)

            print("Rendering :", progressbarValue, "%")
            rendererStat = "Rendering :", progressbarValue, "%"

        elif outPutLine[1] == "Tile":
            # print(outPutLine)
            max_value = outPutLine[-1].split('-')[-1]
            value = outPutLine[-1].split('-')[-2]
            progressbarValue = int(int(value) / int(max_value) * 100)

            print("Compositing :", progressbarValue, "%")
            rendererStat = "Compositing :", progressbarValue, "%"
        # print(outPutLine)

        # return rendererStat, "|", progressbarValue
#
#
def say_hello():
    print("Hello World")
