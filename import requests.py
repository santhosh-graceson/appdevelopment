import requests
import json
import matplotlib.pyplot as plt

# Define the API endpoint and data to send as JSON
url = "https://santhosh-api.free.beeceptor.com"
data = {"temperature": 40, "device_id": 3, "faherinheit": 104}

# Send a POST request with the JSON data and retrieve the response
response = requests.post(url, json=data)
response_json = response.json()

# Extract the relevant data from the response and plot it in real-time
temperature = []
faherinheit = []

for item in response_json:
    temperature.append(item["x"])
    faherinheit.append(item["y"])
    plt.plot(temperature, faherinheit)
    plt.draw()
    plt.pause(0.001)

# Show the final plot
plt.show()