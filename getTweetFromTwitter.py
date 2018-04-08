''' 
  Download tweet from twitter to get URL
'''
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

# We get this token from https://apps.twitter.com/ 
access_token="2564921978-ulEYwcTKFfPhRFJdDFkL4jQpTWKdFPViGFKxnoK"
access_token_secret="nYxnIYiBddLUYjKJ9zrUhpVwOFFEdQwbWiAfOS5t5I3hE"
consumer_key="MW9NovQYcXVPVzM6FWaKRv7H7"
consumer_secret="IXWq48EhicdosGjufs8hlv4AOxmPhHTs70YZLQSCVhyIo9g4HS"
class StdoutListener(StreamListener):
	def on_data(self,data):
		try:
			savefile= open("/home/guddu/Desktop/ML/tweetus.txt","a")
			savefile.write(data)
			#savefile.write('\n')
			savefile.close()
			return True
		except BaseException (e):
			print("Failed on data",str(e))
			time.sleep(5)

	def on_error(self,data):
			print(status)

obj = StdoutListener()
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
stream=Stream(auth,obj)
stream.filter(track=['us'])
