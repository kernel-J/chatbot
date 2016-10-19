from flask import Flask, render_template, request
import apiai
import json

app = Flask(__name__)
ai = apiai.ApiAI('68a530a5164d4f4fab7b044398f99ebd')

@app.route('/', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        ret = main(request.form['user_input'])
        return (echo(ret))
    else:
        return (render_template('index.html'))

def echo(resp):
    if resp != '':
        return (render_template('index.html', ret=resp))

def main(user_input):
    if user_input == 'exit':
        return ("Thank you and come again")

    request = ai.text_request()
    request.query = user_input
    response = json.loads(request.getresponse().read())
    result = response['result']
    fulfillment = result.get("fulfillment")
    return (fulfillment['speech'])

'''def main():
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
'''
if __name__ == '__main__':
    app.run(debug=True)
    #main()
