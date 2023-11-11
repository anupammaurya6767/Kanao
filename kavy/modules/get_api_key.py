import configparser


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config.get('OpenAI', 'API_KEY', fallback=None)

    if not api_key:
        raise ValueError('OpenAI API key is not provided in the configuration file.')

    return api_key