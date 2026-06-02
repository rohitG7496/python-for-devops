import os

# Mandatory: Script crashes if DB_PASS is missing
db_password = os.environ['DB_PASS']

# Optional: Uses 'us-east-1' if REGION is not set
aws_region = os.environ.get('REGION')

print(f"Connecting to AWS {aws_region} region")

#print(os.getenv("DB_PASS"))

print(os.environ.get("DB_PASS"))
#print(os.environ.get("REGION"))