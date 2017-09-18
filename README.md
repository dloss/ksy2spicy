# ksy2spicy

An experimental [Kaitai Struct](http://kaitai.io) to
[Spicy](http://www.icir.org/hilti/) converter.

It only covers some basic types, but that might already be helpful
when trying to write a [Spicy parser](http://www.icir.org/hilti/spicy/intro.html)
for a data structure that Kaitai Struct already [supports](http://formats.kaitai.io).

Dependencies:

* Python
* yaml
* jinja2

Usage:

    python ksy2spicy <myfile.ksy>
