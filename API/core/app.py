from flask import Flask, request, jsonify, render_template

from Dianping import Dianping
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
dianping = Dianping()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dianping/hotel')
def get_hotel_data():
    url = request.args.get('url')
    if url:
        result = dianping.get_hotel_info(url=url)
    return jsonify(result)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)