import pytest
from validator import validate_esg_entry
# Test Case 1: Valid ESG Entry
def test_valid_entry():
    entry = {
        "company": "GreenRate",
        "reporting_period": "Q1-2025",
        "emissions_kg_co2e": 1000,
        "energy_use_mwh": 50.0,
        "data_source": "internal_meter",
        "submitted_by": "officer_01"}
    is_valid, msg = validate_esg_entry(entry)
    assert is_valid is True
    assert msg == "Valid entry"
# Test Case 2: Missing 'submitted_by'
def test_missing_submitter():
    entry = {
        "company": "GreenRate",
        "reporting_period": "Q1-2025",
        "emissions_kg_co2e": 1000,
        "energy_use_mwh": 50.0,
        "data_source": "internal_meter"}
    is_valid, msg = validate_esg_entry(entry)
    assert is_valid is False
    assert msg == "Missing submitter"
# Test Case 3: Invalid Emissions Format
def test_invalid_emissions_format():
    entry = {
        "company": "GreenRate",
        "reporting_period": "Q1-2025",
        "emissions_kg_co2e": "high",  # Should be a number
        "energy_use_mwh": 50.0,
        "data_source": "internal_meter",
        "submitted_by": "officer_01"}
    is_valid, msg = validate_esg_entry(entry)
    assert is_valid is False
    assert msg == "Invalid emissions format"
