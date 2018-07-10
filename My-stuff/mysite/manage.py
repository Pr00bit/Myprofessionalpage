#!/usr/bin/env python
import os
import sys

sys.path.insert(1,'/home/dzikuss98/My-stuff/myvenv/lib/python3.5/site-packages')
path = '/home/dzikuss98/My-stuff/mysite'  # use your own username here
if path not in sys.path:
    sys.path.append(path)
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
