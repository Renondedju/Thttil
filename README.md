# Thttil

<p align="center">
  <a href="https://discord.gg/TpmPFM3">
    <img alt="Logo" src="https://discordapp.com/api/guilds/550366032708108301/widget.png?style=banner2">
  </a>
</p>

[Link](https://github.com/BasileCombet/Thttil/releases) to the latest release.  
  
Thttil is an interpreted language made to generate files.  
The power of Thttil is its extensibility. Since the language is hosted, you can  
control everything from the file lexer/parser to the interpretation through the variable pool and  
builtin features.  
  
**Mhhh ok but why should I use Thttil instead of using any other technology ?**  
  
Thttil will probably be way more maintainable and readable than any other solution.  
Also since this is an interpreted language, no compilation time is required to make changes to your project.  
Thttil is conceived to be intuitive and easy to use so you don't need to be a technical person things to edit template files.  
Finally if your project requires very specific algorithms that are not included in the builtin commands, you can easily extend the language in 5 minutes.  

**Here are some use cases:**
* Automatic language binding generation (eg. Lua binding with C++ using [Sol2](https://github.com/ThePhD/sol2/))
* Custom documentation generator by combining doxygen XML and the python lib [lxml](https://lxml.de/)
* Configuration file generator
* C++ header tool to add reflection to the language (eg. [Unreal Header Tool](https://docs.unrealengine.com/en-us/Programming/BuildTools))  
The real limit here is your imagination. 

**Ok nice, you convicted me, where do I learn how to use Thttil ?**

Here is a link to the [wiki](https://github.com/BasileCombet/Thttil/wiki), everything you need to know about Thttil is in here !

We also have syntax highlight support for your favorite code editor over [here](https://github.com/BasileCombet/Thttil/tree/master/Language/Apps).

# Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) to know what to do.

# Dependencies

## Antlr4 by Terence Parr

What is ANTLR?  
ANTLR (ANother Tool for Language Recognition) is a powerful parser generator for reading, processing, executing, or translating structured text or binary files. It's widely used to build languages, tools, and frameworks. From a grammar, ANTLR generates a parser that can build and walk parse trees. From the [Antlr website](https://www.antlr.org/)

# Licence

MIT Licence

Copyright (c) 2019 Basile Combet

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.