import Parser;

class Main
{
    public static function main(): Void
    {
		var parser = new ThttilParser(byte.ByteData.ofString(".."), "String test");
        trace(parser.parseProgram());
    }
}