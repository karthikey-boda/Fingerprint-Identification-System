import numpy as np
import os

TEMPLATE_FOLDER = "templates"

os.makedirs(TEMPLATE_FOLDER, exist_ok=True)


def save_template(user_id, descriptors):
    """
    Save fingerprint descriptors as a NumPy file.
    """

    filepath = os.path.join(
        TEMPLATE_FOLDER,
        f"{user_id}.npy"
    )

    np.save(filepath, descriptors)

    return filepath