package thttil.symbols;

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