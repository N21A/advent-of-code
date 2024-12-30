/*
SharedFunctions.cs
----------------
Author: Nida Anis
Date: 30/12/2024
----------------
Description:
- Advent of Code 2024 Day 1: Historian Hysteria
- Shared functions
*/

namespace AdventOfCode2024;

public static class SharedFunctions
{

    /// <summary>
    /// Reads the input file and returns a list of lines.
    /// </summary>
    public static string[] ReadInputFile()
    {
        string[] lines = File.ReadAllLines("input.txt");
        return lines;
    }

    /// <summary>
    /// Parses the list of lines and splits it into two lists: list1 and list2.
    /// </summary>
    /// <param name="lines">A list containing lines from the input file.</param>
    public static (List<string> list1, List<string> list2) ParseInputFile(string[] lines)
    {
        List<string> list1 = new List<string>();
        List<string> list2 = new List<string>();

        foreach (string line in lines)
        {
            string trimmedLine = line.Trim();

            // Split the file into individual lists
            string[] row = trimmedLine.Split(' ');
            if (row.Length >= 2) // Make sure there's at least two columns
            {
                // Create lists for each column
                list1.Add(row[0]);
                list2.Add(row[row.Length - 1]);
            }
        }

        // Sort the lists
        list1.Sort();
        list2.Sort();

        return (list1, list2);
    }
}