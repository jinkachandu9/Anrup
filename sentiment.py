# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from textblob import TextBlob
test = "3 Best ICICI Prudential Mutual Fund Schemes With 3-year ...https"


def read_sheet(test):
    result = TextBlob(test)
    result = result.polarity + result.subjectivity
    return result