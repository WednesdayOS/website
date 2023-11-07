from flask import Flask, send_file, request, abort
from flask_cors import CORS
from send_mail import email_token, register
from account_operations import brain
from wos_auth import generate_token, authenticate
from user_management import check_if_user_exists, create_user

app = Flask(__name__)

cors_all = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/get_unfollowers_list', methods=['GET'])
def get_unfollowers_list():
    requested_username = request.args.get('username')
    exists = check_if_user_exists(requested_username)
    if exists == 1:
        brain(requested_username)
        try:
            file_path = f"accounts/{requested_username}/unfollowers.html"
            with open(file_path, 'r') as file:
                file_content = file.read()
            return file_content, 200
        except FileNotFoundError:
            abort(404)  
    else:
        abort(403)

@app.route('/register_user', methods=['GET'])
def register_user():
    requested_username = request.args.get('username')
    requested_email = request.args.get('email')
    exists = check_if_user_exists(requested_username)
    if exists == 1:
        abort(403)
    else:
        create_user(requested_username, requested_email)
        return "Request was successful", 200

@app.route('/is_registered', methods=['GET'])
def is_registered():
    requested_username = request.args.get('username')
    exists = check_if_user_exists(requested_username)
    if exists == 0:
        abort(403)
    else:
        return "Request was successful", 200

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
        return "Request was successful", 200
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
        return "Request was successful", 200
    else:
        abort(403)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
