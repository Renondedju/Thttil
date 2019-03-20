import haxe.macro.Expr;

enum Keyword
{
    KwdAs;    // as
    KwdUsing; // using
}

enum TokenDef
{
    TPrintToken(content: String);                   // %Some random content%
    TKeyword   (keyword: Keyword);                  // Cound be "as" or "using"
    TComment   (content: String);                   // A comment (# Hello :D)  
    TConst     (const  : haxe.macro.Expr.Constant); // Could be a string or an identifier

    TDot;                    // .
    TEndToken;               // )
    TBeginToken;             // $(
    TBeginStream;            // @
    TBeginVariable;          // $
    TEndUsingString;         // >
    TBeginUsingString;       // <
    TStreamRedirection;      // ->
    TArgumentSeparator;      // ,
    TEndInstructionBlock;    // }
    TBeginInstructionBlock;  // {
    TEOF;                    // <EOF>
}