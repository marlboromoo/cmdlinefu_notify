#!/usr/bin/env python
# encoding: utf-8

import requests
import notify2
import json

URL = 'http://www.commandlinefu.com/commands/browse/json'

def get_cmds():
    """Get commands from commandlinefu.com
    :returns: commands in list.
    """
    r = requests.get(URL)
    return json.loads(r.text) if r.status_code == 200 else None

def main():
    """Get newest command from commandlinefu.com and send a notification.
    :returns: None
    """
    cmds = get_cmds()
    if cmds:
        cmd = cmds.pop(0)
        notify2.init('cmdline-fu')
        n = notify2.Notification(
            summary = cmd['summary'],
            message = cmd['command'],
            icon = 'notification-message-email'
        )
        n.show()

if __name__ == '__main__':
    main()
