from os.path import expanduser


def get_config_contents():
    home = expanduser('~')
    config_path = home + '/.aws/config'
    with open(config_path, 'r') as config_file:
        return config_file.read().split('\n')


def get_role_arn(profile='default'):
    contents = get_config_contents()
    if profile == 'default':
        for line in contents:
            if line.strip() == '':
                return None
            if 'role_arn' in line:
                return line.split(' ')[2]
        return None
    else:
        correct_block = False
        for line in contents:
            if line == f'[profile {profile}]':
                correct_block = True
                continue
            if correct_block:
                if line.strip() == '':
                    return
                if 'role_arn' in line:
                    return line.split(' ')[2]
        return None
