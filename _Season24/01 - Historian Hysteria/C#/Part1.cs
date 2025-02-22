/*
Part1.cs
----------------
Author: Nida Anis
Date created: 22/02/2025
----------------
Description:
- Advent of Code 2024 Day 1: Historian Hysteria
- Solution to Part 1 (Part 2 in Part2.cs)
*/

class Part1
{
    public static int CalcDistanceSum(List<string> list1, List<string> list2)
    {
        int distanceSum = 0;
        List<int> distances = new List<int>();

        for (int i = 0; i < list1.Count; i++)
        {
            int num1 = int.Parse(list1[i]);
            int num2 = int.Parse(list2[i]);
            int diff = Math.Abs(num1 - num2);
            distances.Add(diff);
        }

        for (int i = 0; i < distances.Count; i++)
        {
            distanceSum += distances[i];
        }

        return distanceSum;
        
    }

}