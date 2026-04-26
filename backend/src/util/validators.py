import json
import os

validators = {}

def getValidator(collection_name: str):
    """
    Load MongoDB validator JSON file for a given collection.
    """

    if collection_name not in validators:

        base_dir = os.path.dirname(os.path.dirname(__file__))
        validator_path = os.path.join(
            base_dir,
            "static",
            "validators",
            f"{collection_name}.json"
        )

        with open(validator_path, "r") as f:
            validators[collection_name] = json.load(f)

    return validators[collection_name]