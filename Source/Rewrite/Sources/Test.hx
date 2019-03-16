import Parser;

/**
 * Main test class
 */
class Test
{
    public static function main(): Void
    {
        var parser = new ThttilParser(byte.ByteData.ofString(".."), "Test program");
        trace(parser.parseProgram());
    }
}