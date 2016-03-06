import numpy as np
import pandas as pd
from . import wordCount as wc
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB

from .basic_utils import create_widget
from .basic_utils import extract_logbook_data
from .basic_utils import isolate_columns

from .config import *


class LogbookClassifier:

    def __init__(self):
        # extract data from zip file
        logbook_data = extract_logbook_data('CLIWOC15.csv')
        logbook_data = isolate_columns(logbook_data, desired_columns)

        # extract logs that mention slaves
        mentions_slaves = wc.count_key_words(logbook_data,
                                                text_columns, slave_words)
        slave_index = mentions_slaves[(mentions_slaves['ContainsKeyWord'] != 0)].index

        self.slave_logs = logbook_data.loc[slave_index.values]

        # temporarily using first 1000 logs as non-slave training set,
        # will replace this with something that actually makes sense
        self.not_slave_logs = logbook_data[:1000]

        # all remaining logs are unclassified (need to also remove non-slave log
        # training data indexes)
        self.unclassified_logs = logbook_data.drop(slave_index)

        # initialize multinomial naive bayes classifier
        self.classifier = MultinomialNB()


    def encode_data(self):
        """
        """
        encoder = MultiColumnLabelEncoder()
        _, self.slave_logs_enc, _ = MultiColumnLabelEncoder.transform(self.slave_logs)
        _, self.not_slave_logs_enc, _ = MultiColumnLabelEncoder.transform(self.not_slave_logs)
        _, self.unclassified_logs_enc, _ = MultiColumnLabelEncoder.transform(self.unclassified_logs)

    def fit_classifier(self):
        """
        Fit training data to classifier.
        """
        try:
            self.slave_logs_enc
        except:
            raise KeyError('Must encode data before fitting classifier')

        #self.classifier.fit(data, classes)


    def predict(self):
        """
        Predict class of remaining voyages.
        """
        data = ''
        self.classifier.predict(data)
