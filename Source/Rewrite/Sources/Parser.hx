import Lexer;
import Tokens;
import Symbols;

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
     * @return ThttilProgram
     */
    public function parseProgram(): ThttilProgram
    {
        var program: ThttilProgram = new ThttilProgram();
        var token  : ThttilToken   = null;

        // Looking for all the tokens in the file.
        // If parseToken() return null, then the End Of File is reached and our
        // program has been successfully parsed.
        do
        {
            token = parseToken();
            if (token != null)
                program.tokens.push(token);
        }
        while (token != null);

        return program;
    }

    /**
     * Looks for a token to create
     * @return ThttilToken The parsed token or null if EOF has been reached.
     */
    public function parseToken(): ThttilToken
    {
        return hxparse.Parser.parse(switch stream
        {
            // Found a classic token: $(COMMAND "args...")
            case [TBeginToken, TConst(CIdent(command_name)), arguments = parseTokenArguments([]), block = parseTokenInstructionBlock()]:
                new ThttilToken(new ThttilCommand(), arguments, block);

            // Found a print token
            case [TPrintToken(content)]:
                new ThttilToken(new ThttilCommand(), [new ThttilString(content)], null);
            
            // End of file. Not more tokens to parse.
            case [TEOF]:
                null;
        });
    }

    /**
     * Parses a token instruction block
     * @return ThttilTokenList a token list or null if nothing has been found
     */
    public function parseTokenInstructionBlock(): Array<ThttilToken>
    {
        if (peek(0) != TBeginInstructionBlock)
            return null;

        junk();
        return parseTokenInstructionBlockContent([]);
    }

    /**
     * Parses the content of an instruction block
     * @param accumulator 
     * @return Array<ThttilToken> instruction block
     */
    public function parseTokenInstructionBlockContent(accumulator: Array<ThttilToken>): Array<ThttilToken>
    {
        return hxparse.Parser.parse(switch stream{
            case [TEndInstructionBlock]: accumulator;
            case [token = parseToken()]:
                accumulator.push(token);
                switch stream{
                    case [TEndInstructionBlock]: accumulator;
                    case _: parseTokenInstructionBlockContent(accumulator);
                }
        });
    }

    /**
     * Parses token arguments.
     * @param accumulator 
     * @return Array<ThttilArgument> arguments
     */
    public function parseTokenArguments(accumulator: Array<ThttilArgument>): Array<ThttilArgument>
    {
        return hxparse.Parser.parse(switch stream
        {
            case [TEndToken]: accumulator;
            case [arg = parseTokenArgumentContent()]:
                accumulator.push(arg);
                switch stream
                {
                    case [TEndToken]: accumulator;
                    case [TArgumentSeparator]: parseTokenArguments(accumulator);
                }
        });
    }

    /**
     * Parses a token argument content
     * @return ThttilArgument argument
     */
    public function parseTokenArgumentContent(): ThttilArgument
    {
        return hxparse.Parser.parse(switch stream
        {
            case [TBeginVariable, TConst(CIdent(identifier))]:
                new ThttilVariable(identifier, null);
            case [TConst(CString(content))]:
                new ThttilString(content);
            case [TBeginStream, TConst(CIdent(identifier))]:
                new ThttilStream(identifier);
            case [token = parseToken()]:
                token;
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