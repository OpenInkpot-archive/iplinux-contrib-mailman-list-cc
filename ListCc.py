"""
Send a mail to more recipients if X-List-Cc header is specified.
"""

def process(mlist, msg, msgdata):
    if msg.has_key('x-list-cc'):
        if not msgdata.has_key('recips'):
            msgdata['recips'] = []
        for recipient in ','.split(msg['x-list-cc']):
            recipient = recipient.strip()
            if recipient not in msgdata['recips']:
                msgdata['recips'].append(recipient)
