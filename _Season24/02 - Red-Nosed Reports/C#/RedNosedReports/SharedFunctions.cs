/*
SharedFunctions.cs
----------------
Author: Nida Anis
Date: 30/12/2024
----------------
Description:
- Advent of Code 2024 Day 2: Red-Nosed Reports
- Shared functions
*/

namespace AdventOfCode2024;

public static class SharedFunctions
{

    /// <summary>
    /// Reads the input file and returns a list of lines.
    /// </summary>
    /// <returns></returns>
    public static string[] ReadInputFile()
    {
        string[] lines = File.ReadAllLines("input.txt");
        return lines;
    }

    /// <summary>
    /// Parses the list of lines into a jagged array of integers.
    /// </summary>
    /// <param name="lines">A list containing lines from the input file.</param>
    /// <returns></returns>
    public static int[][] ParseInputFile(string[] lines)
    {
        int[][] data = new int[lines.Length][];

        for (int i = 0; i < lines.Length; i++)
        {
            string[] numbers = lines[i].Split(' ', StringSplitOptions.RemoveEmptyEntries);
            data[i] = new int[numbers.Length];

            for (int j = 0; j < numbers.Length; j++)
            {
                data[i][j] = int.Parse(numbers[j]);
            }
        }

        return data;
    }
}