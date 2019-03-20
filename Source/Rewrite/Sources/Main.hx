import Parser;

class Main
{
    public static function main(): Void
    {
		var parser = new ThttilParser(byte.ByteData.ofString("
        $(OUT \"sample\")
        {
            %Lol%
            %Lol%
            %Lol%
            %Lol%
            %Lol%
            %Lol%
        }
"), "String test");

        trace(parser.parseProgram());
    }
}