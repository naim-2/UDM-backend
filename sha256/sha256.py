import hashlib

def calculate_sha256(data):
    # Convert data to bytes if it’s not already
    if isinstance(data, str):
        data = data.encode()
        
    # Calculate SHA-256 hash
    sha256_hash = hashlib.sha256(data).hexdigest()
        
    return sha256_hash