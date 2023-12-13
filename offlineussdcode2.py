from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    # Retrieve data from the incoming USSD request
    user_input = request.form.get('text')
    
    # Process the USSD request and generate a response
    response_text = process_ussd(user_input)
    
    # Return the response to the USSD gateway
    return f"CON {response_text}"

def process_ussd(user_input):
    if not user_input:
        # Initial request for USSD code
        return "Please enter the USSD code in the format *123*amount*account*PIN#"

    # Split the user input into components
    ussd_components = user_input.split('*')

    # Check if the USSD initiator is correct
    if len(ussd_components) == 6 and ussd_components[:4] == ['', '123', 'amount', 'account']:
        # Extract amount, account, and PIN
        amount = ussd_components[4]
        account = ussd_components[5]
        pin = ussd_components[3]

        # Validate PIN (Note: In a real application, this should be securely handled)
        if validate_pin(pin):
            # Your logic to process the transfer with the provided amount and account
            return f"Transaction initiated: Transfer {amount} to account {account}. Thank you!"

        else:
            return "Invalid PIN. Please try again."

    else:
        return "Invalid USSD code. Please use *123*amount*account*PIN# format."

def validate_pin(pin):
    # Simple PIN validation. In a real application, use a secure method.
    return pin.isdigit() and len(pin) == 4

if name == '__main__':
    app.run(debug=True)