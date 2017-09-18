from __future__ import print_function

import sys
import yaml
import jinja2

if len(sys.argv) != 2:
    print("ksy2spicy.py <myfile.ksy>")
    sys.exit(1)

ksy_string = open(sys.argv[1]).read()
ksy = yaml.load(ksy_string)

template_string = open("spicy_template.jinja2").read()
template = jinja2.Template(template_string, trim_blocks=True, lstrip_blocks=True)

print(template.render(data=ksy))

