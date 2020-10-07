import requests 
import json
 
# # Making a get request 
# # response = requests.get('https://www.reddit.com/subreddits/mine/subscriber.json',  headers = {'User-agent': 'your bot 0.1'}) 
  
# # # print response 
# # print(response) 
# # print(response.status_code)
# # # print json content 
# # print(response.json()) 

# # token=request.GET['code']
# requests.POST(https://www.reddit.com/api/v1/access_token)
# headers = {"Authorization":"bearer 608252225708-8kug_Kc9bV4mXba447T2gpPJxN0", "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
# response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
# # myjson=json.loads(response.json())
# print(response.json()['name'])
# # print(response['name'])


# client_auth = requests.auth.HTTPBasicAuth("SVkL9p1vQmhKUw", "s42UWMRwSQwQmXvvPuT654DXhcE")
		
# post_data = {"grant_type": "authorization_code","code": "TVOvXRKPANp_KgxyVGG3fbP8-Mg","redirect_uri": "http://127.0.0.1:8000/"}
# print(client_auth)
# headers={"User-Agent":"xyz"}
# response = requests.post("https://www.reddit.com/api/v1/access_token",auth=client_auth,data=post_data, headers=headers)	
# token_json = response.json()
# print(response.headers)
# print(token_json)

headers={'User-Agent':"jpj"}
response = requests.get("https://www.reddit.com//users/popular.json", headers=headers)
data={}		
myjson=json.loads(response.text)
print(myjson)
index=0;
for x in myjson.get('data').get('children'):
	data[index]=x.get('data').get('display_name_prefixed')[2:]
	index=index+1


print(len(data))