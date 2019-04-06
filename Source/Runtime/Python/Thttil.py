import thttil

def main():

    content = thttil.Bytes.ofString(
"""
@test
@test->@test
%test%
$(OUT "test")
$(UPPER $variable)
""")

    parser = thttil.Parser(content, "Test.thtt")

    for instruction in parser.parseProgram().instructions:
        print("{0.command_name:<15} @{0.position.psource}:{0.position.pmin:<5} {1}".format(instruction, content.getString(instruction.position.pmin, instruction.position.pmax - instruction.position.pmin)))

if __name__ == "__main__":
    main()