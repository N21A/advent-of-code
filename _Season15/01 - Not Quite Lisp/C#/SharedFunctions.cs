/*
SharedFunctions.cs
----------------
Author: Nida Anis
Date created: 21/02/2025
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Shared functions
*/

using System.IO;

namespace AdventOfCode2015;

public static class SharedFunctions
{
    public static char[] GetCharsFromFile()
    {
        string fileContent = File.ReadAllText("input.txt");
        char[] map = fileContent.ToCharArray();

        return map;
    }
}