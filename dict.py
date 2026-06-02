# Storing configuration for a single server node
node_config = {
    "hostname": "prod-web-01",
    "ip_address": "10.0.0.5",
    "environment": "production",
    "cpu_cores": 4
}

# Accessing a value using its key
print(node_config["ip_address"])  # Output: 10.0.0.5

# Adding/Updating a key-value pair
node_config["status"] = "Healthy"
print(node_config)