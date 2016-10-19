import flask from Flask, render_template
import apiai
import json

app = Flask(__name__)

@app.route('/'):
def hello_world():
    return (render_template('index.html'))

def main():
    ai = apiai.ApiAI('68a530a5164d4f4fab7b044398f99ebd')

    while True:
        user_input = raw_input("me: ")
        if user_input == 'exit':
            print "bot: Thank you and come again"
            break

        request = ai.text_request()
        request.query = user_input
        response = json.loads(request.getresponse().read())
        result = response['result']
        fulfillment = result.get("fulfillment")
        print "bot: " + fulfillment['speech']

if __name__ == '__main__':
    app.run(debug=True)
