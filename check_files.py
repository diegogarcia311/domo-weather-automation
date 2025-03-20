import os

# Define the expected files and their paths
expected_files = [
    "fetch_weather.py",
    "send_to_domo.py"
]

def check_files():
    # Get the current working directory (should be the root of the repo)
    current_directory = os.getcwd()

    print(f"Checking files in: {current_directory}")
    print("\nExpected files in the root directory:")
    missing_files = []

    # Iterate over the expected files and check if they exist
    for file in expected_files:
        file_path = os.path.join(current_directory, file)
        if os.path.isfile(file_path):
            print(f"✅ {file} found!")
        else:
            missing_files.append(file)
            print(f"❌ {file} is missing!")

    if missing_files:
        print("\nMissing files:")
        for file in missing_files:
            print(f"❌ {file}")
    else:
        print("\nAll files are correctly placed in the root directory.")

# Call the check_files function
if __name__ == "__main__":
    check_files()
