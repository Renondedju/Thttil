package thttil.symbols;

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