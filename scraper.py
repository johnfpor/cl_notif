import json
import urllib

results = json.load(urllib.urlopen("https://www.kimonolabs.com/api/ds2da4og?apikey=your_api_key_here"))
data = results['results']['collection1']

latest_post = int(open('latest_post.txt').read())
max_topic = latest_post
new_posts = []

sub = "http://sfbay.craigslist.org/sfc/bik/"
       
for post in data:
	ad_id = int(post['title']['href'][len(sub):][:-5])
	if ad_id > latest_post:
		latest_post = ad_id
		new_posts.append(post['price']['text'] + " " + post['title']['text'] + " " + post['title']['href'] + " " + post['area'])
					
with open('latest_post.txt', 'w') as f:
    f.write(str(latest_post))
    
print latest_post
print new_posts

from twilio.rest import TwilioRestClient 
 
ACCOUNT_SID = "your_sid_here" 
AUTH_TOKEN = "your_suth_here" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

for npost in new_posts: 
	client.messages.create(
		to="receiving_number_here", 
		from_="twillio_sending_number_here", 
		body=npost,  
	)

print len(data)	
print len(new_posts)
