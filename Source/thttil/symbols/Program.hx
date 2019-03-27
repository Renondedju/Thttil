package thttil.symbols;

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