import threading


def delayed_message():
    """This function will be called after the delay."""
    print('Waiting 3 seconds...')

print('Starting tests...')

# Create a Timer object that will run the 'delayed_message' function
# after 3.0 seconds.
timer = threading.Timer(3.0, delayed_message)

# Start the timer. This runs in a separate thread.
timer.start()

# This line executes immediately, without waiting for the timer.
print('Tests')

# Note: The script will print:
# Starting tests...
# Tests
# (and then 3 seconds later)
# Waiting 3 seconds...