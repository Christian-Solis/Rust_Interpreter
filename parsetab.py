
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'fooLET STATIC CONST STDIN PRINTLN TRUE FALSE IF ELSE LOOP WHILE FOR IN FN DOTOP ADDOP SUBOP QUOOP DEROP REMOP EQUAL EQLTO UNEQL ANDOP OROPE LESST GREAT LSSEQ GRTEQ STRNG SLCOM BLCOM IDVAR INTVR OPENP CLOSP LBCKT RBCKT SEMCL COMMA COLON\n    foo : program\n    \n    program : declarationList\n    \n    declarationList : declaration\n                    | declaration declarationList\n    \n    declaration : varDeclaration\n                | constDeclaration\n                | staticDeclaration\n                | funcDeclaration\n    \n    varDeclaration : LET IDVAR EQUAL IDVAR SEMCL\n                   | LET IDVAR EQUAL INTVR SEMCL\n                   | LET IDVAR EQUAL STRNG SEMCL\n                   | LET IDVAR EQUAL expression SEMCL\n    \n    constDeclaration : CONST IDVAR EQUAL IDVAR SEMCL\n    \n    staticDeclaration : STATIC IDVAR EQUAL IDVAR SEMCL\n    \n    funcDeclaration : FN function\n    \n    function : FN parameters block\n    \n    parameters : OPENP CLOSP\n               | OPENP paramList CLOSP\n    \n    paramList : parameter\n              | parameter COMMA paramList\n    \n    parameter : IDVAR\n    \n    block : LBCKT RBCKT\n          | LBCKT statement-list RBCKT\n    \n    statement-list : stmt\n                   | stmt statement-list\n    \n    stmt : expression\n         | declaration\n         | selectionStmt\n         | iterationStmt\n         | inputStmt\n         | outputStmt\n    \n    expression : basicExp\n               | assignmentExp SEMCL\n               | comparisonExp\n               | boolExp\n    \n    basicExp : IDVAR\n             | INTVR\n             | STRNG\n    \n    identifier : IDVAR\n               | INTVR\n    \n    assignmentExp : identifier sumOp basicExp\n                  | identifier sumOp assignmentExp\n    \n    comparisonExp : basicExp relop basicExp\n                  | basicExp relop comparisonExp\n    \n    relop : LESST\n          | LSSEQ\n          | GREAT\n          | GRTEQ\n          | EQUAL\n          | UNEQL\n          | EQLTO\n    \n    sumOp : ADDOP\n          | SUBOP\n          | DEROP\n          | QUOOP\n          | EQUAL\n          | REMOP\n    \n    selectionStmt : IF expression EQUAL block\n                  | IF expression EQUAL block ELSE\n    \n    iterationStmt : FOR expression IN expression\n                  | WHILE expression EQUAL expression\n                  | WHILE expression LESST expression\n                  | WHILE expression GREAT expression\n    \n    inputStmt : STDIN OPENP stmt CLOSP\n    \n    outputStmt : PRINTLN OPENP stmt CLOSP\n    \n    boolExp : TRUE\n            | FALSE\n    '
    
_lr_action_items = {'LET':([0,4,5,6,7,8,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,95,96,105,106,107,108,109,110,111,112,],[9,9,-5,-6,-7,-8,-15,-32,-34,-35,-66,-67,-16,9,-9,-10,-11,-12,-33,-13,-14,-22,9,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,9,9,-58,-60,-61,-62,-63,-64,-65,-59,]),'CONST':([0,4,5,6,7,8,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,95,96,105,106,107,108,109,110,111,112,],[10,10,-5,-6,-7,-8,-15,-32,-34,-35,-66,-67,-16,10,-9,-10,-11,-12,-33,-13,-14,-22,10,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,10,10,-58,-60,-61,-62,-63,-64,-65,-59,]),'STATIC':([0,4,5,6,7,8,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,95,96,105,106,107,108,109,110,111,112,],[11,11,-5,-6,-7,-8,-15,-32,-34,-35,-66,-67,-16,11,-9,-10,-11,-12,-33,-13,-14,-22,11,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,11,11,-58,-60,-61,-62,-63,-64,-65,-59,]),'FN':([0,4,5,6,7,8,12,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,95,96,105,106,107,108,109,110,111,112,],[12,12,-5,-6,-7,-8,17,-15,-32,-34,-35,-66,-67,-16,12,-9,-10,-11,-12,-33,-13,-14,-22,12,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,12,12,-58,-60,-61,-62,-63,-64,-65,-59,]),'$end':([1,2,3,4,5,6,7,8,13,18,37,43,44,45,46,63,64,65,90,],[0,-1,-2,-3,-5,-6,-7,-8,-4,-15,-16,-9,-10,-11,-12,-13,-14,-22,-23,]),'IF':([5,6,7,8,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,95,96,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,-32,-34,-35,-66,-67,-16,74,-9,-10,-11,-12,-33,-13,-14,-22,74,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,74,74,-58,-60,-61,-62,-63,-64,-65,-59,]),'FOR':([5,6,7,8,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,95,96,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,-32,-34,-35,-66,-67,-16,75,-9,-10,-11,-12,-33,-13,-14,-22,75,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,75,75,-58,-60,-61,-62,-63,-64,-65,-59,]),'WHILE':([5,6,7,8,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,95,96,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,-32,-34,-35,-66,-67,-16,76,-9,-10,-11,-12,-33,-13,-14,-22,76,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,76,76,-58,-60,-61,-62,-63,-64,-65,-59,]),'STDIN':([5,6,7,8,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,95,96,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,-32,-34,-35,-66,-67,-16,77,-9,-10,-11,-12,-33,-13,-14,-22,77,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,77,77,-58,-60,-61,-62,-63,-64,-65,-59,]),'PRINTLN':([5,6,7,8,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,95,96,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,-32,-34,-35,-66,-67,-16,78,-9,-10,-11,-12,-33,-13,-14,-22,78,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,78,78,-58,-60,-61,-62,-63,-64,-65,-59,]),'IDVAR':([5,6,7,8,9,10,11,18,19,20,21,23,28,30,31,33,34,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,79,80,81,83,84,85,86,87,90,95,96,99,100,101,102,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,14,15,16,-15,24,35,36,42,-32,-34,-35,-66,-67,-16,79,-9,-10,-11,-12,86,-45,-46,-47,-48,-49,-50,-51,-33,79,-52,-53,-54,-55,-56,-57,-13,-14,-22,79,-26,-27,-28,-29,-30,-31,79,79,79,-36,-37,-38,42,-43,-44,-36,-37,-23,79,79,79,79,79,79,-58,-60,-61,-62,-63,-64,-65,-59,]),'INTVR':([5,6,7,8,18,19,28,30,31,33,34,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,79,80,81,84,85,86,87,90,95,96,99,100,101,102,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,25,-32,-34,-35,-66,-67,-16,80,-9,-10,-11,-12,87,-45,-46,-47,-48,-49,-50,-51,-33,80,-52,-53,-54,-55,-56,-57,-13,-14,-22,80,-26,-27,-28,-29,-30,-31,80,80,80,-36,-37,-38,-43,-44,-36,-37,-23,80,80,80,80,80,80,-58,-60,-61,-62,-63,-64,-65,-59,]),'STRNG':([5,6,7,8,18,19,28,30,31,33,34,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,73,74,75,76,79,80,81,84,85,86,87,90,95,96,99,100,101,102,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,26,-32,-34,-35,-66,-67,-16,81,-9,-10,-11,-12,81,-45,-46,-47,-48,-49,-50,-51,-33,81,-52,-53,-54,-55,-56,-57,-13,-14,-22,81,-26,-27,-28,-29,-30,-31,81,81,81,-36,-37,-38,-43,-44,-36,-37,-23,81,81,81,81,81,81,-58,-60,-61,-62,-63,-64,-65,-59,]),'TRUE':([5,6,7,8,18,19,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,74,75,76,79,80,81,84,85,86,87,90,95,96,99,100,101,102,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,33,-32,-34,-35,-66,-67,-16,33,-9,-10,-11,-12,-33,-13,-14,-22,33,-26,-27,-28,-29,-30,-31,33,33,33,-36,-37,-38,-43,-44,-36,-37,-23,33,33,33,33,33,33,-58,-60,-61,-62,-63,-64,-65,-59,]),'FALSE':([5,6,7,8,18,19,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,67,68,69,70,71,72,73,74,75,76,79,80,81,84,85,86,87,90,95,96,99,100,101,102,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,34,-32,-34,-35,-66,-67,-16,34,-9,-10,-11,-12,-33,-13,-14,-22,34,-26,-27,-28,-29,-30,-31,34,34,34,-36,-37,-38,-43,-44,-36,-37,-23,34,34,34,34,34,34,-58,-60,-61,-62,-63,-64,-65,-59,]),'RBCKT':([5,6,7,8,18,28,30,31,33,34,37,38,43,44,45,46,55,63,64,65,66,67,68,69,70,71,72,73,79,80,81,84,85,86,87,90,91,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,-32,-34,-35,-66,-67,-16,65,-9,-10,-11,-12,-33,-13,-14,-22,90,-24,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,-25,-58,-60,-61,-62,-63,-64,-65,-59,]),'CLOSP':([5,6,7,8,18,23,28,30,31,33,34,37,40,41,42,43,44,45,46,55,63,64,65,68,69,70,71,72,73,79,80,81,84,85,86,87,90,97,103,104,105,106,107,108,109,110,111,112,],[-5,-6,-7,-8,-15,39,-32,-34,-35,-66,-67,-16,82,-19,-21,-9,-10,-11,-12,-33,-13,-14,-22,-26,-27,-28,-29,-30,-31,-36,-37,-38,-43,-44,-36,-37,-23,-20,110,111,-58,-60,-61,-62,-63,-64,-65,-59,]),'EQUAL':([14,15,16,24,25,26,28,30,31,32,33,34,55,79,80,81,84,85,86,87,92,94,],[19,20,21,-36,-37,-38,52,-34,-35,61,-66,-67,-33,-36,-37,-38,52,-44,-36,-37,98,100,]),'OPENP':([17,77,78,],[23,95,96,]),'LBCKT':([22,39,82,98,],[38,-17,-18,38,]),'SEMCL':([24,25,26,27,28,29,30,31,33,34,35,36,55,79,80,81,84,85,86,87,88,89,],[43,44,45,46,-32,55,-34,-35,-66,-67,63,64,-33,-36,-37,-38,-43,-44,-36,-37,-41,-42,]),'LESST':([24,25,26,28,30,31,33,34,55,79,80,81,84,85,86,87,94,],[-36,-37,-38,48,-34,-35,-66,-67,-33,-36,-37,-38,48,-44,-36,-37,101,]),'LSSEQ':([24,25,26,28,79,80,81,84,86,87,],[-36,-37,-38,49,-36,-37,-38,49,-36,-37,]),'GREAT':([24,25,26,28,30,31,33,34,55,79,80,81,84,85,86,87,94,],[-36,-37,-38,50,-34,-35,-66,-67,-33,-36,-37,-38,50,-44,-36,-37,102,]),'GRTEQ':([24,25,26,28,79,80,81,84,86,87,],[-36,-37,-38,51,-36,-37,-38,51,-36,-37,]),'UNEQL':([24,25,26,28,79,80,81,84,86,87,],[-36,-37,-38,53,-36,-37,-38,53,-36,-37,]),'EQLTO':([24,25,26,28,79,80,81,84,86,87,],[-36,-37,-38,54,-36,-37,-38,54,-36,-37,]),'ADDOP':([24,25,32,79,80,],[-39,-40,57,-39,-40,]),'SUBOP':([24,25,32,79,80,],[-39,-40,58,-39,-40,]),'DEROP':([24,25,32,79,80,],[-39,-40,59,-39,-40,]),'QUOOP':([24,25,32,79,80,],[-39,-40,60,-39,-40,]),'REMOP':([24,25,32,79,80,],[-39,-40,62,-39,-40,]),'IN':([28,30,31,33,34,55,79,80,81,84,85,86,87,93,],[-32,-34,-35,-66,-67,-33,-36,-37,-38,-43,-44,-36,-37,99,]),'COMMA':([41,42,],[83,-21,]),'ELSE':([65,90,105,],[-22,-23,112,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'foo':([0,],[1,]),'program':([0,],[2,]),'declarationList':([0,4,],[3,13,]),'declaration':([0,4,38,67,95,96,],[4,4,69,69,69,69,]),'varDeclaration':([0,4,38,67,95,96,],[5,5,5,5,5,5,]),'constDeclaration':([0,4,38,67,95,96,],[6,6,6,6,6,6,]),'staticDeclaration':([0,4,38,67,95,96,],[7,7,7,7,7,7,]),'funcDeclaration':([0,4,38,67,95,96,],[8,8,8,8,8,8,]),'function':([12,],[18,]),'parameters':([17,],[22,]),'expression':([19,38,67,74,75,76,95,96,99,100,101,102,],[27,68,68,92,93,94,68,68,106,107,108,109,]),'basicExp':([19,38,47,56,67,74,75,76,95,96,99,100,101,102,],[28,28,84,88,28,28,28,28,28,28,28,28,28,28,]),'assignmentExp':([19,38,56,67,74,75,76,95,96,99,100,101,102,],[29,29,89,29,29,29,29,29,29,29,29,29,29,]),'comparisonExp':([19,38,47,67,74,75,76,95,96,99,100,101,102,],[30,30,85,30,30,30,30,30,30,30,30,30,30,]),'boolExp':([19,38,67,74,75,76,95,96,99,100,101,102,],[31,31,31,31,31,31,31,31,31,31,31,31,]),'identifier':([19,38,56,67,74,75,76,95,96,99,100,101,102,],[32,32,32,32,32,32,32,32,32,32,32,32,32,]),'block':([22,98,],[37,105,]),'paramList':([23,83,],[40,97,]),'parameter':([23,83,],[41,41,]),'relop':([28,84,],[47,47,]),'sumOp':([32,],[56,]),'statement-list':([38,67,],[66,91,]),'stmt':([38,67,95,96,],[67,67,103,104,]),'selectionStmt':([38,67,95,96,],[70,70,70,70,]),'iterationStmt':([38,67,95,96,],[71,71,71,71,]),'inputStmt':([38,67,95,96,],[72,72,72,72,]),'outputStmt':([38,67,95,96,],[73,73,73,73,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> foo","S'",1,None,None,None),
  ('foo -> program','foo',1,'p_foo','rust_parser.py',53),
  ('program -> declarationList','program',1,'p_program','rust_parser.py',60),
  ('declarationList -> declaration','declarationList',1,'p_declarationList','rust_parser.py',77),
  ('declarationList -> declaration declarationList','declarationList',2,'p_declarationList','rust_parser.py',78),
  ('declaration -> varDeclaration','declaration',1,'p_declaration','rust_parser.py',89),
  ('declaration -> constDeclaration','declaration',1,'p_declaration','rust_parser.py',90),
  ('declaration -> staticDeclaration','declaration',1,'p_declaration','rust_parser.py',91),
  ('declaration -> funcDeclaration','declaration',1,'p_declaration','rust_parser.py',92),
  ('varDeclaration -> LET IDVAR EQUAL IDVAR SEMCL','varDeclaration',5,'p_varDeclaration','rust_parser.py',100),
  ('varDeclaration -> LET IDVAR EQUAL INTVR SEMCL','varDeclaration',5,'p_varDeclaration','rust_parser.py',101),
  ('varDeclaration -> LET IDVAR EQUAL STRNG SEMCL','varDeclaration',5,'p_varDeclaration','rust_parser.py',102),
  ('varDeclaration -> LET IDVAR EQUAL expression SEMCL','varDeclaration',5,'p_varDeclaration','rust_parser.py',103),
  ('constDeclaration -> CONST IDVAR EQUAL IDVAR SEMCL','constDeclaration',5,'p_constDeclaration','rust_parser.py',114),
  ('staticDeclaration -> STATIC IDVAR EQUAL IDVAR SEMCL','staticDeclaration',5,'p_staticDeclaration','rust_parser.py',121),
  ('funcDeclaration -> FN function','funcDeclaration',2,'p_funcDeclaration','rust_parser.py',128),
  ('function -> FN parameters block','function',3,'p_function','rust_parser.py',137),
  ('parameters -> OPENP CLOSP','parameters',2,'p_parameters','rust_parser.py',146),
  ('parameters -> OPENP paramList CLOSP','parameters',3,'p_parameters','rust_parser.py',147),
  ('paramList -> parameter','paramList',1,'p_paramList','rust_parser.py',161),
  ('paramList -> parameter COMMA paramList','paramList',3,'p_paramList','rust_parser.py',162),
  ('parameter -> IDVAR','parameter',1,'p_parameter','rust_parser.py',174),
  ('block -> LBCKT RBCKT','block',2,'p_block','rust_parser.py',183),
  ('block -> LBCKT statement-list RBCKT','block',3,'p_block','rust_parser.py',184),
  ('statement-list -> stmt','statement-list',1,'p_statement_list','rust_parser.py',199),
  ('statement-list -> stmt statement-list','statement-list',2,'p_statement_list','rust_parser.py',200),
  ('stmt -> expression','stmt',1,'p_stmt','rust_parser.py',211),
  ('stmt -> declaration','stmt',1,'p_stmt','rust_parser.py',212),
  ('stmt -> selectionStmt','stmt',1,'p_stmt','rust_parser.py',213),
  ('stmt -> iterationStmt','stmt',1,'p_stmt','rust_parser.py',214),
  ('stmt -> inputStmt','stmt',1,'p_stmt','rust_parser.py',215),
  ('stmt -> outputStmt','stmt',1,'p_stmt','rust_parser.py',216),
  ('expression -> basicExp','expression',1,'p_expression','rust_parser.py',224),
  ('expression -> assignmentExp SEMCL','expression',2,'p_expression','rust_parser.py',225),
  ('expression -> comparisonExp','expression',1,'p_expression','rust_parser.py',226),
  ('expression -> boolExp','expression',1,'p_expression','rust_parser.py',227),
  ('basicExp -> IDVAR','basicExp',1,'p_basic','rust_parser.py',235),
  ('basicExp -> INTVR','basicExp',1,'p_basic','rust_parser.py',236),
  ('basicExp -> STRNG','basicExp',1,'p_basic','rust_parser.py',237),
  ('identifier -> IDVAR','identifier',1,'p_id','rust_parser.py',245),
  ('identifier -> INTVR','identifier',1,'p_id','rust_parser.py',246),
  ('assignmentExp -> identifier sumOp basicExp','assignmentExp',3,'p_assignment_expression','rust_parser.py',255),
  ('assignmentExp -> identifier sumOp assignmentExp','assignmentExp',3,'p_assignment_expression','rust_parser.py',256),
  ('comparisonExp -> basicExp relop basicExp','comparisonExp',3,'p_compExp','rust_parser.py',267),
  ('comparisonExp -> basicExp relop comparisonExp','comparisonExp',3,'p_compExp','rust_parser.py',268),
  ('relop -> LESST','relop',1,'p_relop','rust_parser.py',276),
  ('relop -> LSSEQ','relop',1,'p_relop','rust_parser.py',277),
  ('relop -> GREAT','relop',1,'p_relop','rust_parser.py',278),
  ('relop -> GRTEQ','relop',1,'p_relop','rust_parser.py',279),
  ('relop -> EQUAL','relop',1,'p_relop','rust_parser.py',280),
  ('relop -> UNEQL','relop',1,'p_relop','rust_parser.py',281),
  ('relop -> EQLTO','relop',1,'p_relop','rust_parser.py',282),
  ('sumOp -> ADDOP','sumOp',1,'p_sumOp','rust_parser.py',291),
  ('sumOp -> SUBOP','sumOp',1,'p_sumOp','rust_parser.py',292),
  ('sumOp -> DEROP','sumOp',1,'p_sumOp','rust_parser.py',293),
  ('sumOp -> QUOOP','sumOp',1,'p_sumOp','rust_parser.py',294),
  ('sumOp -> EQUAL','sumOp',1,'p_sumOp','rust_parser.py',295),
  ('sumOp -> REMOP','sumOp',1,'p_sumOp','rust_parser.py',296),
  ('selectionStmt -> IF expression EQUAL block','selectionStmt',4,'p_selectionStmt','rust_parser.py',305),
  ('selectionStmt -> IF expression EQUAL block ELSE','selectionStmt',5,'p_selectionStmt','rust_parser.py',306),
  ('iterationStmt -> FOR expression IN expression','iterationStmt',4,'p_iterationStmt','rust_parser.py',315),
  ('iterationStmt -> WHILE expression EQUAL expression','iterationStmt',4,'p_iterationStmt','rust_parser.py',316),
  ('iterationStmt -> WHILE expression LESST expression','iterationStmt',4,'p_iterationStmt','rust_parser.py',317),
  ('iterationStmt -> WHILE expression GREAT expression','iterationStmt',4,'p_iterationStmt','rust_parser.py',318),
  ('inputStmt -> STDIN OPENP stmt CLOSP','inputStmt',4,'p_input_stmt','rust_parser.py',335),
  ('outputStmt -> PRINTLN OPENP stmt CLOSP','outputStmt',4,'p_output_stmt','rust_parser.py',342),
  ('boolExp -> TRUE','boolExp',1,'p_boolExp','rust_parser.py',349),
  ('boolExp -> FALSE','boolExp',1,'p_boolExp','rust_parser.py',350),
]
