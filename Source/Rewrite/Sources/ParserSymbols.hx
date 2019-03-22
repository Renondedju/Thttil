/**
 * This file contains a list of all the parser symbols required to make a THTTIL program
 * 
 * PROGRAM    = TOKEN*
 * TOKEN      = '$(' COMMAND ARUMENT+ ')' (| '{' TOKEN* '}')
 * ARGUMENT   = (VARIABLE | TOKEN | STRING | STREAM_TAG)
 * COMMAND    = IDENTIFIER
 * VARIABLE   = '$' IDENTIFIER
 * STRING     = '"' [^"]* '"'
 */

/**
 * A THTTIL program is a special kind of instruction block
 * (or you can think of it the other way around)
 * \see ParserToken
 */
class ParserProgram extends ParserInstructionBlock
{
    public function new(instructions: Array<ParserToken>)
    {
        super(instructions);
    }
}

/**
 * This is just a parent class
 */
class ParserTokenArgument
{}

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


/**
 * Variable
 * $MyVarName
 */
class ParserVariable extends ParserTokenArgument
{
    public var name      : String;
    public var sub_scopes: Array<String>;

    public function new(name: String, sub_scopes: Array<String>)
    {
        this.name       = name;
        this.sub_scopes = sub_scopes;
    }
}

/**
 * A Stream is a special kind of variale
 * @StreamName
 */
class ParserStream extends ParserVariable
{
    public function new(name: String)
    {
        super(name, []);
    }
}

/**
 * Simple string
 * "Some Content"
 */
class ParserString extends ParserTokenArgument
{
    public var content: String;

    public function new(content: String)
    {
        this.content = content;
    }
}

/**
 * A simple list of instructions
 * '{' TOKEN* '}'
 */ 
class ParserInstructionBlock
{
    public var instructions: Array<ParserToken>;

    public function new(instructions: Array<ParserToken>)
    {
        this.instructions = instructions;
    }
}