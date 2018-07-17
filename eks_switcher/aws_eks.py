import click

def get_server_url(client, name):
    cluster = client.describe_cluster(
        name=name,
    ).get('cluster')
    return cluster.get('endpoint')


def get_certificate_data(client, name):
    cluster = client.describe_cluster(
        name=name,
    ).get('cluster')
    return cluster.get('certificateAuthority').get('data')


def list_clusters(client):
    clusters = client.list_clusters().get('clusters')
    print_formatted_cluster_list(clusters)
    choice = input('Enter the your choice: ')
    return clusters[int(choice) - 1]


def print_formatted_cluster_list(clusters):
    click.echo('Select the cluster you wish to connect to')
    i = 0
    for cluster in clusters:
        i += 1
        click.echo(f'{i}) {cluster}')
