#https://realpython.com/python-logging/
import logging;
import glob;
import os;
import gzip;


# Dataset
search_pattern='>111<';
input_file_path='input';
output_file_path='output';
output_file_name='snapshot.txt';
directory_pattern='*.gz';


def main():
    print('Start');
    clean_output_directory();
    for file in find_files(): process_file(file);
    print('Stop');

def clean_output_directory():
    files = glob.glob(output_file_path+os.sep+'*')
    for f in files: os.remove(f)

def process_file(file_name):

    if '.gz' in file_name:
        file=process_gz_file(file_name);
    else :
        file =process_txt_file(file_name);
    file.close();


def process_gz_file(file):
    with gzip.open(file, 'rb') as f:
        f=process_txt_file(f)
    return f;


def process_txt_file(file):
    dataset = [];
    for line in file:
        line = line.decode('utf-8').rstrip('\r\n');
        if search_pattern in line: dataset.append(line);
    process_data_to_output(dataset);
    return file;


def process_data_to_output(dataset):
    file = open(output_file_path+os.sep+output_file_name,'a')
    for data in dataset:file.write(data+'\n');
    file.close();


def find_files():
    files=glob.glob(input_file_path+os.sep+directory_pattern);
    return files;


if __name__ == "__main__":main()