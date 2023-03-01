from flask import Flask, render_template, request
#import openai
import datetime 

app = Flask(__name__)

@app.route("/movie-details", methods=("GET", "POST"))
def root():
    return 'No request setup for this route use other '

@app.route("/time", methods=("GET", "POST"))
def time():
    local_timezone = str(datetime.datetime.utcnow().astimezone().tzinfo)
    now = str(datetime.datetime.now())+' '+local_timezone
    #print(now)
    return now

if __name__ == '__main__':
    app.run( port=80 ,debug=True)
