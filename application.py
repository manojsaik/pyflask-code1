from flask import Flask, render_template, request
#import openai
import datetime 

application = Flask(__name__)

@application.route("/", methods=("GET", "POST"))
def root():
    return 'Howday!! its working check /time to find current time'

@application.route("/time", methods=("GET", "POST"))
def time():
    local_timezone = str(datetime.datetime.utcnow().astimezone().tzinfo)
    now = str(datetime.datetime.now())+' '+local_timezone
    #print(now)
    return now

if __name__ == '__main__':
    app.run(port=8000,debug=True)
