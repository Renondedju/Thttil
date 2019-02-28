grammar Thttil;

/*

MIT License

Copyright (c) 2019 Basile Combet

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

*/

/*
 * Parser Rules
 */

// Main rule, allows program parsing
program             : commands+=command* EOF ;

// Argument: this may be any command argument
// Syntax  : $var or @extern_var or "String" or $(COMMAND "args...")
argument            : VARIABLE | STRING | command ;

// Print command: this allows for easier file reading
// Syntax       :   %Some arbitrary content%
// Translated to:   $(OUT "Some arbitrary content")
print_command       : PRINT ;

// Command    : this is anything that can execute something and be replaced by it's result
// Syntax     : $(FUNCTION "Some arbitrary content", $some_more ...)
// Replaced by: FUNCTION return value
command             : '$(' function=FUNCTION (| args+=argument (',' args+=argument)*) ')' ('{' commands+=command* '}')?
                    | print_command
                    ;

/*
 * Lexer Rules
 */

fragment LOWERCASE          : [a-z] ;
fragment UPPERCASE          : [A-Z] ;
fragment CHAR               : [a-zA-Z] ;
fragment PROTECTED_PRINT    : '\\\\' | '\\%' ;
fragment PROTECTED_STRING   : '\\\\' | '\\"' ;

FUNCTION            : UPPERCASE+ ;
PRINT               : '%' (PROTECTED_PRINT  | ~[%])*? '%' ;
STRING              : '"' (PROTECTED_STRING | ~["])*? '"' ;
VARIABLE            : '$' (CHAR | '_' | '-' | '.')+ ;
COMMENT             : '#' ~( '\r' | '\n' )* -> skip ;
WHITESPACE          : [ \t\n\r]+ -> skip ;