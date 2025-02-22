/*
SharedFunctions.cs
----------------
Author: Nida Anis
Date created: 21/02/2025
----------------
Description:
- Advent of Code 2024 Day 1: "Historian Hysteria"
- Shared functions
*/

using System.Data;
using System.IO;

namespace AdventOfCode2024;

public static class SharedFunctions
{
    public static (List<string>, List<string>) GetInputFromFile()
    {
        List<string> list1 = new List<string>();
        List<string> list2 = new List<string>();

        foreach (string line in File.ReadLines("input.txt"))
        {
            string[] row = line.Split(new[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
            list1.Add(row[0]);
            list2.Add(row[1]);
        }

        list1.Sort();
        list2.Sort();

        return (list1, list2);

    }
}