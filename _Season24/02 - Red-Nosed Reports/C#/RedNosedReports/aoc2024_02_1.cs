/*
aoc2024_02_1.cs
----------------
Author: Nida Anis
Date: 30/12/2024
----------------
Description:
- Advent of Code 2024 Day 2: Red-Nosed Reports
- Solution to Part 1 (Part 2 in aoc2024_02_2.cs)
*/

using System;
using System.Collections.Generic;
using System.Linq;

class Part1
{

    /// <summary>
    /// Calculates the number of safe reports
    /// </summary>
    /// <param name="data"></param>
    /// <returns></returns>
    public static int CalculateSafeReports(int[][] data)
    {
        int safeReports = 0;

        // Iterate through each report
        foreach (int[] report in data)
        {
            if (report.Length < 2) continue; // Skip invalid data

            List<int> differences = new List<int>();

            for (int i = 0; i < report.Length - 1; i++)
            {
                // Calculate differences between adjacent levels
                differences.Add(report[i + 1] - report[i]);
            }

            // Check for a consistent increase or decrease
            bool isIncreasing = differences.All(diff => diff > 0);
            bool isDecreasing = differences.All(diff => diff < 0);

            // Check if differences are within the valid range
            bool validDifferences = differences.All(diff => Math.Abs(diff) >= 1 && Math.Abs(diff) <= 3);

            if (validDifferences && (isIncreasing || isDecreasing))
            {
                safeReports += 1;
            }
        }

        return safeReports;
    }
}