import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# استرجاع المفتاح السري المخصص للتحقق
SECRET_KEY = os.environ.get("ADMIN_SECRET_KEY", "default_secret")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "online", "message": "Amel Referral Service is running"}), 200

@app.route("/api/referral", methods=["POST"])
def process_referral():
    data = request.get_json() or {}
    auth_header = request.headers.get("Authorization")
    
    # التحقق من المصادقة
    if auth_header != f"Bearer {SECRET_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    user_id = data.get("user_id")
    referral_code = data.get("referral_code")

    if not user_id or not referral_code:
        return jsonify({"error": "Missing user_id or referral_code"}), 400

    # معالجة كود الإحالة
    return jsonify({
        "success": True,
        "message": "Referral processed successfully",
        "data": {
            "user_id": user_id,
            "referral_code": referral_code
        }
    }), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
