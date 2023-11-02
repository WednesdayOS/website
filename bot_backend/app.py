from flask import Flask

app = Flask(__name__)

@app.route('/authenticate', methods=['GET'])
def authentication_process():
    pass #TBD

@app.route('/get_unfollowers', methods=['GET'])
def get_everything():
    pass #TBD

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
