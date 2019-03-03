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
program             : using* (command | stream_tag | stream_redirection)* EOF ;

// Argument: this may be any command argument
// Syntax  : $var or @extern_var or "String" or $(COMMAND "args...")
argument            : (VARIABLE | STRING)
                    | command ;

// Stream tag: Allows to change the current output stream
// Syntax    : @StreamName or @namespace.StreamName
stream_tag          : STREAM_TAG ;

// Stream redirection: Allows to write the content of one stream into another
// Syntax            : @test.default -> @default
stream_redirection  : input_stream=STREAM_TAG ARROW output_stream=STREAM_TAG ;

// Print command: this allows for easier file reading
// Syntax       :   %Some arbitrary content%
// Translated to:   $(OUT "Some arbitrary content")
print_command       : PRINT ;

using               : USING BEGIN_USING_STRING FILENAME END_USING_STRING (| AS BEGIN_USING_STRING ALIAS END_USING_STRING) ;

// Command    : this is anything that can execute something and be replaced by it's result
// Syntax     : $(FUNCTION "Some arbitrary content", $some_more ...)
// Replaced by: FUNCTION return value
command             : BEGIN_TOKEN function=FUNCTION (| args+=argument (ARGUMENT_SEPARATOR args+=argument)*) END_TOKEN
                      (BEGIN_INSTRUCTION_BLOCK commands+=instruction_block_content* END_INSTRUCTION_BLOCK)?
                    | print_command
                    ;

instruction_block_content : (command | stream_tag | stream_redirection) ;

/*
 * Lexer Rules
 */

// Fragments
fragment LOWERCASE          : [a-z] ;
fragment UPPERCASE          : [A-Z] ;
fragment CHAR               : [a-zA-Z] ;

// Keywords
USING                   : 'using' ;
AS                      : 'as' ;
ARROW                   : '->' ;
END_USING_STRING        : '>' ;
BEGIN_USING_STRING      : '<' ;
BEGIN_TOKEN             : '$(' ;
END_TOKEN               : ')' ;
ARGUMENT_SEPARATOR      : ',' ;
BEGIN_INSTRUCTION_BLOCK : '{' ;
END_INSTRUCTION_BLOCK   : '}' ;

// Literals
PRINT               : '%' ('\\\\' | '\\%' | ~[%])*? '%' ;
STRING              : '"' ('\\\\' | '\\"' | ~["])*? '"' ;

// Objects
STREAM_TAG          : '@' (CHAR+? '.')? CHAR+ ;
VARIABLE            : '$' (CHAR | '_' | '-' | '.')+ ;

// Identifiers
FUNCTION            : UPPERCASE+ ;
ALIAS               : CHAR+ ;
FILENAME            : (CHAR | '_' | '-' | '.')+ ;

// Skipped tokens
COMMENT             : '#' ~( '\r' | '\n' )* -> skip ;
WHITESPACE          : [ \t\n\r]+ -> skip ;