from uiautomator2 import connect, device

# Connect to the device
d = connect('your_device_serial_number')  # Replace with your device serial number

# Start the Amaze File Manager app (replace with your app package name)
amaze_package = 'com.amaze.filemanager'
d.app_start(amaze_package)

# Wait for the upload to complete and ensure the file exists
d.wait(5)  # Adjust the waiting time based on your needs

# Open the a.zip file
d(resourceId="your_a_zip_element_id").click()  # Replace with the element ID of the a.zip file

# Wait for a while to make sure the file is loaded
d.wait(5)  # Adjust the waiting time based on your needs

# Click on View
d(resourceId="view_button_id").click()  # Replace with the element ID of the View button

# Wait for a while to ensure the View operation is completed
d.wait(5)  # Adjust the waiting time based on your needs

# Click on b.zip
d(resourceId="b_zip_element_id").click()  # Replace with the element ID of the b.zip file

# Wait for a while to ensure the click operation is completed
d.wait(5)  # Adjust the waiting time based on your needs

# Click on extract multiple times to simulate multiple clicks
for _ in range(5):
    d(resourceId="extract_button_id").click()  # Replace with the element ID of the Extract button
    # Wait for a while to ensure the extract operation is completed
    d.wait(3)  # Adjust the waiting time based on your needs

# Simulated operations completed

# Close the Amaze File Manager app
d.app_stop(amaze_package)
