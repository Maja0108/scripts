import os

matches = []
# Walk the filesystem starting at the test_dir
for root, _, files in os.walk('/test_dir'):
    for name in files:
      	# Create the full path to the file by using os.path.join()
        fullpath = os.path.join(root, name)
        print(f"Processing file: {fullpath}")
        # Split off the extension and discard the rest of the path
        _, ext = os.path.splitext(fullpath)
        # Match the extension pattern .csv
        if ext == ".csv":
            matches.append(fullpath)
            
# Print the matches you find          
print(matches)