
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'program_allleftPLUSMINUSleftTIMESDIVleftMODASSIGN CLOSE_BRACKET CLOSE_PAREN COMMA COMMENT DIV DO ELSE END ENDIF ENDWHILE EQ GE GT IDENTIFIER IF IN IS LE LT MINUS MOD NEQ NUM OPEN_BRACKET OPEN_PAREN PLUS PROCEDURE PROGRAM READ REPEAT SEMICOLON THEN TIMES UNTIL WHILE WRITEprogram_all : mainmain : PROGRAM IS declarations IN commands END\n            | PROGRAM IS IN commands ENDcommands : commandcommand : identifier ASSIGN expression SEMICOLONdeclarations : IDENTIFIERdeclarations : declarations COMMA IDENTIFIERexpression : valuevalue : NUM\n             | identifieridentifier : IDENTIFIER'
    
_lr_action_items = {'PROGRAM':([0,],[3,]),'$end':([1,2,16,18,],[0,-1,-3,-2,]),'IS':([3,],[4,]),'IN':([4,5,7,15,],[6,8,-6,-7,]),'IDENTIFIER':([4,6,8,9,17,],[7,13,13,15,13,]),'COMMA':([5,7,15,],[9,-6,-7,]),'END':([10,11,14,23,],[16,-4,18,-5,]),'ASSIGN':([12,13,],[17,-11,]),'SEMICOLON':([13,19,20,21,22,],[-11,-10,23,-8,-9,]),'NUM':([17,],[22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program_all':([0,],[1,]),'main':([0,],[2,]),'declarations':([4,],[5,]),'commands':([6,8,],[10,14,]),'command':([6,8,],[11,11,]),'identifier':([6,8,17,],[12,12,19,]),'expression':([17,],[20,]),'value':([17,],[21,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program_all","S'",1,None,None,None),
  ('program_all -> main','program_all',1,'p_program_all','_parser.py',19),
  ('main -> PROGRAM IS declarations IN commands END','main',6,'p_main','_parser.py',30),
  ('main -> PROGRAM IS IN commands END','main',5,'p_main','_parser.py',31),
  ('commands -> command','commands',1,'p_commands','_parser.py',40),
  ('command -> identifier ASSIGN expression SEMICOLON','command',4,'p_command','_parser.py',55),
  ('declarations -> IDENTIFIER','declarations',1,'p_declarations','_parser.py',82),
  ('declarations -> declarations COMMA IDENTIFIER','declarations',3,'p_mult_declarations','_parser.py',86),
  ('expression -> value','expression',1,'p_expression','_parser.py',111),
  ('value -> NUM','value',1,'p_value','_parser.py',124),
  ('value -> identifier','value',1,'p_value','_parser.py',125),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier','_parser.py',135),
]
