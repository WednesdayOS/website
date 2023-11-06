from flask import Flask, send_file, request, abort
from send_mail import email_token, register
from account_operations import get_unfollowers
from wos_auth import generate_token, authenticate

app = Flask(__name__)

@app.route('/gen_co', methods=['GET'])
def gen_co():
    requested_username = request.args.get('username')
    authenticate(requested_username)
    user_status = "1"
    with open(f"accounts/{requested_username}/status.txt", 'r') as file:
        user_status = file.read()
    if user_status == "0":
        generate_token(requested_username)
        email_token(requested_username)
        abort(200)
    else:
        abort(403)

@app.route('/auth', methods=['GET'])
def auth():
    requested_username = request.args.get('username')
    e_token = request.args.get('etoken')
    print(f"user provided token: {e_token}")
    authenticate(requested_username)
    user_status = "1"
    real_token = ""
    with open(f"accounts/{requested_username}/status.txt", 'r') as file:
        user_status = file.read()
    with open(f"accounts/{requested_username}/login_token.txt", 'r') as file:
        real_token = file.read()
        print(f"actual token: {real_token}")
    if user_status == "0" and real_token == e_token:
        abort(200)
    else:
        abort(403)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
