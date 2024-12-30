/*
aoc2024_02_2.cs
----------------
Author: Nida Anis
Date: 30/12/2024
----------------
Description:
- Advent of Code 2024 Day 2: Red-Nosed Reports
- Solution to Part 2 (Part 1 in aoc2024_02_1.cs)
*/

using System;
using System.Collections.Generic;
using System.Linq;

class Part2
{

    /// <summary>
    /// Calculates the number of safe reports
    /// </summary>
    /// <param name="data"></param>
    /// <returns></returns>
    public static int CalculateSafeReportsWithDampener(int[][] data)
    {
        int safeReportsWithDampener = 0;

        // Iterate through each report
        foreach (int[] report in data)
        {
            if (report.Length < 2) continue; // Skip invalid data

            bool isSafeWithDampener = false;
            
            // Attempt to remove each element and validate the dampened report
            for (int i = 0; i < report.Length; i++)
            {
                // Apply the Problem Dampener
                int[] dampenedReport = report.Where((_, index) => index != i).ToArray();

                List<int> differences = new List<int>();

                // Calculate differences for the dampened report
                for (int j = 0; j < dampenedReport.Length - 1; j++)
                {
                    differences.Add(dampenedReport[j + 1] - dampenedReport[j]);
                }

                // Check for a consistent increase or decrease
                bool isIncreasing = differences.All(diff => diff > 0);
                bool isDecreasing = differences.All(diff => diff < 0);

                // Check if differences are within the valid range
                bool validDifferences = differences.All(diff => Math.Abs(diff) >= 1 && Math.Abs(diff) <= 3);

                if (validDifferences && (isIncreasing || isDecreasing))
                {
                    isSafeWithDampener = true;
                    break; // No need to check further dampened versions
                }
            }

            if (isSafeWithDampener)
            {
                safeReportsWithDampener += 1;
            }
        }

        return safeReportsWithDampener;
    }
}