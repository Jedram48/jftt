
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEMODrightUMINUSrightPOWERDIVIDE LPAREN MINUS MOD NUMBER PLUS POWER RPAREN TIMES\n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression TIMES expression\n               | expression DIVIDE expression\n               | expression POWER expression\n               | expression MOD expression\n               | LPAREN expression RPAREN\n               | MINUS NUMBER %prec UMINUS\n               | NUMBER\n    '
    
_lr_action_items = {'LPAREN':([0,3,5,6,7,8,9,10,],[3,3,3,3,3,3,3,3,]),'MINUS':([0,1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,],[2,6,2,-9,2,2,2,2,2,2,-8,6,-1,-2,-3,-4,-5,-6,-7,]),'NUMBER':([0,2,3,5,6,7,8,9,10,],[4,11,4,4,4,4,4,4,4,]),'$end':([1,4,11,13,14,15,16,17,18,19,],[0,-9,-8,-1,-2,-3,-4,-5,-6,-7,]),'PLUS':([1,4,11,12,13,14,15,16,17,18,19,],[5,-9,-8,5,-1,-2,-3,-4,-5,-6,-7,]),'TIMES':([1,4,11,12,13,14,15,16,17,18,19,],[7,-9,-8,7,7,7,-3,-4,-5,-6,-7,]),'DIVIDE':([1,4,11,12,13,14,15,16,17,18,19,],[8,-9,-8,8,8,8,-3,-4,-5,-6,-7,]),'POWER':([1,4,11,12,13,14,15,16,17,18,19,],[9,-9,-8,9,9,9,9,9,9,9,-7,]),'MOD':([1,4,11,12,13,14,15,16,17,18,19,],[10,-9,-8,10,10,10,-3,-4,-5,-6,-7,]),'RPAREN':([4,11,12,13,14,15,16,17,18,19,],[-9,-8,19,-1,-2,-3,-4,-5,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,5,6,7,8,9,10,],[1,12,13,14,15,16,17,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression','file.py',54),
  ('expression -> expression MINUS expression','expression',3,'p_expression','file.py',55),
  ('expression -> expression TIMES expression','expression',3,'p_expression','file.py',56),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','file.py',57),
  ('expression -> expression POWER expression','expression',3,'p_expression','file.py',58),
  ('expression -> expression MOD expression','expression',3,'p_expression','file.py',59),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','file.py',60),
  ('expression -> MINUS NUMBER','expression',2,'p_expression','file.py',61),
  ('expression -> NUMBER','expression',1,'p_expression','file.py',62),
]
