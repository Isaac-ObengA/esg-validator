import hashlib
import json
REQUIRED_FIELDS = ["emissions", "energy_use", "governance_score"]
def validate_format(data: dict) -> dict:
    missing = [field for field in REQUIRED_FIELDS if field not in data or not data[field]]
    return {
        "valid": len(missing) == 0,
        "missing_fields": missing  }
def generate_hash(data: dict) -> str:
    json_data = json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(json_data).hexdigest()
def validate_and_hash(data: dict) -> dict:
    validation = validate_format(data)
    if validation["valid"]:
        data_hash = generate_hash(data)
        return {"status": "pass", "hash": data_hash}
    else:
        return {"status": "fail", "errors": validation["missing_fields"]}
