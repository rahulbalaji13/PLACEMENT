def device_count():
    # Getting input from the user
    hours = int(input("Enter the number of available hours: "))
    devices = int(input("Enter the number of devices to be tested: "))
    
    # Check if the given hours is less than 4
    if hours < 4:
        print("Invalid Input")
        return
    
    # Calculate how many devices can be tested
    devices_tested = hours // 4
    
    # If the devices to be tested are more than available devices
    if devices_tested > devices:
        devices_tested = devices
    
    # Calculate the remaining devices
    remaining_devices = devices - devices_tested
    
    # Output the results
    print(devices_tested)
    print(remaining_devices)

# Call the function
device_count()
                                                                                                                            
