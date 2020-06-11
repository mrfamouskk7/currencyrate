import requests
from flask import Flask, request,render_template


app = Flask(__name__, static_url_path='/static')

@app.route('/exchange')
def convert():
    from1=request.args.get('cfrom')
    to1=request.args.get('cto')
    url=f'https://api.ratesapi.io/api/latest?base={from1}&symbols={to1}'
    response=requests.get(url).json()
    convert=response['rates'][f'{to1}']
    return f'1 {from1} is equal to {convert} {to1}'
        





@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
