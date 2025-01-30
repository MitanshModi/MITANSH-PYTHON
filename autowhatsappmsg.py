import pywhatkit as kit

# Send a WhatsApp message to a contact at a specific time
phone_number = "8866059279"  # Replace with the actual phone number
message = "Hello, this is an automated WhatsApp message!"
hour = 10  # 10 AM
minute = 45  # 45 minutes

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)

print(f"Message scheduled to be sent to {phone_number} at {hour}:{minute}")
