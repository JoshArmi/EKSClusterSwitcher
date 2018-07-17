from os.path import expanduser

from jinja2 import Environment, PackageLoader, select_autoescape

from aws_eks import get_server_url, get_certificate_data
from aws_config import get_role_arn


def generate_kube_config(client, name, profile):
    server_url = get_server_url(client, name)
    certificate_data = get_certificate_data(client, name)
    role_arn = get_role_arn(profile)
    env = Environment(
        loader=PackageLoader('eks-switcher', 'files'),
        autoescape=select_autoescape(['jinja2'])
    )
    template = env.get_template('config.jinja2')
    home = expanduser('~')
    config_path = home + '/.kube/config'
    with open(config_path, 'w') as kube_config:
        kube_config.write(template.render(
            server_url=server_url,
            certificate_data=certificate_data,
            cluster_name=name,
            role_arn=role_arn,
            aws_profile=profile,
        ))
