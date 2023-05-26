import argparse

def main():
    parser = argparse.ArgumentParser(description='File Exterminator')
    parser.add_argument('file', help='Specify path to the file that needs to be securely deleted.')
    
    args = parser.parse_args()
    path_to_file = args.file

    print(path_to_file)

    confirm_delete = input(f'Please confirm to if want to delete file "{path_to_file}". (y/n): ')
    if confirm_delete.lower() != 'y':
        print('Canceled file deletion. Nothing happened.')
        return

    # TODO: Now need to write the actual logic
    print('After fil deleted')

if __name__ == "__main__":
    main()