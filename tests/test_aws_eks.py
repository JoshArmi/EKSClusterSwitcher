from unittest.mock import patch, MagicMock
import json

import pytest
import boto3
from botocore.stub import Stubber

from eks_switcher import aws_eks


cluster_name = 'test_cluster'


def test_get_server_url():
    client = boto3.client('eks')
    stubber = Stubber(client)
    with open('./tests/files/sample_cluster.json', 'r') as server_file:
        server_json = json.loads(server_file.read())
        stubber.add_response('describe_cluster', server_json)
        with stubber:
            assert aws_eks.get_server_url(client, cluster_name) == 'https://A0DCCD80A04F01705DD065655C30CC3D.yl4.us-west-2.eks.amazonaws.com'


def test_get_certificate_data():
    client = boto3.client('eks')
    stubber = Stubber(client)
    with open('./tests/files/sample_cluster.json', 'r') as server_file:
        server_json = json.loads(server_file.read())
        stubber.add_response('describe_cluster', server_json)
        with stubber:
            assert aws_eks.get_certificate_data(client, cluster_name) == 'HERE_BE_SOME_CERT_DATA='
