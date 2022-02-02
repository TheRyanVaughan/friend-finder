import pandas as pd

from PreferenceGenerator import PreferenceGenerator


class FriendFinder:
    def run(self):
        data = self.load_data()
        preferences = self.generate_preferences(data)
        pairings = self.pair_friends()

    def load_data(self):
        csv = pd.read_csv("data/form_data.csv")
        return csv

    def generate_preferences(self, data):

        pref_generator = PreferenceGenerator(data)
        pref_generator.run()

    def pair_friends(self):
        pass

