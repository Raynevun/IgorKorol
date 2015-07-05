from urllib.request import urlopen
from xml.dom.minidom import parseString
from lib import StringUtils

url = 'https://beacon.nist.gov/rest/record/last'
ERROR_BEACON_API_MSG = "Error: Unable calculate char sequence because Beacon API issue\n  " \
                       "Status code : Actual {0}, Expected {1}\n"\
                       "Beacon response :\n {2}"

response = urlopen(url)
resp_body = response.read()

code_actual = response.getcode()
code_expected = 200

if code_actual == code_expected:
    value = parseString(resp_body).getElementsByTagName('outputValue')[0].firstChild.data
    print("Beacon 'last' value :\n{0}".format(value))

    # calculate char sequense from Beacon HEX value represented as string
    results = StringUtils.calculate_char_sequence(value)

    # print result as 'character, sequense'
    StringUtils.print_collection(results)
else:
    print(ERROR_BEACON_API_MSG.format(code_actual, code_expected, resp_body))


