import http.client

# Establish an HTTP connection to the server
http_connection = http.client.HTTPConnection('www.example.com')

# Send an HTTP GET request
http_connection.request("GET", "/")

# Get the response from the server
server_response = http_connection.getresponse()

# Print the type of the response object
print(type(server_response))

# Print the status code and reason phrase from the response
print(server_response.status, server_response.reason)

# If the request was successful (status code 200), read and print the response data
if server_response.status == 200:
    response_data = server_response.read()
    print(response_data)
