import requests

def check_site_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"SUCCESS: {url} is up!"
        else:
            return f"WARNING: {url} returned {response.status_code}"
    except Exception as e:
        return f"FAILED: {url} is unreachable. Error: {e}"

# Calling it manually for now
print(check_site_status("https://google.com"))