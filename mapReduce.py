import time
import pymp


def fileWords(openFiles):
    fileList = []
    for file in openFiles:
        currentFile = []
        for line in file:
            for word in line.split():
                currentFile.append(word)
        fileList.append(currentFile)
    return fileList

def mapReduce(wordList, fileList):
    sharedDict = pymp.shared.dict()
    with pymp.Parallel() as p:
        lock = p.lock
        for fileWords in p.iterate(fileList):
            for word in fileWords:
                for listWord in wordList:
                    if listWord in word.lower():
                        lock.acquire()
                        if listWord not in sharedDict:
                            sharedDict[listWord] = 0
                        sharedDict[listWord] += 1
                        lock.release()
    return sharedDict


def main():

    words = ['hate', 'love', 'death', 'night', 'sleep', 'time', 'henry',
        'hamlet', 'you', 'my', 'blood', 'poison', 'macbeth', 'king', 'heart',
        'honest']

    fileNames = ['shakespeare1.txt', 'shakespeare2.txt', 'shakespeare3.txt', 'shakespeare4.txt',
    'shakespeare5.txt', 'shakespeare6.txt', 'shakespeare7.txt', 'shakespeare8.txt']

    files = []
    for file in fileNames:
        files.append(open(file, 'r'))

    start = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
    fileList = fileWords(files)
    result = mapReduce(words, fileList)
    end = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
    elapsed = end - start

    print('Frequency:')
    for word, freq in result.items():
        print(f'\t{word} - {freq}')

    print(elapsed)


if __name__ == '__main__':
    main()
