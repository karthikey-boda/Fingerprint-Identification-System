from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from utils.preprocess import preprocess_image
from utils.feature_extractor import extract_features
from utils.enroll import save_template
from utils.matcher import match_fingerprint
from utils.database import init_db, add_user, voter_exists

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

init_db()


@app.route("/")
def home():
    return "Fingerprint Identification API Running"


@app.route("/upload", methods=["POST"])
def upload():

    # Get Voter ID
    voter_id = request.form.get("voter_id", "").strip()

    if voter_id == "":
        return jsonify({
            "status": "error",
            "message": "Please enter Voter ID."
        }), 400

    # Check fingerprint uploaded
    if "fingerprint" not in request.files:
        return jsonify({
            "status": "error",
            "message": "Please upload a fingerprint."
        }), 400

    file = request.files["fingerprint"]

    if file.filename == "":
        return jsonify({
            "status": "error",
            "message": "Please upload a fingerprint."
        }), 400

    # Save uploaded image
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Preprocess image
    processed_path = preprocess_image(filepath)

    # Extract ORB features
    keypoints, descriptors = extract_features(processed_path)

    if descriptors is None:
        return jsonify({
            "status": "error",
            "message": "No fingerprint features detected."
        })

    # Match fingerprint
    matched_user, score, similarity = match_fingerprint(descriptors)

    print("================================")
    print("Matched User :", matched_user)
    print("Score        :", score)
    print("Similarity   :", similarity)
    print("================================")

    # Fingerprint already exists
    if matched_user is not None:
        return jsonify({
            "status": "found",
            "message": "Fingerprint already exists.",
            "voter_id": matched_user,
            "score": score,
            "similarity": similarity
        })

    # Prevent duplicate voter IDs
    if voter_exists(voter_id):
        return jsonify({
            "status": "duplicate",
            "message": "This Voter ID is already registered."
        })

    # Enroll new fingerprint
    save_template(voter_id, descriptors)
    add_user(voter_id)

    return jsonify({
        "status": "enrolled",
        "message": "New fingerprint enrolled successfully.",
        "voter_id": voter_id
    })


if __name__ == "__main__":
    app.run(debug=True)