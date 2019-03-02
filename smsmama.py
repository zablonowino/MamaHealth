import africastalking
import pprint


username = "sandbox"
api_key = "27eeb6aaa31b1014d3f68a42016a97f172190aefc7ae70b6e55f62f1726916f8"
africastalking.initialize(username,api_key)

sms = africastalking.SMS
message = 'habari mama'
        
response = sms.send(message,['+254727544483'])
pprint.pprint(response)

        
