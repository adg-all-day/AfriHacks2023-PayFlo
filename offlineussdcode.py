# Sample USSD Application in Python

# Dictionary to store user sessions
user_sessions = {}

def handle_ussd(session_id, user_input):
    """
    Handle USSD requests and provide appropriate responses.
    """
    if session_id not in user_sessions:
        user_sessions[session_id] = {'name': None, 'balance': 0.0}

    if user_input == '1':
        user_sessions[session_id]['name'] = input("Enter your name: ")
        return f"Welcome, {user_sessions[session_id]['name']}! Choose an option:\n1. Check Balance\n2. Exit"
    elif user_input == '2':
        return f"Goodbye, {user_sessions[session_id]['name']}!"

    elif user_input == '1' and user_sessions[session_id]['name']:
        return f"Your balance is ${user_sessions[session_id]['balance']}."

    else:
        return "Invalid input. Please try again."

# Simulate USSD session
def simulate_ussd_session():
    session_id = input("Enter session ID: ")
    user_input = ""

    while user_input.lower() != '2':
        user_input = input("Enter your choice (1 for balance, 2 to exit): ")
        response = handle_ussd(session_id, user_input)
        print(response)

# Run simulation
simulate_ussd_session()