# import libraries 
import sys
import pandas as pd
import numpy as np
import sqlite3
import sqlalchemy
from sqlalchemy import create_engine


def load_data(disaster_messages, disaster_categories):
    """
    This function loads and merges datasets from 2 different files.
    
    Files:
    disaster_messages: messages csv file
    disaster_categories: categories csv file
    
    Returns:
    df: dataframe containing disaster_messages and disaster_categories combined
    
    """
    # load datasets
    messages = pd.read_csv(disaster_messages)
    categories = pd.read_csv(disaster_categories)
    # merge datasets on common id and assign to df
    df = messages.merge(categories, how ='outer', on =['id'])
    return df


def clean_data(df):
    """
    This function cleans the dataframe loaded before.
    
    Files:
    df: DataFrame
    
    Returns:
    df: Cleaned DataFrame
    
    """
    ##Creting the splitted dataframe
    categories = df['categories'].str.split(';', expand=True)
    #Selecting the first row of the categories dataframe
    row = categories.head(1)
    #Using this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    category_colnames = row.applymap(lambda x: x[:-2]).iloc[0,:]
    #Renaming the columns of categories dataframe
    categories.columns = category_colnames
    
    # iterate through the category columns in df to keep only the
    # last character of the string 
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1]
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    # replace 2s with 1s in related column
    categories['related'] = categories['related'].replace(to_replace=2, value=1)
        
    # drop the original categories column from `df`
    df.drop('categories', axis=1, inplace=True)
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)
    # drop duplicates
    df.drop_duplicates(inplace=True)
    return df


def save_data(df, Disaster_Response):
    """This function stores the cleaned df in a SQLite database."""
    engine = create_engine('sqlite:///Disaster_Response.db')
    df.to_sql('disaster_categories', engine, index=False, if_exists='replace')

def main():
    if len(sys.argv) == 4:

        disaster_messages, disaster_categories, Disaster_Response = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(disaster_messages, disaster_categories))
        df = load_data(disaster_messages, disaster_categories)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(Disaster_Response))
        save_data(df, Disaster_Response)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()