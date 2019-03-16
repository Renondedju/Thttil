import Lexer;
import Tokens;

class ThttilParser extends hxparse.Parser<hxparse.LexerTokenSource<TokenDef>, TokenDef>
{
    public function new(input: byte.ByteData, source_name: String)
    {
		var lexer        = new ThttilLexer(input, source_name);
		var token_source = new hxparse.LexerTokenSource(lexer, ThttilLexer.tokens);
		super(token_source);
	}

    public function parseProgram(): String
    {
        return hxparse.Parser.parse(switch stream
        {
            case [TDot, TDot, TEOF]:
                return "Dot-EOF";
            case [TEOF]:
                return "EOF";
        });
    }

	/**
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

    public function composeVariable(): Void
    {
        
    }

}