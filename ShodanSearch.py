#!/usr/bin/env python3
import shodan
import sys

# Configuration
API_KEY = 'eqXVbpcctHp51oNhyh7cbP6VT8UL4av2'

# The list of properties we want summary information on
FACETS = [
    'org',
    'domain',
    'port',
    'asn',
    ('os', 5),
    ('country', 5),
]

FACET_TITLES = {
    'org': 'Top 5 Organizations',
    'domain': 'Top 5 Domains',
    'port': 'Top 5 Ports',
    'asn': 'Top 5 Autonomous Systems',
    'os' : 'Top 5 Operating Systems',
    'country': 'Top 5 Countries',
}

# Input validation
if len(sys.argv) == 1:
    print('Usage: %s query' % sys.argv[0])
    sys.exit(1)

try:
    # Setup the api
    api = shodan.Shodan(API_KEY)

    # Generate a query string out of the command-line arguments
    query = ' '.join(sys.argv[1:])

    # And it also runs faster than doing a search().
    result = api.count(query, facets=FACETS)

    print('Shodan Summary Information')
    print('Query: %s' % query)
    print('Total Results: %s\n' % result['total'])

    # Print the summary info from the facets
    for facet in result['facets']:
        print(FACET_TITLES[facet])

        for term in result['facets'][facet]:
            print('%s: %s' % (term['value'], term['count']))

        # Print an empty line between summary info
        print('')

except Exception as e:
    print('Error: %s' % e)
    sys.exit(1)
