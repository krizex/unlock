#!/usr/bin/env python
import requests
import pprint

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def main():
    s = requests.Session()
    r = s.get('https://citrix.service-now.com/unlock.do')
    payload = {
        'sysparm_processor': 'global.OrchestartionUtil',
        'sysparm_scope': 'global',
        'sysparm_want_session_messages': 'true',
        'sysparm_name': 'callUnlock',
        'userID': 'yangqi',
        'ni.nolog.x_referer': 'ignore',
        'x_referer': 'unlock.do'
    }
    # req = s.Request('POST', 'https://citrix.service-now.com/xmlhttp.do', data=payload)
    # prepared = req.prepare()
    # pretty_print_POST(prepared)
    # r = s.send(prepared)
    s.headers.update({'X-UserToken': '284b16d8db6f07400c9d69c3ca9619106c229d6aabe9de30f05f5497afb8c9c689bdc257'})
    r = s.post('https://citrix.service-now.com/xmlhttp.do', data=payload)
    print 'headers:'
    pprint.pprint(r.request.headers)
    print r.text

if __name__ == '__main__':
    main()
