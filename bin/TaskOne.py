from urllib.request import urlopen
from xml.dom.minidom import parseString
import collections

url = 'https://beacon.nist.gov/rest/record/last'
ERROR_BEACON_API_MSG = "Error: Unable calculate char sequence because Beacon API issue\n  " \
                       "Status code : Actual {0}, Expected {1}\n"\
                       "Beacon response :\n {2}"

response = urlopen(url)
resp_body = response.read()

code_actual = response.getcode()
code_expected = 201
if code_actual == code_expected:
    value = parseString(resp_body).getElementsByTagName('outputValue')[0].firstChild.data
    print(value)

    results = collections.defaultdict(int)
    for c in value:
        results[c] += 1

    for k in results.keys():
        print(k, ',', results[k])
else:
    print(ERROR_BEACON_API_MSG.format(code_actual, code_expected, resp_body))