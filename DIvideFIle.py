import subprocess

INPUT_FILE_PATH = 'Posts.xml'
OUTPUT_FILE_PATH = '/media/vesper/DATA/stackoverflow-data/divided-files/'
START_FILE_STRING = '<?xml version="1.0" encoding="utf-8"?>\n <posts>\n'
END_FILE_STRING = '</posts>'
POSTS_IN_ONE_FILE = 100000
START_LINE = 3
TOTAL_NUMBER_OF_LINES = 42850540


def numberOfLines(fname):
    p = subprocess.Popen(['wc', '-l', fname], stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
    result, err = p.communicate()
    if p.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0]) + 1

def readLines(startPosition, numberOfLines, filePath ):
    lines = []
    lineNumber = 0
    with open(filePath, 'r') as f:
        while(1):
            lineNumber+=1

            # ignore line
            if lineNumber < startPosition:
                f.readline()
                continue

            # number of lines reached
            if lineNumber >= startPosition + numberOfLines:
                break

            lines.append(f.readline())

    data = ''.join([str(x) for x in lines])
    return data

def writeToFile(data, OutputFilePath):
    text_file = open(OutputFilePath, "w")
    text_file.write(data)
    text_file.close()


if __name__ == '__main__':

    # numberOfLines = numberOfLines(INPUT_FILE_PATH)

    startLine = START_LINE
    i = 1

    while (startLine < TOTAL_NUMBER_OF_LINES):

        data = readLines(startLine, POSTS_IN_ONE_FILE, INPUT_FILE_PATH)
        data = START_FILE_STRING +  data + END_FILE_STRING
        writeToFile(data, OUTPUT_FILE_PATH + str(i) + '.xml')

        startLine = startLine + POSTS_IN_ONE_FILE
        i+=1







