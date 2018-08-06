# !/usr/bin/env python3

import dataProcessor
import economy
import cgi
import stamps
import html

ec = economy
dp = dataProcessor
cl = dp.get_children_list()
el = dp.get_event_list()

form = cgi.FieldStorage()
child = form.getfirst("child", "не задано")
points = form.getfirst("zlatas", "0")
child = html.escape(child)
points = int(html.escape(points))
childCheckBoxList = []
stamps.print_head(stamps.pagesList[3]['title'])
stamps.print_page_header()

print("""
<div class="content">
        <form action="/cgi-bin/singlePayment.py">
            <input type="text" name="child" list="dl_children" autofocus autocomplete="off">
            <input type="number" name="zlatas" list="dl_events" autocomplete="off">
            <input type="submit">""")

print('<datalist id="dl_children">')
for chil in cl:
    print('<option value="', chil['name'], '">', chil['balance'], '</option>', sep="")
print("""</datalist>

<datalist id="dl_events">""")
for event in el:
    print('<option value="', event['price'], '">', event['description'], '</option>', sep="")
print("""</datalist>
    </form>
    </div>
</body>
</html>""")

if points != 0:
    ec.give_points_by_name(child, points)
