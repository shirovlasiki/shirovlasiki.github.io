import dataProcessor
import stamps

def sort_by_name(l):
    return l['name']


def sort_by_balance(l):
    return l['balance']


dp = dataProcessor
stamps.print_head('Рейтинг')
stamps.print_page_header()
print("""
            <table border="1">
                <caption>SHIROFORBES TOP-34</caption>
                <tr>
                    <th>№</th>
                    <th>Шировласик</th>
                    <th>Златы</th>
                </tr>""")
cl = dp.get_children_list()

cl.sort(key = sort_by_balance, reverse=1)
i = 1
for child in cl:
    print("<tr><td>", i, "</td><td>", child['name'], "</td><td>", child['balance'], '</td></tr>')
    i += 1
print("""
        </table>
    </body>
</html>""")
