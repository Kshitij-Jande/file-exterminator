import argparse

def main():
    parser = argparse.ArgumentParser(description='File Exterminator')
    parser.add_argument('file', help='Specify path to the file that needs to be securely deleted.')
    
    args = parser.parse_args()
    path_to_file = args.file

    print(path_to_file)

if __name__ == "__main__":
    main()