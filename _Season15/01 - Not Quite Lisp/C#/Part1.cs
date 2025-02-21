/*
Part1.cs
----------------
Author: Nida Anis
Date created: 21/02/2025
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Solution to Part 1 (Part 2 in Part2.cs)
*/

class Part1
{
    public static int GetFinalFloorNumber(char[] map)
    {
        int floorNum = 0;

        for (int i = 0; i < map.Length; i++)
        {
            if (map[i] == '(')
            {
                floorNum += 1;
            }

            else if (map[i] == ')')
            {
                floorNum -= 1;
            }
        }

        return floorNum;
    }
}