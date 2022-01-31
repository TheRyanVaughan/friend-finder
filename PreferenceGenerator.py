import pandas as pd

class PreferenceGenerator:
    def __init__(self, data):
        self.data = data
    def run(self):
        self.__make_rankings()
    def __make_rankings(self):
        '''
        Make the rankings based on a dissimilarity metric.
        Generate a score for this user with every other user, then make a list in sorted order of preferences.
        Probably helps to make a user data type to keep all of their question answers together.
        EX: Simply pass two user objects around rather than indices and the data

        :return:
        '''
        pass

