package thttil.symbols;

import thttil.symbols.Token;

/**
 * A simple list of instructions
 * '{' TOKEN* '}'
 */ 
class InstructionBlock
{
    public var instructions: Array<Token>;

    public function new(instructions: Array<Token>)
    {
        this.instructions = instructions;
    }
}