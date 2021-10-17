import tweepy


def authenticate(settings):
    auth = tweepy.OAuthHandler(settings.get("consumer_key"), settings.get("consumer_secret"))
    auth.set_access_token(settings.get("token"), settings.get("token_secret"))
    print("Authentication successful.")
    return tweepy.API(auth, wait_on_rate_limit=True)


def get_user_obj(api, handle):
    try:
        return api.get_user(screen_name=handle)
    except tweepy.TweepyException as e:
        for api_code in e.api_codes:
            if api_code == 63:
                print(f'{handle} is suspended. Skipping...')


def get_num_followers(user_obj):
    return user_obj.followers_count


def get_num_tweets(user_obj):
    return user_obj.statuses_count
