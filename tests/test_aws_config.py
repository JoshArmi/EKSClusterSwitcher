from unittest.mock import patch

import pytest

from eks_switcher import aws_config

custom_profile = 'eks'


@patch('eks_switcher.aws_config.get_config_contents')
def test_get_role_arn_for_default_profile_with_no_role(mock):
    with open('./tests/files/config_no_role', 'r') as config_file:
        mock.return_value = config_file.read().split('\n')
    assert aws_config.get_role_arn() is None


@patch('eks_switcher.aws_config.get_config_contents')
def test_get_role_arn_for_custom_profile_with_no_role(mock):
    with open('./tests/files/config_no_role', 'r') as config_file:
        mock.return_value = config_file.read().split('\n')
    assert aws_config.get_role_arn(profile=custom_profile) is None


@patch('eks_switcher.aws_config.get_config_contents')
def test_get_role_arn_for_default_profile(mock):
    with open('./tests/files/config', 'r') as config_file:
        mock.return_value = config_file.read().split('\n')
    assert aws_config.get_role_arn() == 'arn:aws:iam::000000000000:role/roleDefaultDevel'


@patch('eks_switcher.aws_config.get_config_contents')
def test_get_role_arn_for_custom_profile(mock):
    with open('./tests/files/config', 'r') as config_file:
        mock.return_value = config_file.read().split('\n')
    assert aws_config.get_role_arn(profile=custom_profile) == 'arn:aws:iam::333333333333:role/roleEksDevDevel'
