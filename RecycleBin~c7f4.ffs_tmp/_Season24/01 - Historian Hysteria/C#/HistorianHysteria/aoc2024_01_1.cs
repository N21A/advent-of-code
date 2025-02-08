/*
aoc2024_01_1.cs
----------------
Author: Nida Anis
Date: 29/12/2024
----------------
Description:
- Advent of Code 2024 Day 1: Historian Hysteria
- Solution to Part 1 (Part 2 in aoc2024_01_2.cs)
*/

using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.InteropServices;
using AdventOfCode2024;

class Part1
{
    
    /// <summary>
    /// Calculates the sum of the distances between items in list1 and items in list2.
    /// </summary>
    /// <param name="lists">A tuple containing two lists: list1 and list2.</param>
    public static int CalculateDistances((List<string> list1, List<string> list2) lists)
    {
        List<int> distances = new List<int>();
        int sumOfDistances = 0;

        // Calculate distances
        for (int i = 0; i < lists.list1.Count; i++)
        {
            int distance = Math.Abs(int.Parse(lists.list1[i]) - int.Parse(lists.list2[i]));
            distances.Add(distance);
        }

        // Sum distances
        for (int i = 0; i < distances.Count; i++)
        {
            sumOfDistances += distances[i];
        }

        return sumOfDistances;
    }
}
