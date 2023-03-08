#!/usr/bin/python
import os

paths = '/home/madsen/codespace/frameworks/keras/dataset/train'

files_found = []
iterator = 0


def traverse(path):
    global files_found

    for root, dirs, files in os.walk(path):
        for f in files:
            current_file = os.path.join(root, f)
            files_found.append(current_file)


def iterate(paths):
    global iterator

    for path in paths:
        iterator = iterator + 1

        base = os.path.basename(path)
        extension = os.path.splitext(base)[1]

        artefact_name = str(iterator) + extension
        directory_path = os.path.dirname(path)
        full = os.path.join(directory_path, artefact_name)

        print("renamed to: " + full)
        os.rename(path, full)


def main():
    global paths, files_found
    traverse(paths)
    iterate(files_found)


if __name__ == '__main__':
    main()