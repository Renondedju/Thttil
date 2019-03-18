import Parser;

class Main
{
    public static function main(): Void
    {
		var parser = new ThttilParser(byte.ByteData.ofString("
        using <Lol.thtt>  as <Lol>

@default

%Extern variable test:   %   $(OUT   $extern_var)
%\nOUT     command test:   % $(OUT   \"sample\")
%\nCALL    command test:   % $(CALL  \"inspect\")
%\nPRINT   command test:   % $(PRINT \"sample\")
"), "String test");
        trace(parser.toString());
    }
}