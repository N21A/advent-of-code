/*
aoc2024_01_2.cs
----------------
Author: Nida Anis
Date: 29/12/2024
----------------
Description:
- Advent of Code 2024 Day 1: Historian Hysteria
- Solution to Part 2 (Part 1 in aoc2024_01_1.cs)
*/

using System;
using System.Collections.Generic;
using AdventOfCode2024;

class Part2
{

    /// <summary>
    /// Calculates the sum of the similarity scores between items in list1 and items in list2.
    /// </summary>
    /// <param name="lists">A tuple containing two lists: list1 and list2.</param>
    /// <returns></returns>
    public static int CalculateSimilarityScores((List<string> list1, List<string> list2) lists)
    {
        int count = 0;
        int sumOfSimilarityScores = 0;
        List<int> similarityScores = new List<int>();

        // Calculate similarity scores
        for (int i = 0; i < lists.list1.Count; i++)
        {
            for (int j = 0; j < lists.list2.Count; j++)
            {
                if (lists.list1[i] == lists.list2[j])
                {
                    count += 1;
                }

                similarityScores.Add(int.Parse(lists.list1[i]) * count);
                count = 0;
            }
        }

        // Sum similarity scores
        for (int i = 0; i < similarityScores.Count; i++)
        {
            sumOfSimilarityScores += similarityScores[i];
        }

        return sumOfSimilarityScores;
    }
}