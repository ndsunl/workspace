import struct
import datatime

def stock_csv(filepath, name):
    data = []
    with open(filepath, 'rb') as f:
        file_object = '/home/jackchen/data/stock_data/' + name + '.csv'