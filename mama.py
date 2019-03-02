from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])






def ussd():
    session_id = request.values.get("sessionId",None)
    servicecode =  request.values.get("serviceCode",None)
    phone_number = request.values.get("phoneNumber",None)
    text = request.values.get("text",None)

    if text == "":
      response = "CON Congratulations You Have A Baby\n"
      response+= "1. Advice\n"
      response+= "2. Check Up Schedule\n"
    elif text == '1':
      response = 'CON Try Observing The Following:\n'
      response+='1. Go For Regular Checkups\n'
      response+='2. Eat Healthy \n'
      response+='3. Avoid Drugs And Alcohol\n'
      response+='0. Main Page'
    elif text == '2':
      response = 'CON Check Up Schedule:\n'
      response+='1. For The First 7 Months Go For Regular Checkups Monthly\n'
      response+='2. For The 8th And 9th Month Go Twice A Month\n'
      response+='3. After The 9th Month See You Doctor As Advised\n'
      response+='0. Main Page'
    elif text == '1*0' or text == '2*0':
               response = "CON Congratulations You Have A Baby\n"
               response+= "1. Advice\n"
               response+= "2. Check Up Schedule\n"
             #   text = '
    else:
        response = "END Invalid choice"

    return response

if __name__ == "__main__":
    	app.run(debug=True)
