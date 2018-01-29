import re

preTable = r""
with open("preTable.txt", 'r') as f:
    preTable = f.read()

postTable = r""
with open("postTable.txt", 'r') as f:
    postTable = f.read()


def htmlTable(teamsFinalData):
    finalString = ""

    # Make table
    table = ""

    for team in teamsFinalData:
        table += """
            <tr>
                <td>%(team_number)s</td>
                <td>%(help_number)i</td>
                <td>%(nickname)s</td>
                <td>%(rookie_year)s</td>
                <td>%(country)s</td>
                <td>%(champs)i</td>
                <td>%(regionals)i</td>
                <td>%(highest_rank)i</td>
                <td>%(qualified_string)s</td>
                <td>%(max_opr)f</td>
                <td>%(average_opr)f</td>
            </tr>\n
        """ % (teamsFinalData[team])

    finalString = preTable + table + postTable
    finalString = re.sub(r'[^\x00-\x7F]+','', finalString)
    return finalString
