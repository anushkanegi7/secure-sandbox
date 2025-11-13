import os
import tempfile
import subprocess
import uuid

def run_in_sandbox(code):
    # Create a temporary .py file in the system temp directory
    filename = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4().hex}.py")
    
    with open(filename, 'w') as f:
        f.write(code)

    try:
        # Run the file in a subprocess (safe, isolated)
        result = subprocess.run(
            ['python', filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5,
            text=True
        )

        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "Error: Code execution timed out."
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        try:
            os.remove(filename)
        except:
            pass
