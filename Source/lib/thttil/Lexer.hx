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

class Lexer extends hxparse.Lexer implements hxparse.RuleBuilder
{
	// This buffer is used to read strings 
    static var temp_buffer: StringBuf;
	static var identifier : String = "_*[a-zA-Z][a-zA-Z0-9_]*|_+[0-9][_a-zA-Z0-9]*";

	// Main token rule
    public static var tokens = @:rule [

		// Litterals
		'"'	=> {
			temp_buffer = new StringBuf();
			lexer.token(string);
			thttil.Tokens.TokenDef.TConst(CString(temp_buffer.toString()));
		},

		"%"	=> {
			temp_buffer = new StringBuf();
			lexer.token(print);
			thttil.Tokens.TokenDef.TPrintToken(temp_buffer.toString());
		},

		"[\r\n\t ]+" 			=> lexer.token(tokens), 			  // Passing whitespaces
		"#[^\n\r]*"  			=> {
			#if keep_comments
			thttil.Tokens.TokenDef.TComment(lexer.current.substr(1)); // Passing comments
			#else
			lexer.token(tokens);
			#end
		},

		"as"					=> Tokens.TokenDef.TKeyword(Tokens.Keyword.KwdAs),
		"using"					=> Tokens.TokenDef.TKeyword(Tokens.Keyword.KwdUsing),
		
		"\\."					=> Tokens.TokenDef.TDot,
		"\\)"					=> Tokens.TokenDef.TEndToken,
		"\\$\\("				=> Tokens.TokenDef.TBeginToken,
		"@"						=> Tokens.TokenDef.TBeginStream,
		"\\$"					=> Tokens.TokenDef.TBeginVariable,
		">"						=> Tokens.TokenDef.TEndUsingString,
		"<"						=> Tokens.TokenDef.TBeginUsingString,
		"->"					=> Tokens.TokenDef.TStreamRedirection,
		","						=> Tokens.TokenDef.TArgumentSeparator,
		"}"						=> Tokens.TokenDef.TEndInstructionBlock,
		"{"						=> Tokens.TokenDef.TBeginInstructionBlock,
		identifier				=> Tokens.TokenDef.TConst(CIdent(lexer.current)),

		"" => TEOF
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