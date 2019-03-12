#https://realpython.com/python-logging/
import logging;

logging.basicConfig(
        level=logging.INFO,datefmt='%d-%b-%y %H:%M:%S', filename='logs/scripts.log', filemode='w',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    logging.info('Start');
    read_file();
    logging.info('Stop');


def read_file():
    filepath='input/demo.xml';
    contents = [line.strip() for line in open(filepath, 'r').readlines()]
    data = "";
    for content in contents:
        data = data +content;
    print(data);
    logging.info(data);

if __name__ == "__main__":main()