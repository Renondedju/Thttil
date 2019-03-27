package thttil.symbols;

/**
 * Parser representation of a token
 * 
 * $(COMMAND_NAME $Argment1, "Argument2", [...])
 */
class ParserToken extends ParserTokenArgument
{
    public var command_name     : String;
    public var arguments        : Array<ParserTokenArgument>;
    public var instruction_block: Array<ParserToken>;

    public function new(command_name: String, arguments: Array<ParserTokenArgument>, instruction_block: Array<ParserToken> = null)
    {
        this.instruction_block  = instruction_block;
        this.command_name       = command_name;
        this.arguments          = arguments;
    }
}