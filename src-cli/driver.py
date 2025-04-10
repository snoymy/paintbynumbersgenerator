import subprocess
import time
import os


def run_js_and_wait(js_file, args, output_folder, expected_image_name, timeout=30):
    # Build the command
    command = ["node", js_file] + args
    print(f"Running: {' '.join(command)}")

    # Run the JS file
    process = subprocess.run(command, capture_output=False, text=True)

    if process.returncode != 0:
        print("JavaScript error output:", process.stderr)
        return False

    print("JavaScript executed successfully.")

    # Wait for image to appear
    image_path = os.path.join(output_folder, expected_image_name)
    elapsed = 0
    interval = 1  # seconds

    while elapsed < timeout:
        if os.path.exists(image_path):
            print(f"Image found: {image_path}")
            return True
        time.sleep(interval)
        elapsed += interval

    print(f"Timeout: Image not found in {timeout} seconds.")
    return False


input_filename = "j_surreal_upscaled"
output_filename = "j_surreal_upscaled"

run_js_and_wait(
    js_file="main.js",
    args=["-i", f"input/{input_filename}.jpeg", "-o", f"results/{output_filename}.svg"],
    output_folder="results",
    expected_image_name=f"{output_filename}-full.png",
    timeout=120,  # wait up to 120 seconds
)
