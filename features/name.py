import pandas as pd

# list of titles to find in names
from numpy import NaN

titles = ['Mr', 'Master', 'Miss', 'Mrs', 'Major', 'Ms', 'Mlle', 'Mee', 'Rev',
          'Dr', 'Col', 'Capt', 'Countess', 'Don', 'Jonkheer']


# utility function to find title in name
def title_in_name(name):
    for title in titles:
        if title in name:
            return title
    # return pd.NaN
    return NaN


# utility function to generalize titles
def generalize_titles(frame):
    title = frame['Title']
    if title in ['Mr', 'Don', 'Major', 'Capt', 'Jonkheer', 'Rev', 'Col']:
        return 'Mr'
    elif title in ['Master']:
        return 'Master'
    elif title in ['Countess', 'Mme', 'Mrs']:
        return 'Mrs'
    elif title in ['Mlle', 'Ms', 'Miss']:
        return 'Miss'
    elif title == 'Dr':
        if frame['Sex'] == 0:
            return 'Mrs'
        else:
            return 'Mr'
    else:
        return title


# utility function to create new column title and fill titles according to
# titles found i names
def create_title_columns(df):
    df['Title'] = df['Name'].map(lambda x: title_in_name(x))
    df['Title'] = df.apply(generalize_titles, axis=1)
    df = pd.concat([df, pd.get_dummies(df['Title'])], axis=1)
    return df
