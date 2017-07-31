import re

preTable = """
<head>
<link href="css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<table id="myTable" class="table tablesorter">
<thead>
<tr>
<th>Team Number</th>
<th>Help Number</th>
<th>Name</th>
<th>Rookie Year</th>
<th>Country</th>
<th># of Champs</th>
<th># of Regionals</th>
<th>Highest Normalized Rank</th>
<th>Qualified</th>
<th>Max OPR</th>
<th>Average OPR</th>
</tr>
</thead>
<tbody>
"""

postTable = """
</tbody>
<script src="js/jquery.min.js"></script>
<script type="text/javascript" src="js/jquery.tablesorter.min.js"></script>
<script src="js/bootstrap.min.js"></script>
<script>
    $(document).ready(function() 
    { 
        $("#myTable").tablesorter( {sortList: [[1,-1]]} ); 
    } 
);
</script>
</body>
"""


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
    finalString = re.sub('[^\u0000-\u007f]', '', finalString)
    return finalString
