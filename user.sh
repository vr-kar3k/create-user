#!/bin/bash

# Step 1: Clone the GitHub repository
echo "Cloning the GitHub repository..."
git clone https://github.com/vr-kar3k/create-user.git

# Navigate into the cloned directory
cd create-user

# Step 2: Run the Python script to create the user
echo "Running the create_user.py script..."
sudo python3 create_user.py

# Step 3: Check if the user creation was successful
if [ $? -eq 0 ]; then
    echo "User creation successful!"

    # Step 4: Cleanup the downloaded files
    echo "Cleaning up downloaded files..."
    cd ..
    sudo rm -rf create-user

    echo "Cleanup successful!"
else
    echo "User creation failed. No cleanup performed."
fi