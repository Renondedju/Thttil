import thttil

def main():

    collection = thttil.StreamCollection()
    collection.getNamedStream("default").append("Test")

    print(collection.getNamedStream("default").get())

    parser = thttil.Parser(thttil.Bytes.ofString(
"""
@test
@test->@test
%test%
$(OUT "test")
"""), "Test Source")

    for instruction in parser.parseProgram().instructions:
        print(instruction.command_name, "\t", instruction.arguments)

if __name__ == "__main__":
    main()