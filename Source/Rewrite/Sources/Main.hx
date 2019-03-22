import Parser;

class Main
{
    public static function main(): Void
    {
		var parser = new ThttilParser(byte.ByteData.ofString("

@default

%Extern variable test:   %   $(OUT   $extern_var)
%\nOUT     command test:   % $(OUT   \"sample\")
%\nCALL    command test:   % $(CALL  \"inspect\")
%\nPRINT   command test:   % $(PRINT \"sample\")
%\nUPPER   command test:   % $(OUT $(UPPER \"sample\"))
%\nLOWER   command test:   % $(OUT $(LOWER \"SAMPLE\"))
%\nTITLE   command test:   % $(OUT $(TITLE \"sample sample SAMPLE\"))
%\nSHELL   command test:   % $(OUT $(SHELL \"cd\"))
%\nIFEQ    command test:   % $(IFEQ  \"equal\", \"equal\"){ $(OUT \"I should be printed!\"   ) } $(IFEQ  \"equal\", \"not equal\"){ $(OUT \"I shouldn't be printed!\") }
%\nIFNEQ   command test:   % $(IFNEQ \"equal\", \"equal\"){ $(OUT \"I shouldn't be printed!\") } $(IFNEQ \"equal\", \"not equal\"){ $(OUT \"I should be printed!\"   ) }
%\nCREATE  command test:   % $(CREATE \"MyVariableName\", \"Content of MyVariableName\") $(OUT $MyVariableName)
%\nSET     command test:   % $(SET    $MyVariableName , \"New content of MyVariableName\") $(OUT $MyVariableName)
%\nREPLACE command test:   % $(OUT $(REPLACE $MyVariableName, \"New\", \"Replaced\"))
%\nJOIN    command test:   % $(OUT $(JOIN $(SPLIT $MyVariableName, \" \"), \"_\"))
%\nFOREACH command test: \n% $(FOREACH \"iterator\", $(SPLIT $MyVariableName, \" \"))
{
    %   [% $(OUT $iterator.index.value) %/% $(OUT $iterator.index.max) %] % $(OUT $iterator.value) %\n%
}

@test

%This should now be writing in the named 'test' stream%

# Writes the current content of @test into @default 
@test -> @default

        "), "String test");

        trace(parser.parseProgram());
    }
}