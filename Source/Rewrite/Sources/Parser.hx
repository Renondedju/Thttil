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
                program.tokens.push(token)
        }
        while (token != null)

        return program;
    }

    /**
     * Looks for a token to create
     * @return ThttilToken The parsed token or null if EOF has been reached.
     */
    public function parseToken(): ThttilToken
    {
        return hxparse.Parse.parse(switch stream
        {
            // Found a classic token: $(COMMAND "args...")
            case [TBeginToken]:
                null; // TODO parse token

            // Found a print token
            // TODO rename TPrintCommand to TPrintToken
            case [TPrintCommand(content)]:
                null; // TODO parse token

            // End of file. Not more tokens to parse.
            case [TEOF]:
                null;
            
            // TODO Error, unexpected token.
            case _:
                null;
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
            switch stream.token()
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
                case TPrintCommand(content):
                    tree += "PrintCommand (" + content + ") ";
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