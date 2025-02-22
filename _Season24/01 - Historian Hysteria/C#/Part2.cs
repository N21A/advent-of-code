/*
Part2.cs
----------------
Author: Nida Anis
Date created: 22/02/2025
----------------
Description:
- Advent of Code 2024 Day 1: Historian Hysteria
- Solution to Part 2 (Part 1 in Part1.cs)
*/

class Part2
{
    public static int CalcSimilaritySum(List<string> list1, List<string> list2)
    {
        int count = 0;
        int similaritySum = 0;
        List<int> similarityScores = new List<int>();

        for (int i = 0; i < list1.Count; i++)
        {
            for (int j = 0; j < list2.Count; j++)
            {
                if (list1[i] == list2[j])
                {
                    count += 1;
                }
            }

            int num1 = int.Parse(list1[i]);
            int similarityScore = num1 * count;
            similarityScores.Add(similarityScore);
            count = 0;
        }

        for (int i = 0; i < similarityScores.Count; i++)
        {
            similaritySum += similarityScores[i];
        }

        return similaritySum;
    }
}