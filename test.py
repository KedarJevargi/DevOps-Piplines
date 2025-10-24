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

# --- THIS IS THE FIX ---
# Wait for the timer's thread to complete before the main script exits.
# Without this, the script and the GitHub Action would exit immediately.
timer.join()

print('Test script finished.')

# The script will now correctly print:
# Starting tests...
# Tests
# (waits 3 seconds)
# Waiting 3 seconds...
# Test script finished.