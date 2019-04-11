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

import thttil.Lexer;

import thttil.error.ParserError;
import thttil.error.ParserErrorMessage;

import thttil.symbols.InstructionBlock;
import thttil.symbols.Definitions;
import thttil.symbols.Argument;
import thttil.symbols.PString;
import thttil.symbols.Program;
import thttil.symbols.Stream;
import thttil.symbols.Token;

class Parser extends hxparse.Parser<hxparse.LexerTokenSource<thttil.Token>, thttil.Token>
{
    private var source_name: String;

    public function new(input: byte.ByteData, source_name: String)
    {
		var lexer        = new thttil.Lexer(input, source_name);
		var token_source = new hxparse.LexerTokenSource(lexer, thttil.Lexer.tokens);

        this.source_name = source_name;

		super(token_source);
	}

    private function parsingError(error: thttil.error.ParserErrorMessage)
    {
        trace(error);
    }

    private static function punion(position1: hxparse.Position, position2: hxparse.Position): hxparse.Position
    {
        return new hxparse.Position(
            position1.psource,
            position1.pmin < position2.pmin ? position1.pmin : position2.pmin,
			position1.pmax > position2.pmax ? position1.pmax : position2.pmax
        );
    }

    /**
     * Parses a thttil program
     * @return ParserProgram
     */
    public function parseProgram(): thttil.symbols.Program
    {
        var program: thttil.symbols.Program = new thttil.symbols.Program([], new hxparse.Position(source_name, 0, 0));
        var token  : thttil.symbols.Token   = null;

        // Looking for all the tokens in the file.
        // If parseToken() return null, then the End Of File is reached and our
        // program has been successfully parsed.
        do
        {
            token = parseToken();
            if (token != null)
            {
                program.instructions.push(token);
                program.position.pmax = token.position.pmax;
            }
        }
        while (token != null);

        return program;
    }

    /**
     * Looks for a token to create
     * @return ParserToken The parsed token or null if EOF has been reached.
     */
    public function parseToken(): thttil.symbols.Token
    {
        return hxparse.Parser.parse(switch stream
        {
            // If we found the following pattern : @SomeStreamName
            case [{token: TBeginStream, position: pos1}, {token: TConst(CIdent(istream)), position: pos2}]:
                switch stream
                {
                    // And next to the previous pattern there is "->@SomeOtherStreamName"
                    case [{token: TStreamRedirection}, {token: TBeginStream, position: pos3}, {token: TConst(CIdent(ostream)), position: pos4}]:

                        // This is a stream redirection from istream to ostream
                        new thttil.symbols.Token("REDIRECTION",
                            [new thttil.symbols.Stream(istream, punion(pos1, pos2)),
                             new thttil.symbols.Stream(ostream, punion(pos3, pos4))],
                            punion(pos1, pos4), null);

                    // Otherwise, this is a simple stream selection
                    case _:
                        new thttil.symbols.Token("SELECT", [new thttil.symbols.Stream(istream, punion(pos1, pos2))], punion(pos1, pos2), null);
                }

            // If there is the following pattern : $(COMMAND_NAME "Arg1", $arg2, @arg3, [...])
            case [{token: TBeginToken, position: pos}, {token: TConst(CIdent(command_name))}, arguments = parseTokenArguments({array: [], max: 0}), block = parseTokenInstructionBlock()]:

                // This is a token in it's most basic form
                pos.pmax = arguments.max;

                if (block.instructions != null)
                    pos = punion(pos, block.position);

                new thttil.symbols.Token(command_name, arguments.array, pos, block);

            // If there is the following pattern: %Some random content ...%
            case [{token: TPrintToken(content), position: pos}]:

                // This is a simplified OUT token
                new thttil.symbols.Token("OUT", [new thttil.symbols.PString(content, pos)], pos, null);

            // And if this is the end of the file, returning 'null'.
            case [{token: TEOF}]:
                null;
        });
    }

    /**
     * Parses a token instruction block
     * @return Array<thttil.symbols.Token> a token list or null if nothing has been found
     */
    public function parseTokenInstructionBlock(): thttil.symbols.InstructionBlock
    {
        return hxparse.Parser.parse(switch stream{

            // If we don't found a '{' then there is no instruction block following.
            case [{token: TBeginInstructionBlock, position: pos}]:

                // Parsing all the instructions in the block ...
                var content = parseTokenInstructionBlockContent({array: [], max: 0});
                pos.pmax = content.max;
                new thttil.symbols.InstructionBlock(content.array, pos);

            case _:

                new thttil.symbols.InstructionBlock(null, null);
        });
    }

    /**
     * Parses the content of an instruction block
     * @param accumulator This allows the compilator to do some optimizations since we are doing recursive calls :/
     * @return Array<thttil.symbols.Token> instruction block
     */
    public function parseTokenInstructionBlockContent(accumulator: {array: Array<thttil.symbols.Token>, max: Int}): {array: Array<thttil.symbols.Token>, max: Int}
    {
        return hxparse.Parser.parse(switch stream{

            // If we found '}', this means that this is the end of the block.
            case [{token: TEndInstructionBlock, position: pos}]:
                accumulator.max = pos.pmax;
                accumulator;

            // Otherwise this means that there must be a token to parse here !
            case [token = parseToken()]:

                // Adding the parsed token to the list
                accumulator.array.push(token);
                switch stream {

                    // Then checking again if there is '}' to tell
                    // us if this is the end of the block or not
                    case [{token: TEndInstructionBlock, position: pos}]:
                        accumulator.max = pos.pmax;
                        accumulator;

                    // Otherwise, there is another token to parse ...
                    case _: parseTokenInstructionBlockContent(accumulator);
                }
        });
    }

    /**
     * Parses token arguments.
     * @param accumulator This allows the compilator to do some optimizations since we are doing recursive calls :/
     * @return Array<thttil.symbols.Argument> arguments
     */
    public function parseTokenArguments(accumulator: {array: Array<thttil.symbols.Argument>, max: Int}): {array: Array<thttil.symbols.Argument>, max: Int}
    {
        return hxparse.Parser.parse(switch stream {

            // If there is a ')', then this is the end of the token.
            case [{token: TEndToken, position: pos}]:
                accumulator.max = pos.pmax;
                accumulator;

            // Otherwise, there is still other arguments to parse !
            case [arg = parseTokenArgumentContent()]:

                // Adding the parsed argument to the list
                accumulator.array.push(arg);
                switch stream {

                    // Then checking again if there is ')' to tell
                    // us if this is the end of the token or not
                    case [{token: TEndToken, position: pos}]:
                        accumulator.max = pos.pmax;
                        accumulator;

                    // Otherwise, there is another argument to parse ...
                    case [{token: TArgumentSeparator}]: parseTokenArguments(accumulator);
                }
        });
    }

    /**
     * Parses a token argument content
     * @return thttil.symbols.Argument argument
     */
    public function parseTokenArgumentContent(): thttil.symbols.Argument
    {
        return hxparse.Parser.parse(switch stream
        {
            // If the argument looks like this : $SomeName or like this $This.is.also.a.variable
            case [{token: TBeginVariable, position: pos}, {token: TConst(CIdent(identifier))}, sub_scopes = parseVariableSubScopes({array: [], max: 0})]:

                // Then we found a variable
                pos.pmax = sub_scopes.max;
                new thttil.symbols.Variable(identifier, sub_scopes.array, pos);

            // If the argument looks like this: "Some string content"
            case [{token: TConst(CString(content)), position: pos}]:

                // Then we found a string
                new thttil.symbols.PString(content, pos);

            // If the argument looks like this: @StreamName
            case [{token: TBeginStream, position: pos1}, {token: TConst(CIdent(identifier)), position: pos2}]:

                // Then we found a stream
                new thttil.symbols.Stream(identifier, punion(pos1, pos2));

            // And finally if the argument looks like this: $(COMMAND "Args...")
            case [token = parseToken()]:

                // Then we found a token.
                token;
        });
    }

    /**
     * A variable sub scope is simply the name of a sub object of that variable
     * eg. $Person.job or $Song.length
     * @param accumulator This allows the compilator to do some optimizations since we are doing recursive calls :/
     * @return Array<String> sub scopes
     */
    public function parseVariableSubScopes(accumulator: {array: Array<String>, max: Int}): {array: Array<String>, max: Int}
    {
        return hxparse.Parser.parse(switch stream{

            // If there is the following pattern: .some_name
            case [{token: TDot}, {token: TConst(CIdent(identifier)), position: pos}]:

                // Then we found a sub scope
                accumulator.max = pos.pmax;
                accumulator.array.push(identifier);

                // Looking for the next sub scope
                parseVariableSubScopes(accumulator);

            // Otherwise, we found everything that we could.
            case _: accumulator;
        });
    }

	/**
     * @deprecated Test function.
     * 
	 * Returns the string representation of the current parsed file or input
	 * @return String tree representation
	 */
	public function toString(): String
	{
		var tree: String = "";
        while (true)
        {
            switch (stream.token())
            {
                case {token: TDot}:
                    tree += "Dot ";
                case {token: TEndToken}:
                    tree += "EndToken ";
                case {token: TBeginToken}:
                    tree += "BeginToken ";
                case {token: TBeginStream}:
                    tree += "BeginStream ";
                case {token: TBeginVariable}:
                    tree += "BeginVariable ";
                case {token: TEndUsingString}:
                    tree += "EndUsingString ";
                case {token: TBeginUsingString}:
                    tree += "BeginUsingString ";
                case {token: TStreamRedirection}:
                    tree += "StreamRedirection ";
                case {token: TArgumentSeparator}:
                    tree += "ArgumentSeparator ";
                case {token: TEndInstructionBlock}:
                    tree += "EndInstructionBlock ";
                case {token: TBeginInstructionBlock}:
                    tree += "BeginInstructionBlock ";
                case {token: TPrintToken(content)}:
                    tree += "TPrintToken (" + content + ") ";
                case {token: TConst(CString(content))}:
                    tree += "String (" + content + ") ";
                case {token: TConst(CIdent(name))}:
                    tree += "Identifier (" + name + ") ";
                case {token: TKeyword(keyword)}:
                    tree += "Keyword (" + keyword + ") ";
                case {token: TComment(content)}:
                    tree += "Comment (" + content + ") ";
                case {token: TEOF}:
                    tree += "EOF";
                    return tree;
                case _:
                    return tree + "! UNEXPECTED !"; 
            }
        }
	}
}