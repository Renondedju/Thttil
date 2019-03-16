import Lexer;
import Tokens;

class ThttilParser extends hxparse.Parser<hxparse.LexerTokenSource<TokenDef>, TokenDef>
{
    public function new(input: byte.ByteData, sourceName: String)
    {
		var lexer        = new ThttilLexer(input, sourceName);
		var token_source = new hxparse.LexerTokenSource(lexer, ThttilLexer.tokens);
		super(token_source);
	}

    public function composeVariable(): Void
    {
        
    }

	public function parseThttil(): Dynamic
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