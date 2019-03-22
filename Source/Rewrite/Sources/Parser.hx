import Lexer;
import Tokens;

// Parser symbols are not the same as the "executable" symbols that we are gonna use
// to create and interpret the program.
import ParserSymbols;

class ThttilParser extends hxparse.Parser<hxparse.LexerTokenSource<TokenDef>, TokenDef>
{
    public function new(input: byte.ByteData, source_name: String)
    {
		var lexer        = new ThttilLexer(input, source_name);
		var token_source = new hxparse.LexerTokenSource(lexer, ThttilLexer.tokens);
		super(token_source);
	}

    /**
     * Parses a thttil program
     * @return ParserProgram
     */
    public function parseProgram(): ParserProgram
    {
        var program: ParserProgram = new ParserProgram([]);
        var token  : ParserToken   = null;

        // Looking for all the tokens in the file.
        // If parseToken() return null, then the End Of File is reached and our
        // program has been successfully parsed.
        do
        {
            token = parseToken();
            if (token != null)
                program.instructions.push(token);
        }
        while (token != null);

        return program;
    }

    /**
     * Looks for a token to create
     * @return ParserToken The parsed token or null if EOF has been reached.
     */
    public function parseToken(): ParserToken
    {
        return hxparse.Parser.parse(switch stream
        {
            // If we found the following pattern : @SomeStreamName
            case [TBeginStream, TConst(CIdent(istream))]:
                switch stream
                {
                    // And next to the previous pattern there is "->@SomeOtherStreamName"
                    case [TStreamRedirection, TBeginStream, TConst(CIdent(ostream))]:

                        // This is a stream redirection from istream to ostream
                        new ParserToken("REDIRECTION", [new ParserStream(istream), new ParserStream(ostream)], null);

                    // Otherwise, this is a simple stream selection
                    case _:
                        new ParserToken("SELECT", [new ParserStream(istream)], null);
                }

            // If there is the following pattern : $(COMMAND_NAME "Arg1", $arg2, @arg3, [...])
            case [TBeginToken, TConst(CIdent(command_name)), arguments = parseTokenArguments([]), block = parseTokenInstructionBlock()]:

                // This is a token in it's most basic form
                new ParserToken(command_name, arguments, block);

            // If there is the following pattern: %Some random content ...%
            case [TPrintToken(content)]:

                // This is a simplified OUT token
                new ParserToken("OUT", [new ParserString(content)], null);

            // And if this is the end of the file, returning 'null'.
            case [TEOF]:
                null;
        });
    }

    /**
     * Parses a token instruction block
     * @return Array<ParserToken> a token list or null if nothing has been found
     */
    public function parseTokenInstructionBlock(): Array<ParserToken>
    {
        // If we don't found a '{' then there is no instruction block following.
        if (peek(0) != TBeginInstructionBlock)
            return null;

        junk();

        // Parsing all the instructions in the block ...
        return parseTokenInstructionBlockContent([]);
    }

    /**
     * Parses the content of an instruction block
     * @param accumulator This allows the compilator to do some optimizations since we are doing recursive calls :/
     * @return Array<ThttilToken> instruction block
     */
    public function parseTokenInstructionBlockContent(accumulator: Array<ParserToken>): Array<ParserToken>
    {
        return hxparse.Parser.parse(switch stream{

            // If we found '}', this means that this is the end of the block.
            case [TEndInstructionBlock]: accumulator;

            // Otherwise this means that there must be a token to parse here !
            case [token = parseToken()]:

                // Adding the parsed token to the list
                accumulator.push(token);
                switch stream {

                    // Then checking again if there is '}' to tell
                    // us if this is the end of the block or not
                    case [TEndInstructionBlock]: accumulator;

                    // Otherwise, there is another token to parse ...
                    case _: parseTokenInstructionBlockContent(accumulator);
                }
        });
    }

    /**
     * Parses token arguments.
     * @param accumulator This allows the compilator to do some optimizations since we are doing recursive calls :/
     * @return Array<ParserTokenArgument> arguments
     */
    public function parseTokenArguments(accumulator: Array<ParserTokenArgument>): Array<ParserTokenArgument>
    {
        return hxparse.Parser.parse(switch stream {

            // If there is a ')', then this is the end of the token.
            case [TEndToken]: accumulator;

            // Otherwise, there is still other arguments to parse !
            case [arg = parseTokenArgumentContent()]:

                // Adding the parsed argument to the list
                accumulator.push(arg);
                switch stream {

                    // Then checking again if there is ')' to tell
                    // us if this is the end of the token or not
                    case [TEndToken]: accumulator;

                    // Otherwise, there is another argument to parse ...
                    case [TArgumentSeparator]: parseTokenArguments(accumulator);
                }
        });
    }

    /**
     * Parses a token argument content
     * @return ThttilArgument argument
     */
    public function parseTokenArgumentContent(): ParserTokenArgument
    {
        return hxparse.Parser.parse(switch stream
        {
            // If the argument looks like this : $SomeName or like this $This.is.also.a.variable
            case [TBeginVariable, TConst(CIdent(identifier)), sub_scopes = parseVariableSubScopes([])]:

                // Then we found a variable
                new ParserVariable(identifier, sub_scopes);

            // If the argument looks like this: "Some string content"
            case [TConst(CString(content))]:

                // Then we found a string
                new ParserString(content);

            // If the argument looks like this: @StreamName
            case [TBeginStream, TConst(CIdent(identifier))]:

                // Then we found a stream
                new ParserStream(identifier);

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
    public function parseVariableSubScopes(accumulator: Array<String>): Array<String>
    {
        return hxparse.Parser.parse(switch stream{

            // If there is the following pattern: .some_name
            case [TDot, TConst(CIdent(identifier))]:

                // Then we found a sub scope
                accumulator.push(identifier);

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
                case TDot:
                    tree += "Dot ";
                case TEndToken:
                    tree += "EndToken ";
                case TBeginToken:
                    tree += "BeginToken ";
                case TBeginStream:
                    tree += "BeginStream ";
                case TBeginVariable:
                    tree += "BeginVariable ";
                case TEndUsingString:
                    tree += "EndUsingString ";
                case TBeginUsingString:
                    tree += "BeginUsingString ";
                case TStreamRedirection:
                    tree += "StreamRedirection ";
                case TArgumentSeparator:
                    tree += "ArgumentSeparator ";
                case TEndInstructionBlock:
                    tree += "EndInstructionBlock ";
                case TBeginInstructionBlock:
                    tree += "BeginInstructionBlock ";
                case TPrintToken(content):
                    tree += "TPrintToken (" + content + ") ";
                case TConst(CString(content)):
                    tree += "String (" + content + ") ";
                case TConst(CIdent(name)):
                    tree += "Identifier (" + name + ") ";
                case TKeyword(keyword):
                    tree += "Keyword (" + keyword + ") ";
                case TComment(content):
                    tree += "Comment (" + content + ") ";
                case TEOF:
                    tree += "EOF";
                    return tree;
                case _:
                    return tree + "! UNEXPECTED !"; 
            }
        }
	}
}