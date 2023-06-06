from os.path \
    import \
    exists, \
    join, \
    splitext

from os \
    import \
    walk, \
    path

import os

root_path = r'/mnt/d/DataSets/ScreenshotAsDataset/uncategorised/1'


def get_directory(value):
    return path.dirname(
        path.realpath(
            value
        )
    )


def rename(
        directory_path: str,
        filename: str,
        fid: int
):
    split_file_name = splitext(filename)

    convert_fid = str(fid) + str(
        split_file_name[
            len(split_file_name) - 1
            ]
    )

    original = join(
        directory_path,
        filename
    )

    new_path = join(
        directory_path,
        convert_fid
    )

    print("original name:")
    print(original)

    print()

    print("new name:")
    print(new_path)

    print()

    os.rename(original, new_path)


def main():
    counter = 0

    for root, \
        dirs, \
        files \
            in walk(root_path, topdown=True):
        for file \
                in files:
            counter = counter + 1

            full_path = join(
                root,
                file
            )

            dir_path = get_directory(full_path)

            rename(
                dir_path,
                file,
                counter
            )


if __name__ == '__main__':
    if exists(root_path):
        print("Found Path: Will continue")
        main()
