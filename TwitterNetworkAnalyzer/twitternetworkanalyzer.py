from datetime import datetime
import db
import data
import twitter


def main():
    # get settings and authenticate twitter
    settings = data.get_settings('settings.ini')
    api = twitter.authenticate(settings)
    # get current date
    now = datetime.now()
    date = now.strftime("%m/%d/%Y")
    # get accounts from excel sheet
    accounts_df = data.get_accounts(file=settings.get('excel_file'), sheet=settings.get('accounts_sheet_name'))
    accounts_dict = data.df_to_custom_dictionary(accounts_df)
    # db initialization
    connection = db.get_connection(settings.get('db_name'))
    cursor = db.get_cursor(connection)
    db.create_summary_table(cursor)
    db.create_accounts_table(cursor)
    # iterate over account networks
    for network in accounts_dict:
        total_followers = 0
        total_tweets = 0
        account_list = accounts_dict.get(network)
        # iterate over each account in network
        for account in account_list:
            print(f"Grabbing {account}'s data...")
            user = twitter.get_user_obj(api, account)
            if user:
                num_followers = twitter.get_num_followers(user)
                num_tweets = twitter.get_num_tweets(user)
            # user is suspended
            else:
                num_followers = 0
                num_tweets = 0
            # insert user data into account row in db
            db.insert_accounts_row(cursor, date, network, account, num_followers, num_tweets)
            # add user data to totals to be used in summary table
            total_followers += num_followers
            total_tweets += num_tweets
        # insert each network's summary data into summary table
        db.insert_summary_row(cursor, date, network, total_followers, total_tweets)
    db.save_and_close(connection)


if __name__ == '__main__':
    main()
