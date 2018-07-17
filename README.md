# EKS-Switcher
Python util for swapping generating configuration files and swapping between EKS Clusters on AWS
By running the utility it will overwrite your ~/.kube/config file with what's required for connecting via `kubectl`

## Installation
`pipenv install eks_switcher`

## Usage
`eks-switcher --name {CluterName} --profile {AwsProfile}`

### Local Development
The repo is built using `flit` and it is using `pipenv` for dependency management.
