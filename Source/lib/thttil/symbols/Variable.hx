package thttil.symbols;

/**
 * Variable
 * $MyVarName
 */
class Variable extends Argument
{
    public var name      : String;
    public var sub_scopes: Array<String>;

    public function new(name: String, sub_scopes: Array<String>)
    {
        this.name       = name;
        this.sub_scopes = sub_scopes;
    }
}