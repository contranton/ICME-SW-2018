"""
Scripts to implement various algorithms seen in the ICME Summer Workshop, Santiago 2018
"""
import pandas

class Cluster():
    def __init__(self, data):
        self.data = data
        self.N, self.dim = data.shape
        self.centroid = self.get_centroid()

    def get_centroid(self):
        return self.data.sum(0)/self.N
            

class KMeans():
    def __init__(self, data_file):
        self.data = self.read_data(data_file)
        self.classes = {}

    def read_data(self, filename):
        return pandas.read_table(filename, sep=",")

    def calculate_centroids(self):
        for cls in self.classes.values():
            cls.get_centroid()

    def initialize_random_clusters(self, k):
        temp_d = self.data.copy()
        for i in range(k):
            # Generate sample with 1/k percentage of elements
            cls = Cluster(temp_d.sample(frac=1/(k-i)))
            self.classes[i] = cls

            # Get the complement
            temp_d = temp_d.drop(temp_d.index[list(cls.data.index)])

if __name__ == '__main__':
    d = KMeans("data/s1.txt")
    d.initialize_random_clusters(5)
    
