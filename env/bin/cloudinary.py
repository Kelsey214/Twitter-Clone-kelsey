#!/Users/musubimanagement/Desktop/django_forum/env/bin/python3
# -*- coding: utf-8 -*-
import re
import sys

from cloudinary_cli.cli import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())