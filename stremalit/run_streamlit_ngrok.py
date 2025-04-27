from pyngrok import ngrok
import subprocess
import time

token = "2w5qB9BanWszHTdJpiaXSNRohp0_5555q9EicW5yiCsx5WPeY"

# Step 1: Set ngrok auth token
try:
    ngrok.set_auth_token(token)
except Exception as e:
    print(f"Error setting ngrok token: {e}")
    exit(1)

# Step 2: Open ngrok tunnel on port 8501 (default Streamlit port)
try:
    public_url = ngrok.connect(8501)
    print(f" * ngrok tunnel started: {public_url}")
except Exception as e:
    print(f"Error starting ngrok tunnel: {e}")
    exit(1)

# Step 3: Run Streamlit app as a subprocess
# Replace 'app.py' with your Streamlit app filename if different
try:
    streamlit_process = subprocess.Popen(['streamlit', 'run', 'app.py'])
except Exception as e:
    print(f"Error running Streamlit app: {e}")
    ngrok.kill()  # Make sure to kill the ngrok tunnel if an error occurs
    exit(1)

try:
    # Keep the script running while the Streamlit app is running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...")
    streamlit_process.terminate()
    ngrok.kill()
