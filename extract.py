# -*- coding: utf-8 -*-
#!/usr/bin/python

import json
from bs4 import BeautifulSoup

str_json=r'{"title":"xxx","content":"<p class=\"MsoNormal\" "}'
j = json.loads(str_json)
soup=BeautifulSoup(j)
print (soup.get_text())




