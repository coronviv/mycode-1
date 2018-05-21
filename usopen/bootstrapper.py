from netmiko import ConnectHandler
def bootstrapper(dev_type, dev_ip, dev_un, dev_pw, config):
    try:
        config_file = open(config, 'r') # open the file object described by config argument
        config_lines = config_file.read().splitlines() # create a list of the file lines
        config_file.close() # close the file object
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        open_connection.enable()
        output = open_connection.send_config_set(config_lines) # pass the config to the send_config_set() method
        print("4")
        print(output) # print the config to the screen # output to the screen

        open_connection.send_command_expect('write memory') # write the memory
        print("5")
        open_connection.disconnect() # close the open connection

        return True # Everything worked! - "Return TRUE when complete"
    except:
        return False # Something failed during the configuration process - "Return FALSE if fails"
