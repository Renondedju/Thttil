import Parser;

/**
 * Main test class
 */
class Test
{
    public static function main(): Void
    {
        var parser = new ThttilParser(byte.ByteData.ofString("
        $(OUT \"test\")
        {
            %This is a simple test !%
            $(COMMAND $Variable, \"String\")
        }"), "Test program");
        trace(parser.parseProgram());
    }
}