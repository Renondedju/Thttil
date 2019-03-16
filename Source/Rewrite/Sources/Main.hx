import Parser;

class Main
{
    public static function main(): Void
    {
		var parser = new ThttilParser(byte.ByteData.ofString("  
            # yjeyfizufyez
            $test.test.test @test->@test \" \\\"\\aSome content\" $"), "String test");

        trace(parser.parseThttil());
    }
}