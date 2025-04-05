This repo contains all relevant files to run and maintain my homelab network.

Below is a 'roadmap' for finding stuff around the repo: 

| Directory | Description|
| --- | --- |
| .github/ | This is where all Github Workflow configurations are housed. |
| data/ | This is where data and scripts for specific services are stored, categorized by the service's name. |
| docker/ | This houses the Docker information necessary for composing all Docker services. |
| src/setup/ | This directory is for initializing pre-requisite components, such as my Python container with all dependencies included. |

# Install & Setup

1. Download the code from this repo. Don't clone it; the runners part won't work.
2. Build and connect your [self-hosted runner](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners)
   1. Your runner server must run Docker Server for the workflows to run correctly. See [update-dns.yaml](https://github.com/dakotah-hurda/bind9-shared/blob/df92745e477a0b269d818caa64a968f85ac752da/.github/workflows/update_dns.yaml#L29-L33) 
3. Build an ubuntu/bind9:latest Docker container. I don't know why this isn't in my Dockerfile and I don't feel like building it out. 
   1. Configure SSH key-based authentication. You'll need the SSH private key for the next step.
4. You'll need to configure the following VARS and SECRETS in your own Github repo: 

| Name | Type | Description| 
| --- | --- | --- |
| DOCKER_HOSTNAME | var | Hostname/IP of your Docker server |
| DOCKER_USERNAME | var | Management username of your Docker server admin |
| DOCKER_WORKSPACE | var | Directory where this repo will be cloned to on the Docker server, e.g. ' /home/dockeradmin/repos/bind9-shared'
| DOCKER_PASSWROD | secret | Admin password | 
| SSH_PRIVATE_KEY | secret | Used for SSH key-based authentication between Runner server and Docker server. 

5. You may need to update the [bind9 config templates](https://github.com/dakotah-hurda/bind9-shared/tree/main/data/bind9/templates) to match [your own DNS config.](https://bind9.readthedocs.io/en/latest/chapter3.html) I kept these pretty barebones. 

# Usage

1. Update the entries in [dns.yaml](https://github.com/dakotah-hurda/bind9-shared/blob/main/data/bind9/dns.yaml), then commit + push the changes to the main branch of your repo.
2. This should trigger the [workflow file ](https://github.com/dakotah-hurda/bind9-shared/blob/main/.github/workflows/update_dns.yaml) to generate the new bind9 configs and push them to your bind9 server.

# Troubleshooting and Support

Leave me alone