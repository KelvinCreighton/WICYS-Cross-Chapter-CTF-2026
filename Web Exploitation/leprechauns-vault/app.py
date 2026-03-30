"""
CTF Web Challenge: "Leprechaun's Vault"
==============================
A secret pot-of-gold portal with a backdoor left in by a careless leprechaun dev.

Run:
    pip install flask
    python3 app.py

Then visit http://localhost:5000
"""

from flask import Flask, request, jsonify, render_template
import base64

app = Flask(__name__)

FLAG = "WICYS{p0t_0f_g0ld_4cquir3d_m8}"

# The known employee email (given to players in the challenge brief)
TARGET_EMAIL = "shamrock@leprechaun-vault.net"

# ----------------------------------------------------------------
# Hint hidden in the HTML:
# base64 encode of: "DEV NOTE (finn): quick backdoor for load testing
# - add header 'X-Leprechaun-Token: lucky-charm' to skip auth. remove before prod!!"
#
# Encoded: REVWIE5PVEUgKGZpbm4pOiBxdWljayBiYWNrZG9vciBmb3IgbG9hZCB0ZXN0aW5nIC0gYWRkIGhlYWRlciAnWC1MZXByZWNoYXVuLVRva2VuOiBsdWNreS1jaGFybScgdG8gc2tpcCBhdXRoLiByZW1vdmUgYmVmb3JlIHByb2QhIQ==
# ----------------------------------------------------------------

HINT_B64 = base64.b64encode(
    b"DEV NOTE (finn): quick backdoor for load testing"
    b" - add header 'X-Leprechaun-Token: lucky-charm' to skip auth."
    b" remove before prod!!"
).decode()

@app.route('/')
def index():
    return render_template('index.html', hint=HINT_B64)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    email = data.get('email', '')
    internal_token = request.headers.get('X-Leprechaun-Token', '')

    # Backdoor: correct email + secret header bypasses password check
    if email == TARGET_EMAIL and internal_token == 'lucky-charm':
        return jsonify(success=True, flag=FLAG)

    # Normal auth (no valid password exists — intentionally impossible)
    return jsonify(success=False, message='Invalid credentials'), 401

if __name__ == '__main__':
    print("\n  Leprechaun's Vault CTF Challenge")
    print("  Running at http://localhost:5000\n")
    app.run(debug=False, host='0.0.0.0', port=5000)
