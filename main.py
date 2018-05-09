#!/usr/bin/env python


'''
    A program that scan a particular website and extract useful information
    includes: url, ip address, domain name, robot.txt, whois details
    Tpye the full url of the website you want in website.py, then the program 
    will generate the webInfo in the webInfo folder

    Usage: $python main.py
'''
from domain import get_domain_name
from general import create_directory, write_to_file
from ip_address import get_ip_address
from ip import get_nmap
from robots_txt import get_robots_txt
from whois import get_whois
from website import websites


# Create a Root Directory to store all the results
DIR = 'webInfo'
create_directory(DIR)


def gather_info(name, url):
    print("Scanning " + url + '\n')

    print("Getting Domain Name...")
    domain_name = get_domain_name(url)
    print("Finished\n")

    print("Getting the IP Address...")
    ip_address = get_ip_address(domain_name)
    nmap = get_nmap('-F', ip_address)
    print("Finished\n")

    print("Fetching robots.txt...")
    robots_txt = get_robots_txt(url)
    print("Finished\n")

    print("Extracting whois details...")
    whois = get_whois(domain_name)
    print("Finished\n")

    # Create report in a file
    create_report(name, url, domain_name, nmap, robots_txt, whois)
    print("Information for " + name + " saved in WebInfo/" + name + " Folder\n")


def create_report(name, url, domain_name, nmap, robots_txt, whois):
    project_dir = DIR + '/' + name
    create_directory(project_dir)
    write_to_file(project_dir + '/url.txt', url)
    write_to_file(project_dir + '/domain-name.txt', domain_name)
    write_to_file(project_dir + '/ip.txt', nmap)
    write_to_file(project_dir + '/robots-txt.txt', robots_txt)
    write_to_file(project_dir + '/whois.txt', whois)

for web in websites:
    gather_info(web[0], web[1])
