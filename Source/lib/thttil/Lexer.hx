/**
 * MIT License
 * 
 * Copyright (c) 2019 Renondedju
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
 
package thttil;

import thttil.error.LexerError;
import thttil.symbols.Definitions;

class Lexer extends hxparse.Lexer implements hxparse.RuleBuilder
{
	// This buffer is used to read strings 
    static var temp_buffer: StringBuf;
	static var identifier : String = "_*[a-zA-Z][a-zA-Z0-9_]*|_+[0-9][_a-zA-Z0-9]*";

	static function make(lexer: hxparse.Lexer, token_definition: TokenDefinition): Token
	{
		return new Token(token_definition, lexer.curPos());
	}

	// Main token rule
    public static var tokens = @:rule [

		// Litterals
		'"'	=> {
			temp_buffer = new StringBuf();

			var position_min = lexer.curPos();
			var position_max = try lexer.token(string) catch (exception: haxe.io.Eof) throw new LexerError(UnterminatedString, position_min);

			var token = make(lexer, thttil.symbols.TokenDefinition.TConst(CString(temp_buffer.toString())));

			token.position.pmin = position_min.pmin;
			token;
		},

		"%"	=> {
			temp_buffer = new StringBuf();

			var position_min = lexer.curPos();
			var position_max = try lexer.token(print) catch (exception: haxe.io.Eof) throw new LexerError(UnterminatedPrintToken, position_min);

			var token = make(lexer, thttil.symbols.TokenDefinition.TPrintToken(temp_buffer.toString()));

			token.position.pmin = position_min.pmin;
			token;
		},

		"[\r\n\t ]+" 			=> lexer.token(tokens), // Ignoring whitespaces
		"#[^\n\r]*"  			=> lexer.token(tokens), // Ignoring comments

		"as"					=> make(lexer, thttil.symbols.TokenDefinition.TKeyword(thttil.symbols.Keyword.KwdAs)),
		"using"					=> make(lexer, thttil.symbols.TokenDefinition.TKeyword(thttil.symbols.Keyword.KwdUsing)),
		
		"\\."					=> make(lexer, thttil.symbols.TokenDefinition.TDot),
		"\\)"					=> make(lexer, thttil.symbols.TokenDefinition.TEndToken),
		"\\$\\("				=> make(lexer, thttil.symbols.TokenDefinition.TBeginToken),
		"@"						=> make(lexer, thttil.symbols.TokenDefinition.TBeginStream),
		"\\$"					=> make(lexer, thttil.symbols.TokenDefinition.TBeginVariable),
		">"						=> make(lexer, thttil.symbols.TokenDefinition.TEndUsingString),
		"<"						=> make(lexer, thttil.symbols.TokenDefinition.TBeginUsingString),
		"->"					=> make(lexer, thttil.symbols.TokenDefinition.TStreamRedirection),
		","						=> make(lexer, thttil.symbols.TokenDefinition.TArgumentSeparator),
		"}"						=> make(lexer, thttil.symbols.TokenDefinition.TEndInstructionBlock),
		"{"						=> make(lexer, thttil.symbols.TokenDefinition.TBeginInstructionBlock),
		identifier				=> make(lexer, thttil.symbols.TokenDefinition.TConst(CIdent(lexer.current))),

		"" => make(lexer, TEOF)
	];

	static var string = @:rule [
		"\\\\t" => {
			temp_buffer.addChar("\t".code);
			lexer.token(string);
		},
		"\\\\n" => {
			temp_buffer.addChar("\n".code);
			lexer.token(string);
		},
		"\\\\r" => {
			temp_buffer.addChar("\r".code);
			lexer.token(string);
		},
		'\\\\a' => {	// Bell
			temp_buffer.addChar(7);
			lexer.token(string);
		},
		'\\\\b' => {	// Backspace
			temp_buffer.addChar(8);
			lexer.token(string);
		},
		'\\\\f' => {	// New page
			temp_buffer.addChar(12);
			lexer.token(string);
		},
		'\\\\v' => {	// Vertical tab
			temp_buffer.addChar(11);
			lexer.token(string);
		},
		'\\\\"' => {
			temp_buffer.addChar('"'.code);
			lexer.token(string);
		},
		'"' => {
			lexer.curPos().pmax;
		},
		'[^"]' => {
			temp_buffer.add(lexer.current);
			lexer.token(string);
		}
	];

	static var print  = @:rule [
		"\\\\t" => {
			temp_buffer.addChar("\t".code);
			lexer.token(print);
		},
		"\\\\n" => {
			temp_buffer.addChar("\n".code);
			lexer.token(print);
		},
		"\\\\r" => {
			temp_buffer.addChar("\r".code);
			lexer.token(print);
		},
		'\\\\a' => {	// Bell
			temp_buffer.addChar(7);
			lexer.token(print);
		},
		'\\\\b' => {	// Backspace
			temp_buffer.addChar(8);
			lexer.token(print);
		},
		'\\\\f' => {	// New page
			temp_buffer.addChar(12);
			lexer.token(print);
		},
		'\\\\v' => {	// Vertical tab
			temp_buffer.addChar(11);
			lexer.token(print);
		},
		'\\\\%' => {
			temp_buffer.addChar('%'.code);
			lexer.token(print);
		},
		'\\%' => {
			lexer.curPos().pmax;
		},
		'[^%]' => {
			temp_buffer.add(lexer.current);
			lexer.token(print);
		}
	];
}