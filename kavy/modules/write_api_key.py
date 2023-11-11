import configparser

def write_api_key(api_key):
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Add a section [OpenAI] and set the API_KEY
    config['OpenAI'] = {'API_KEY': api_key}

    # Write the configuration to a file
    with open('config.ini', 'w') as configfile:
        config.write(configfile)