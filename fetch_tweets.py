import sys, tweepy
import csv
'''' authentication function '''
def twitter_auth():
    try:
        consumer_key = '**'
        consumer_secret = '**'
        access_token = '**'
        access_secret = '**'
    except KeyError:
        sys.stderr.write("TWITTER_* environment variable not set\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth

def get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth,wait_on_rate_limit=True)
    return client

if __name__ == '__main__':
    user = input("Enter username: ")
    client = get_twitter_client()
    with open('data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',')
        # writer.writerow(['text'])
        for status in tweepy.Cursor(client.home_timeline, screen_name=user).items(15): # change number in brackets for more tweets
            # print(status.text)
            writer.writerow([status.text]) # puts data in a csv file