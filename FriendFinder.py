import pandas as pd

class FriendFinder:
    def run(self):
        data = self.load_data()
        preferences = self.generate_preferences(data)
        pairings = self.pair_friends()

    def load_data(self):
        csv = pd.read_csv("data/form_data.csv")
        return csv

    def generate_preferences(self, data):
        pass

    def pair_friends(self):
        pass