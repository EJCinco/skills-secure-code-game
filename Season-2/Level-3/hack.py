import requests

# Set the URL for the application
url = "http://127.0.0.1:5000/"  # Adjust the port if needed

# Define the payload simulating the attack
payload = "<img src='x' onerror='alert(1)'>"

# Prepare the POST request with the payload
data = {"planet": payload}

# Send the POST request
response = requests.post(url, data=data)

# Print the response content
print("Response:")
print(response.text)

# Check if the application blocks the input correctly
if "Unknown planet" in response.text:
    print("Test Passed: The application handled the attack payload correctly.")
elif "alert" in response.text:
    print("Test Failed: XSS vulnerability is still present.")
else:
    print("Test Result: Unexpected behavior. Review the application response.")
