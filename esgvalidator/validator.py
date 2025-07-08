import hashlib
import json

def validate_esg_entry(entry: dict) -> tuple[bool, str]:
    """
    Validates an ESG entry by checking field presence and correct data types.

    Parameters:
    - entry (dict): The ESG data record.

    Returns:
    - tuple: (True, "Valid entry") if valid; (False, "Reason") if not.
    """
    required_fields = ["emissions_kg_co2e", "energy_use_mwh", "submitted_by"]

    for field in required_fields:
        if field not in entry:
            return False, f"Missing required field: {field}"

    if not isinstance(entry["emissions_kg_co2e"], (int, float)):
        return False, "Invalid emissions format"

    if not isinstance(entry["energy_use_mwh"], (int, float)):
        return False, "Invalid energy use format"

    return True, "Valid entry"


def generate_signature(entry: dict) -> str:
    """
    Creates a SHA-256 signature hash from an ESG entry.

    Parameters:
    - entry (dict): The ESG data to sign (excluding existing signature)

    Returns:
    - str: Hexadecimal hash of the serialized entry.
    """
    entry_for_signing = {k: v for k, v in entry.items() if k != "verifier_signature"}
    serialized = json.dumps(entry_for_signing, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()


def validate_and_sign(entry: dict) -> dict:
    """
    Validates an ESG entry and adds a verifier signature if valid.

    Parameters:
    - entry (dict): ESG data record

    Returns:
    - dict: Entry with added 'verifier_signature' if valid, or empty dict if invalid.
    """
    is_valid, message = validate_esg_entry(entry)

    if is_valid:
        entry["verifier_signature"] = generate_signature(entry)
        entry["validation_status"] = "accepted"
        entry["validation_message"] = message
        return entry
    else:
        return {
            "validation_status": "rejected",
            "validation_message": message,
            "original_entry": entry}
