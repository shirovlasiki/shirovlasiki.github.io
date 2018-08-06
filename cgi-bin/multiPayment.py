# !/usr/bin/env python3

import dataProcessor
import stamps
import economy
import cgi
import html

ec = economy
dp = dataProcessor
cl = dp.get_children_list()
el = dp.get_event_list()

form = cgi.FieldStorage()
zlatas = form.getfirst("zlatas", "0")
zlatas = int(html.escape(zlatas))

childCheckBoxList = []


stamps.print_head(stamps.pagesList[3]['title'])
stamps.print_page_header()

print('<datalist id="dl_children">')

for chil in cl:
    print('<option value="', chil['name'], '">', chil['balance'], '</option>', sep="")
print("""</datalist>
<datalist id="dl_events">""")

for event in el:
    print('<option value="', event['price'], '">', event['description'], '</option>', sep="")
print("""</datalist>
    </form>""")

print("""
    <form name="multiple_choice" action=/cgi-bin/multiPayment.py>
        <input type="number" name="zlatas" list="dl_events" autocomplete="off">
        <input type="submit">
        <table border="0">
            <tr><td><input type="checkbox" name="select_all", id="cball" onclick="selectAll()"></td><td><b>Выбрать всех</b></td></tr>
""")
for chil in cl:
    print('<tr><td><input type="checkbox" name="checkbox', chil['ID'], '" id="cb', chil['ID'], '"></td><td>',
          chil['name'], '</td></tr>', sep="")
    childCheckBoxList.append(form.getfirst("checkbox" + str(chil['ID'])))

print("""
<script>
function selectAll(){
""")
for chil in cl:
    print('document.getElementById("cb', chil['ID'], '").checked=document.getElementById("cball").checked;', sep="")

print("""
}
</script>
</table>
</body>
</html>""")


print('<!--', childCheckBoxList, '-->')
print('<!--', form, '-->')
print('<!--', form.keys(), '-->')

currentgroup = []
i = 0
for childCB in childCheckBoxList:
    if childCB == 'on':
        currentgroup.append(cl[i]['ID'])
    i += 1


if zlatas != 0:
    if len(currentgroup) > 0:
        ec.give_points_to_group(currentgroup, zlatas)

