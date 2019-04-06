/**
 * MIT License
 * 
 * Copyright (c) 2019 Renondedju
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

package thttil.symbols;

import thttil.symbols.Argument;
import thttil.symbols.InstructionBlock;

/**
 * Parser representation of a token
 * 
 * $(COMMAND_NAME $Argment1, "Argument2", [...])
 */
class Token extends Argument
{
    public var command_name     : String;
    public var arguments        : Array<Argument>;
    public var instruction_block: InstructionBlock;

    public function new(command_name: String, arguments: Array<Argument>, position: hxparse.Position, instruction_block: InstructionBlock = null)
    {
        this.instruction_block  = instruction_block;
        this.command_name       = command_name;
        this.arguments          = arguments;
        
        super(position);
    }
}