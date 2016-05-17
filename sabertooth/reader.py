
import pandas as pd
import os


data_path = "data/core"


class BaseballStats(object):

    def load_data(self):
        self.data = dict()
        for fname in os.listdir(data_path):
            key = fname.split(".")[0]
            self.data[key] = pd.read_csv(data_path + "/" + fname)
        return self

    def get_data(self):
        return self.data

    def get_table(self, key):
        return self.data[key]

    def merge(self, left, right):
        return self.data[left].merge(self.data[right])
