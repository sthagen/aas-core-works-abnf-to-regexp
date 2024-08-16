alphanum = '[a-zA-Z0-9]'
mark = "[\\-\\-.!~*'()]"
unreserved = f'({alphanum}|{mark})'
hex = (
    '([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[e'
    'E]|[fF])'
)
escaped = f'%{hex}{hex}'
pchar = f'({unreserved}|{escaped}|[:@&=+$,])'
param = f'({pchar})*'
segment = f'({pchar})*(;{param})*'
path_segments = f'{segment}(/{segment})*'
abs_path = f'/{path_segments}'
scheme = '[a-zA-Z][a-zA-Z0-9+\\-.]*'
userinfo = f'({unreserved}|{escaped}|[;:&=+$,])*'
domainlabel = f'({alphanum}|{alphanum}({alphanum}|-)*{alphanum})'
toplabel = f'([a-zA-Z]|[a-zA-Z]({alphanum}|-)*{alphanum})'
hostname = f'({domainlabel}\\.)*{toplabel}(\\.)?'
ipv4address = '[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+'
host = f'({hostname}|{ipv4address})'
port = '[0-9]*'
hostport = f'{host}(:{port})?'
server = f'(({userinfo}@)?{hostport})?'
reg_name = f'({unreserved}|{escaped}|[$,;:@&=+])+'
authority = f'({server}|{reg_name})'
net_path = f'//{authority}({abs_path})?'
reserved = '[;/?:@&=+$,]'
uric = f'({reserved}|{unreserved}|{escaped})'
query = f'({uric})*'
hier_part = f'({net_path}|{abs_path})(\\?{query})?'
uric_no_slash = f'({unreserved}|{escaped}|[;?:@&=+$,])'
opaque_part = f'{uric_no_slash}({uric})*'
absoluteuri = f'{scheme}:({hier_part}|{opaque_part})'
fragment = f'({uric})*'
lowalpha = (
    '([aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[gG]|[hH]|[iI]|[jJ]|[k'
    'K]|[lL]|[mM]|[nN]|[oO]|[pP]|[qQ]|[rR]|[sS]|[tT]|[uU]|[v'
    'V]|[wW]|[xX]|[yY]|[zZ])'
)
path = f'({abs_path}|{opaque_part})?'
rel_segment = f'({unreserved}|{escaped}|[;@&=+$,])+'
rel_path = f'{rel_segment}({abs_path})?'
relativeuri = f'({net_path}|{abs_path}|{rel_path})(\\?{query})?'
upalpha = (
    '([aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[gG]|[hH]|[iI]|[jJ]|[kK]|'
    '[lL]|[mM]|[nN]|[oO]|[pP]|[qQ]|[rR]|[sS]|[tT]|[uU]|[vV]|'
    '[wW]|[xX]|[yY]|[zZ])'
)
uri_reference = f'({absoluteuri}|{relativeuri})?(\\#{fragment})?'