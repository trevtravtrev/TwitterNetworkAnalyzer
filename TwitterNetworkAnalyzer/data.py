import configparser
import pandas


def get_settings(file):
    """
    Gets settings.ini settings into a dictionary.
    :param file: .ini file extension
    :return: settings dictionary
    """
    config = configparser.ConfigParser()
    config.read(file)
    settings = {
        'excel_file': config['Excel']['excel_file'],
        'accounts_sheet_name': config['Excel']['accounts_sheet_name'],
        'db_name': config['Excel']['db_name'],
        'consumer_key': config['Twitter']['consumer_key'],
        'consumer_secret': config['Twitter']['consumer_secret'],
        'token': config['Twitter']['token'],
        'token_secret': config['Twitter']['token_secret']
    }
    return settings


def get_accounts(file, sheet):
    """
    Gets twitter account network(s) from excel file.
    :param file: excel file extension
    :param sheet: excel sheet name
    :return: twitter account dataframe
    """
    return pandas.read_excel(file, sheet_name=sheet)


def df_to_custom_dictionary(dataframe):
    """
    Turns pandas dataframe into a usable dictionary where the keys are the networks and the values are lists of
    accounts {network: [accounts]}
    :param dataframe: accounts pandas dataframe
    :return: accounts dictionary {network:[accounts]}
    """
    accounts = {network: [] for network in dataframe}
    for network in dataframe:
        for index, account in dataframe[network].iteritems():
            if not pandas.isnull(account):
                accounts[network].append(account)
    return accounts
