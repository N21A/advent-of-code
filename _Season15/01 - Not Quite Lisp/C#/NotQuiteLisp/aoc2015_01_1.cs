/*
aoc2015_01_1.cs
----------------
Author: Nida Anis
Date: 31/12/2024
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Solution to Part 1 (Part 2 in aoc2015_01_2.cs)
*/

class Part1
{

    /// <summary>
    /// Gets Santa's final floor number.
    /// </summary>
    /// <param name="charArray"></param>
    /// <returns>Santa's final floor number.</returns>
    public static int GetFinalFloorNumber(char[] charArray)
    {
        int floorNumber = 0;

        for (int i = 0; i < charArray.Length; i++)
        {
            if (charArray[i] == '(')
            {
                floorNumber += 1;
            }

            else if (charArray[i] == ')')
            {
                floorNumber -= 1;
            }
        }

        return floorNumber;
    }
}