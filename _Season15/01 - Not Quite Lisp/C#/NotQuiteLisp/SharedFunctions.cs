/*
SharedFunctions.cs
----------------
Author: Nida Anis
Date: 31/12/2024
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Shared functions
*/
using System.IO;

namespace AdventOfCode2015;

public static class SharedFunctions
{

    /// <summary>
    /// Reads the input file and returns a list of characters.
    /// </summary>
    /// <returns>A list of characters from the input file.</returns>
    public static char[] GetCharsFromFile()
    {
        string fileContent = File.ReadAllText("input.txt");
        char[] charArray = fileContent.ToCharArray();

        return charArray;
    }
}