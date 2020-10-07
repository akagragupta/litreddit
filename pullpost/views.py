from django.shortcuts import render
from django.http import HttpResponse
import requests
import requests.auth
import json
# Create your views here.


def get_token(code):
	client_auth = requests.auth.HTTPBasicAuth("SVkL9p1vQmhKUw", "s42UWMRwSQwQmXvvPuT654DXhcE")
	headers={"User-Agent":"xyz"}	
	post_data = {"grant_type": "authorization_code","code": code,"redirect_uri": "https://litreddit.herokuapp.com"}
	response = requests.post("https://www.reddit.com/api/v1/access_token",auth=client_auth,data=post_data,headers=headers)	
	token_json = response.json()
	accesstoken=token_json['access_token']
	return accesstoken


def popular_user():
	# headers = {"Authorization":"bearer "+accesstoken,  "User-Agent": "ChangeMeClient/0.1 by AkagraGupta"}
	headers={'User-Agent':"jpj"}
	response = requests.get("https://www.reddit.com//users/popular.json", headers=headers)

	data={}		
	myjson=json.loads(response.text)
		
	index=1;
	for x in myjson.get('data').get('children'):
		data[index]="https://www.reddit.com/user/"+x.get('data').get('display_name_prefixed')[2:]
		index=index+1
	
	return data


def top():
	# headers = {"Authorization":"bearer "+accesstoken,  "User-Agent": "ChangeMeClient/0.1 by AkagraGupta"}
	headers={'User-Agent':"jpj"}
	response = requests.get("https://www.reddit.com/r/aww/top.json", headers=headers)

	data={}		
	myjson=json.loads(response.text)
		
	index=1;
	for x in myjson.get('data').get('children'):
		data[index]="https://www.reddit.com/"+x.get('data').get('permalink')
		index=index+1
	
	return data



def get_name(accesstoken):
	headers = {"Authorization":"bearer "+accesstoken,  "User-Agent": "ChangeMeClient/0.1 by AkagraGupta"}
	response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
	myjson=json.loads(response.text)
	return myjson['name']



def home(request):
	data={}
	if(request.method=='GET'):
		code=request.GET['code']
		
		accesstoken=get_token(code)
		print(accesstoken+"...........................")

		# headers = {"Authorization":"bearer "+accesstoken,  "User-Agent": "ChangeMeClient/0.1 by AkagraGupta"}
		# response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)


		headers = {"Authorization":"bearer "+accesstoken,  "User-Agent": "ChangeMeClient/0.1 by AkagraGupta"}
		response = requests.get("https://oauth.reddit.com/r/trending_subreddits", headers=headers)

			
		myjson=json.loads(response.text)
		
		index=1;
		for x in myjson.get('data').get('children'):
			data[index]="https://www.reddit.com/"+x.get('data').get('permalink')
			index=index+1
		
		name=get_name(accesstoken);

		popuser={}
		popuser=popular_user();

		toppost={}
		toppost=top();


		for x in data:
			print(data[x])
		return render(request,'home.html',{'context': data, 'popuser':popuser, 'toppost':toppost,'username':name})

	else:
		print("404 page not found")
		return render(request,'404.html')

	
	

	
	


# def accesstoken(request):
# 	if(request.method=='POST'):
# 		token_json = resp.json()
# 		accesstoken=token_json["access_token"]

# 		headers = {"Authorization":"bearer "+accesstoken,  "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
# 		response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
		
# 		myjson=json.loads(response.json())
# 		print(myjson['name'])
# 	else:
# 		print("404 page not found")
# 		return render(request,'404.html')

# 	return render(request,'home.html')