# lextab.py. This file automatically created by PLY (version 3.10). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('PRINTLN', 'INCON', 'INTVR', 'GRTEQ', 'EQLTO', 'ANDOP', 'STRING', 'SUBOP', 'REMOP', 'FOR', 'EQUAL', 'ITER', 'OROPE', 'STRNG', 'LOOPC', 'STATIC', 'ADDOP', 'SLCOM', 'IF', 'TRUE', 'UNEQL', 'CONST', 'WHILE', 'BLCOM', 'FORCN', 'LSSEQ', 'STDIN', 'LBCKT', 'LESST', 'CLOSP', 'THEN', 'DEROP', 'OPENP', 'IN', 'SEMCL', 'RBCKT', 'IDVAR', 'FALSE', 'LET', 'LOOP', 'GREAT', 'DOTOP', 'CONCAT', 'ELSE', 'NEW', 'QUOOP'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_IDVAR>[a-zA-Z_!.][a-zA-Z0-9_!.]*)|(?P<t_newline>\\n+)|(?P<t_SLCOM>//.*)|(?P<t_BLCOM>///(.|\\n)?///)|(?P<t_STRNG>"[ a-zA-Z_][ a-zA-Z0-9_][ a-zA-Z0-9_~?!@#$%^&-]*")|(?P<t_INTVR>[-+]?[0-9]+)|(?P<t_OROPE>\\|\\|)|(?P<t_EQLTO>\\=\\=)|(?P<t_UNEQL>\\=\\!)|(?P<t_LSSEQ>\\<\\=)|(?P<t_GRTEQ>\\>\\=)|(?P<t_DOTOP>\\.)|(?P<t_ADDOP>\\+)|(?P<t_DEROP>\\*)|(?P<t_OPENP>\\()|(?P<t_CLOSP>\\))|(?P<t_SUBOP>-)|(?P<t_QUOOP>/)|(?P<t_REMOP>%)|(?P<t_ANDOP>&)|(?P<t_EQUAL>=)|(?P<t_LESST><)|(?P<t_GREAT>>)|(?P<t_LBCKT>{)|(?P<t_RBCKT>})|(?P<t_SEMCL>;)', [None, ('t_IDVAR', 'IDVAR'), ('t_newline', 'newline'), ('t_SLCOM', 'SLCOM'), ('t_BLCOM', 'BLCOM'), None, (None, 'STRNG'), (None, 'INTVR'), (None, 'OROPE'), (None, 'EQLTO'), (None, 'UNEQL'), (None, 'LSSEQ'), (None, 'GRTEQ'), (None, 'DOTOP'), (None, 'ADDOP'), (None, 'DEROP'), (None, 'OPENP'), (None, 'CLOSP'), (None, 'SUBOP'), (None, 'QUOOP'), (None, 'REMOP'), (None, 'ANDOP'), (None, 'EQUAL'), (None, 'LESST'), (None, 'GREAT'), (None, 'LBCKT'), (None, 'RBCKT'), (None, 'SEMCL')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {'INITIAL': 't_eof'}
