

tst_id = '''\n<line_test xmlns = "http://oval.mitre.org/XMLSchema/oval-definitions-5#nxos" id = "{data[test_id]}" check_existence = "at_least_one_exists" comment = "Check for {data[Comment]}" version = "1" check = "all" >
    <object object_ref ="oval:org.tanium.cisco.nxos.cve:obj:8000"/>
    <state state_ref ="{data[state_id]}"/>
</line_test>'''

state_id = '''\n<line_state xmlns = "http://oval.mitre.org/XMLSchema/oval-definitions-5#nxos" id = "{data[state_id]}" version = "1" comment = "{data[Comment]}Affected Pattern" >
    <config_line operation ="pattern match" >{data[state_regex]}</config_line >
</line_state>'''

