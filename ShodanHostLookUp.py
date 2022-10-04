#!/usr/bin/env python3
import shodan
import sys

# Configuration
API_KEY = 'eqXVbpcctHp51oNhyh7cbP6VT8UL4av2'
api = shodan.Shodan(API_KEY)

# lookup the host
Host = api.host(input('Enter the ip or domain: '))

#print the general info
print("""
      Domains: {}
      IP: {}
      Organization: {}
      Operating System: {}
      Autonomous Systems: {}
      Countries: {}
      """.format(Host['ip_str'], Host.get('domain', 'n/a'),Host.get('org', 'n/a'),Host.get('os', 'n/a'),Host.get('ans','n/a'),Host.get('country','n/a')))

# print all banners
for vbanner in Host['data']:
    print("""
          port: {}
          Banners: {}
          """.format(vbanner['port'], vbanner['data']))