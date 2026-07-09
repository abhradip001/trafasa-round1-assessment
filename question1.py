import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Mock database
mock_db = {
    "V001": {"name": "Alpha Corp", "rating": 4.5},
    "V002": {"name": "Beta Ltd", "rating": 3.8},
    "V004": {"name": "Delta Inc", "rating": 4.9},
}

def fetch_vendor_data(vendor_ids):
    """
    Fetch vendor information from the mock database.

    Parameters:
        vendor_ids (list): List of vendor IDs.

    Returns:
        dict: Dictionary containing successfully retrieved vendor data.
    """
    retrieved_data = {}

    for vendor_id in vendor_ids:
        # Simulate a slow API call
        time.sleep(0.5)

        if vendor_id in mock_db:
            retrieved_data[vendor_id] = mock_db[vendor_id]
        else:
            logging.warning(f"Vendor ID '{vendor_id}' not found.")

    return retrieved_data


# Example Usage
if __name__ == "__main__":
    vendors_list = ["V001", "V003", "V002", "V004", "V005"]

    result = fetch_vendor_data(vendors_list)

    print("\nRetrieved Vendor Data:")
    for vendor_id, details in result.items():
        print(f"{vendor_id}: {details}")