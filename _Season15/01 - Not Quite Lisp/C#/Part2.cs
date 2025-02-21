/*
Part2.cs
-----------------
Author: Nida Anis
Date: 21/02/2025
-----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Solution to Part 2 (Part 1 in Part1.cs)
*/

class Part2
{
    public static int GetFirstBasementPos(char[] map)
    {
        int position = 0;
        int floorNum = 0;

        for (int i = 0; i < map.Length; i++)
        {
            position += 1;

            if (map[i] == '(')
            {
                floorNum += 1;
            }

            else if (map[i] == ')')
            {
                floorNum -= 1;
            }

            if (floorNum == -1)
            {
                return position;
            }
        }

        return -1;
    }
}