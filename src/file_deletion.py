import os
import random


class FileDeletion:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def securely_delete(self):
        # Decided to initially implement the DoD 5220.22-M method
        # https://www.jetico.com/blog/dod-522022-m-explained-data-erasure-standards
        # 0, 1, R, 0, 0, 1, R
        self.write_zeros()
        self.write_ones()
        self.write_random_data()
        self.write_zeros()
        self.write_zeros()
        self.write_ones()
        self.write_random_data()
        os.remove(self.path_to_file)

    def write_zeros(self):
        orig_size = os.path.getsize(self.path_to_file)
        with open(self.path_to_file, 'wb') as f:
            f.write(b'\x00' * orig_size)

    def write_ones(self):
        orig_size = os.path.getsize(self.path_to_file)
        with open(self.path_to_file, 'wb') as f:
            f.write(b'\xFF' * orig_size)

    def write_random_data(self):
        orig_size = os.path.getsize(self.path_to_file)
        with open(self.path_to_file, 'wb') as f:
            random_data = bytes([random.randint(0, 255)
                                for i in range(orig_size)])
            f.write(random_data)
