import studentclass
import os

def readAssignment():
    base_path = '.'
    source_path = base_path + '/source'

    source_list = os.listdir(source_path)

    for zip in source_list:
        zip_path = source_path + '/' + zip
        print(zip_path)

def main():
    readAssignment()    

if __name__ == "__main__":
    main()