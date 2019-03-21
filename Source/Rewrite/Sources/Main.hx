import Parser;

class Main
{
    public static function main(): Void
    {
		var parser = new ThttilParser(byte.ByteData.ofString("

$(OUT $test.lol.test.lol.test)

        "), "String test");

        trace(parser.parseProgram());
    }
}