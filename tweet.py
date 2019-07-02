import twitter
import random
from crontab import CronTab
# get Twitter followers

api = twitter.Api(consumer_key='ktSErpirBZRAE3UbCc8qs1tK9',
                      consumer_secret='hsRGKJPH7IcjpectLHQjXMUtiufugsC2VqW1gKQf1zOi0NRZl6',
                      access_token_key='338600510-Gg5XIODTYjpGqO35weF2y1DfBoM6U5R3eVzjzW6y',
                      access_token_secret='MvNnAr9cOnWddVQf1yHBQyTrf1ZAjZ732OEm4MYz9MjYv')


followers = api.GetFollowers()
# print([u.name for u in followers])
# print(len(followers))

# pick one at random 

randomIndex=random.randint(0,(len(followers)-1))

randomFollower= followers[randomIndex]

# print(randomFollower.screen_name)

# Tweet at random follower

tweet = "@{} you are the random follower of the day".format(randomFollower.screen_name)

api.PostUpdate(tweet)
print(tweet)
print("Thanks for tweeting")
