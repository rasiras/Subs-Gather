#!/usr/bin/env python3
import argparse
import os
import subprocess

# Set up the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('domain', help='the domain to enumerate subdomains for')
parser.add_argument('--save', action='store_true', help='save the list of subdomains to a file')
args = parser.parse_args()

# Use amass to get a list of subdomains from various sources
amass_output = subprocess.run(['amass', 'enum', '-d', args.domain], stdout=subprocess.PIPE)
amass_output = amass_output.stdout.decode()
amass_subdomains = amass_output.split('\n')

# Use subfinder to get a list of subdomains from various sources
subfinder_output = subprocess.run(['subfinder', '-silent', '-d', args.domain], stdout=subprocess.PIPE)
subfinder_output = subfinder_output.stdout.decode()
subfinder_subdomains = subfinder_output.split('\n')

# Use assetfinder to get a list of subdomains from various sources
assetfinder_output = subprocess.run(['assetfinder', '--subs-only', args.domain], stdout=subprocess.PIPE)
assetfinder_output = assetfinder_output.stdout.decode()
assetfinder_subdomains = assetfinder_output.split('\n')

# Use dig to get a list of subdomains from DNS records
dig_output = subprocess.run(['dig', args.domain, '+nostats', '+nocomments'], stdout=subprocess.PIPE)
dig_output = dig_output.stdout.decode()
dig_subdomains = []
for line in dig_output.split('\n'):
    if line.startswith(';; ANSWER SECTION:'):
        for subdomain in line.split('\n'):
            if subdomain and subdomain[0].isdigit():
                subdomain = subdomain.split()[4]
                if subdomain.endswith('.' + args.domain):
                    subdomain = subdomain[:-len(args.domain) - 1]
                    dig_subdomains.append(subdomain)

# Print the list of unique subdomains
unique_subdomains = set(amass_subdomains + subfinder_subdomains + assetfinder_subdomains + dig_subdomains)
for subdomain in sorted(unique_subdomains):
    print(subdomain)

# Save the list of subdomains to a file, if the --save flag was provided
if args.save:
    filename = args.domain + '_subdomains.txt'
    with open(filename, 'w') as f:
        for subdomain in sorted(unique_subdomains):
            f.write(subdomain + '\n')
