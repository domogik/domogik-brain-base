# -*- coding: utf-8 -*-
import subprocess

def test_internet(cfg_i18n):
    """ Test ping on interner
        1. test a ping on an ip to check if network is ok
        2. test a ping on an url to check if DNS is working
    """
    response_ip = ping("4.4.4.4")  # Google DNS server

    # ip ping ko
    if response_ip != 0:
        return cfg_i18n['NO_IP_ACCESS']
    # ip ping ok
    else:
        response_dns = ping("www.google.com")
        if response_dns != 0:
            return cfg_i18n['NO_DNS_ACCESS']
        else:
            return cfg_i18n['OK']

def ping(remote):
    ping_action = subprocess.Popen(["/bin/ping", "-c1", "-w2", remote], stdout=subprocess.PIPE)
    ping_action.communicate()
    return ping_action.returncode

