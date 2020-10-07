from django.shortcuts import render
import praw
from django.contrib import messages
import requests
import requests.auth

# Create your views here.
def home(request):
	return render(request,'login.html')

# def login(request):
# 	if request.method=='POST':
# 		username=request.POST['username']
# 		password=request.POST['password']
# 		# reddit = praw.Reddit(client_id="SI8pN3DSbt0zor",client_secret="xaxkj7HNh8kwg8e5t4m6KvSrbTI",password="1guiwevlfo00esyy",
# 		# 	user_agent="testscript by u/fakebot3",username="fakebot3")
# 		client_auth = requests.auth.HTTPBasicAuth('SI8pN3DSbt0zor', 'xaxkj7HNh8kwg8e5t4m6KvSrbTI')
# 		post_data = {"grant_type": "password", "username":username, "password":password}
# 		headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
# 		response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
# 		response.json()
# 		# if(reddit.user.me()==username):
# 		# 	return render(request,'home.html')
# 		# else:
# 		# 	messages.info(request,'Invalid Credentials')
# 	else:
# 		return render(request,'login.html')
