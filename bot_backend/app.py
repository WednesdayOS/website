from flask import Flask, send_file, request
import os
from send_mail import email_token, register
from account_operations import get_unfollowers
from wos_auth import generate_token, authenticate

app = Flask(__name__)

@app.route('/gen_co', methods=['POST'])
def gen_co():
    requested_username = request.args.get('username')
    authenticate(requested_username)
    user_status = "1"
    with open(f"accounts/{requested_username}/status.txt", 'r') as file:
        user_status = file.read()
    
    if user_status == "0":
        generate_token(requested_username)
        email_token(requested_username)

@app.route('/get_2fa', methods=['GET'])
def get_2fa():
    requested_username = request.args.get('username')
    authenticate(requested_username)
    user_status = "1"
    with open(f"accounts/{requested_username}/status.txt", 'r') as file:
        user_status = file.read()
    if user_status == "0":
        returned_file = f"accounts/{requested_username}/login_token.txt"
        return send_file(returned_file, as_attachment=True)
    else:
        return send_file("beans.txt", as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
