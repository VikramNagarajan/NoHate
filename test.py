from flask import Flask
from flask import Flask, render_template, request
import requests
from hatesonar import Sonar
import json
app = Flask(__name__)

@app.route('/pass_val',methods=['GET', 'POST'])
def pass_val():
    name=request.args.get('value')
    sonar = Sonar()
    f = open('popup.html', 'w')
    resultHate = float(sonar.ping(text=str(name))['classes'][0]['confidence'])
    resultOff = float(sonar.ping(text=str(name))['classes'][1]['confidence'])
    print(resultHate, resultOff)
    if resultHate >= 0.40:
        result = 'could be categorized as hate speech.'
    elif resultOff >= 0.40:
        result = ' could be categorized as offensive language.'
    else:
        result = ' was not flagged as either hate speech or offensive language.'
    default = ''' <style>
   
.quote {
    color: #4585F4;
}

.pad {
    padding-top: 10px;
    padding-bottom: 10px;
    padding-right: 10px;
    padding-left: 10px;

}

</style>

<div>

    '''

    f.write(default + '<div class="pad"><h2 class="quote"><b>' + '"' + name + '"' + '</b></h2>' + '<h2 class="result">' + result + '</h2></div>')
    f.close()
    f = open('data.json', 'w')
    f.write(json.dumps({"message": "'" + name + "'" + result}))
    f.close()
    return 'success'
@app.route('/get_data', methods=['POST'])
def home():
    f = open('popup.html', 'r')
    x = f.read()
    f.close()
    return x


if __name__ == '__main__':
    app.run(debug=True)