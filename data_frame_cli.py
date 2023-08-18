# Author: Ryan Baker
import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt

def print_heading(text):
    """Prints text with special formatting.

        text(str): Text to be printed as heading
    """
    print('\n{} {} {}\n'.format('*'*3, text, '*'*3) )

def print_shape(csv_filename, df):
    """Prints csv filename and shape of df.

        csv_filename(str): File name corresponding to df
        df (pandas.DataFrame): DataFrame to get the shape of
    """
    print_heading('df.shape')
    print('{} loaded with shape {}'.format(csv_filename, df.shape))

def print_head(head, df):
    """Prints the DataFrame head of the dataframe object.

        head (bool): True if the cli argument -t or --head was passed, false otherwise.
        df (pandas.DataFrame): DataFrame to get the head of.
    """
    if head:
        print_heading('df.head()')
        print(df.head())


def print_info(info, df):
    """Prints the DataFrame info of the dataframe object.

        info (bool): True if the cli argument -i or --info was passed, false otherwise.
        df (pandas.DataFrame): DataFrame to get the head of.
    """
    if info:
        print_heading('df.info()')
        print(df.info())

def print_describe(describe, df):
    """Prints the summarized columns of the dataframe object.

        describe (list): List of column names to summarize. If no names are specified, all columns will be summarized.
        df (pandas.DataFrame): DataFrame to get the head of.
    """
    if describe==None:
        pass
    # if COLUMN_NAME has 0 elements, then -d was passed
    elif len(describe) == 0:
        print_heading('df.describe()')
        print(df.describe())

    # pytest uses a string in the test, but COLUMN_NAME is a list object. This passes pytest.
    elif(isinstance(describe, str)):
        if df.get(describe) is None:
            print(f'df.describe() failed.{describe} not found')
            return
        else:
            pass
        print(df[describe].describe())
        
    # if COLUMN_NAME has more than 0 elements, a column name has been specified.
    else:
        for col in describe:
            if df.get(col) is None:
                print(f'{col} not found')
                return                
            else:
                pass         
        print_heading('df.describe()')
        print(df[describe].describe())


def cli(args=None):
    """Main function: Connects argument parser to functions

        The csv file is a mandatory argument and is opened and read into a 
        pandas.DataFrame here. Handles file errors.

        Arguments and DataFrame are passed to corresponding functions for printing.

        args(list(str)): List of strings to be parsed as arguments.
                         If None, sys.argv is used.
    """
    if args is not None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Inspecting csv files with Pandas DataFrame methods.",formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('csv_filename', help='A (nice) csv file.')
    parser.add_argument('-t', '--head', action='store_true', help='print dataframe head.')
    parser.add_argument('-i', '--info', action='store_true', help='print dataframe info.')
    parser.add_argument('-d', '--describe', action='store', dest='COLUMN_NAME', nargs='*', help='''Print dataframe statistics. If COLUMN_NAME provided,\nprint statistics of selected column only.''')

    args = parser.parse_args(args)

    # File might not exist, be of wrong format
    try:
        df = pd.read_csv(args.csv_filename)
    except:
        print('There was an error reading {}'.format(args.csv_filename))
        print('Make sure file is present, readable, and formatted as csv.')
        exit()

    print_shape(args.csv_filename, df)
    #TODO: call functions corresponding to other arguments
    print_head(args.head, df)
    print_info(args.info, df)
    print_describe(args.COLUMN_NAME, df)

if __name__ == '__main__':
    cli()
