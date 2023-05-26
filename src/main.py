import argparse
import os
from file_deletion import FileDeletion


def main():
    parser = argparse.ArgumentParser(description='File Exterminator')
    parser.add_argument('file', help='Specify path to the file that needs to be securely deleted.')

    args = parser.parse_args()
    path_to_file = args.file

    if not os.path.exists(path_to_file):
        print("That file doesn't exist. Please try again.")
        return

    confirm_delete = input(f'Please confirm if want to delete file "{path_to_file}". (y/n): ')

    if confirm_delete.lower() != 'y':
        print('Canceled file deletion. Nothing happened.')
        return

    FileDeletion(path_to_file).securely_delete()

    print(f'File {path_to_file} has been securely deleted.')
    print('The program will exit now.')


if __name__ == "__main__":
    main()
