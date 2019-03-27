package thttil.symbols;

import thttil.symbols.InstructionBlock;
import thttil.symbols.Token;

/**
 * A THTTIL program is a special kind of instruction block
 * (or you can think of it the other way around)
 * \see Token
 */
class Program extends InstructionBlock
{
    public function new(instructions: Array<Token>)
    {
        super(instructions);
    }
}