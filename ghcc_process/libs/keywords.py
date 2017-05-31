#!/usr/bin/env python

''' If a keyword in this list is present in a commits patch, that commit
    will be flagged. Add additional key words or organizational specific
    words to this list. These are not case sensitive. Use keywords specific
    to your company (ie, domain names, internal systems, etc) that are not
    common words.
'''

KEYWORDS = ['BEGIN RSA PRIVATE KEY',
            'BEGIN PGP PRIVATE']
