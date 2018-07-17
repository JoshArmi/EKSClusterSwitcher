""" A CLI utilitiy for for swapping your Kubernetes config amongst different 
    EKS Clusters """

__version__ = '0.4'

import boto3
import click

from .aws_eks import list_clusters
from .kube_config import generate_kube_config


@click.command()
@click.option('--profile', '-p', help='Name of AWS profile')
@click.option('--name', '-n', help='Name of EKS Cluster')
def main(profile, name):
    if profile is None:
        profile = 'default'
    session = boto3.Session(profile_name=profile)
    client = session.client('eks')
    if name is None:
        name = list_clusters(client)
    generate_kube_config(client, name, profile)
