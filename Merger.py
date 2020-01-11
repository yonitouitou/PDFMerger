import sys
import os
from os import path

from PyPDF2 import PdfFileMerger


def get_files_to_merge(folder_path):
    files_to_merge = []
    for file in sorted(os.listdir(folder_path)):
        if file.endswith(".pdf") or file.endswith(".PDF"):
            files_to_merge.append(folder_path + os.path.sep + file)

    return files_to_merge


def merge_files(folder_path, merged_file_path):
    if path.exists(folder_path):
        files_to_merge = get_files_to_merge(folder_path)

        merger = PdfFileMerger()

        print("Merging %i PDF files..." % len(files_to_merge))
        i = 1
        for pdf in files_to_merge:
            print("(%i/%i) Merging %s" % (i, len(files_to_merge), path.abspath(pdf)))
            merger.append(pdf)
            i = i + 1

        merger.write(merged_file_path)
        merger.close()
        print("Merged file is %s" % merged_file_path)

    else:
        print("The folder %s does not exist." % folder_path)


def show_manual():
    print("Arguments format should be <folder_path> <merged_file_name>")


if __name__ == '__main__':

    if len(sys.argv) != 3 or sys.argv[1] == 'man' or sys.argv[1] == '--man':
        show_manual()
    else:
        folder_path = sys.argv[1]
        merged_file_name = sys.argv[2]
        merged_file_path = folder_path + os.path.sep + merged_file_name
        merge_files(folder_path, merged_file_path)





