import requests
import os
import json
import tweepy as tw

consumer_key = 'bCs3KjDixkdgew0WrHXTGDPe1'
consumer_secret = 'iCY2EIFUUOMzpAUEa7JXWYhu9xjg8gqXXp2rhacsAPGrqnaJ0Y'
access_token = '1358710907006779398-ztYTwvVQyJWKRKOqF4IaeHwhzfmtpz'
access_token_secret= 'cBqB48bge67Iysm10FJGqSdzo1WPkLrAu0HEjWfsPZ7mb'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAE2cMgEAAAAAxuksyrty6gvuuLMm6keHIr7cq8o%3DNMOcO1jCAKG4R22MPYQvFGJladaeGZDlPnUXDfNwj5HglKMJUS'


# auth.set_access_token(access_token, access_token_secret)
# api = tw.API(auth, wait_on_rate_limit=True)

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return os.environ.get("BEARER_TOKEN")
    # return tw.OAuthHandler(consumer_key, consumer_secret)


def create_url():
    tweet_fields = "tweet.fields=lang,author_id,text"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    text = "text=redistricting"
    ids = "44513878"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets.josn?q={}&{}&{}".format(ids, tweet_fields, text)
    return url
# 'https://api.twitter.com/1.1/search/tweets.json?q=from%3ACmdr_Hadfield%20%23nasa'

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()