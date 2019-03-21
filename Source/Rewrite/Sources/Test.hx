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
            @stream
            @stream->@other_stream
        }"), "Test program");
        trace(parser.parseProgram());
    }
}