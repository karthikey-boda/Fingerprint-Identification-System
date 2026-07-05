import os
import cv2
import numpy as np

TEMPLATE_FOLDER = "templates"

MATCH_DISTANCE = 50
MATCH_THRESHOLD = 75.0


def match_fingerprint(query_descriptors):

    if query_descriptors is None:
        return None, 0, 0

    if not os.path.exists(TEMPLATE_FOLDER):
        os.makedirs(TEMPLATE_FOLDER)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    best_user = None
    best_score = 0
    best_similarity = 0

    for file in os.listdir(TEMPLATE_FOLDER):

        if not file.endswith(".npy"):
            continue

        voter_id = file.replace(".npy", "")

        stored_descriptors = np.load(
            os.path.join(TEMPLATE_FOLDER, file),
            allow_pickle=True
        )

        if stored_descriptors is None or len(stored_descriptors) == 0:
            continue

        matches = bf.match(query_descriptors, stored_descriptors)

        good_matches = [
            m for m in matches if m.distance < MATCH_DISTANCE
        ]

        score = len(good_matches)

        similarity = (
            score /
            max(len(query_descriptors), len(stored_descriptors))
        ) * 100

        print("--------------------------------")
        print("Checking:", voter_id)
        print("Good Matches:", score)
        print("Similarity:", round(similarity, 2))
        print("--------------------------------")

        if similarity > best_similarity:
            best_similarity = similarity
            best_score = score
            best_user = voter_id

    # Reject weak matches
    if best_similarity < MATCH_THRESHOLD:
        return None, 0, 0

    return best_user, best_score, round(best_similarity, 2)