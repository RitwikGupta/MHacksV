import urllib2
import xmltodict
from string import split

statesGlobalVar = ['China']
def query(q, key="PA5U8P-6XX65RA456"):
    return urllib2.urlopen('http://api.wolframalpha.com/v2/query?appid=%s&input=%s&format=plaintext' % (key,urllib2.quote(q))).read()

def state_query(group_name, states=statesGlobalVar):
    results = {s: xmltodict.parse(query('%s of %s?' % (group_name, s))) for s in states}
    results = {s: [p for p in v['queryresult']['pod'] if p['@title'] == 'Result'][0]['subpod']['plaintext'] for s,v in results.items()}
    results = {s: float(split(v)[0])*(1000000 if 'million' in v else 1) for s,v in results.items()}
    return results

print state_query('population')
