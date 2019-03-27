package thttil.symbols;

import thttil.symbols.Argument;

/**
 * Simple string
 * "Some Content"
 */
class PString extends Argument
{
    public var content: String;

    public function new(content: String)
    {
        this.content = content;
    }
}