package thttil.symbols;

import thttil.symbols.Argument;

/**
 * Parser representation of a token
 * 
 * $(COMMAND_NAME $Argment1, "Argument2", [...])
 */
class Token extends Argument
{
    public var command_name     : String;
    public var arguments        : Array<Argument>;
    public var instruction_block: Array<Token>;

    public function new(command_name: String, arguments: Array<Argument>, instruction_block: Array<Token> = null)
    {
        this.instruction_block  = instruction_block;
        this.command_name       = command_name;
        this.arguments          = arguments;
    }
}