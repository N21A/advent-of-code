/*
aoc2015_01_2.cs
----------------
Author: Nida Anis
Date: 31/12/2024
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Solution to Part 2 (Part 1 in aoc2015_01_1.cs)
*/

class Part2
{

    /// <summary>
    /// Gets the position of the first character that causes Santa to enter the basement.
    /// </summary>
    /// <param name="charArray"></param>
    /// <returns>The position of the first character that causes Santa to enter the basement.</returns>
    public static int GetFirstBasementPos(char[] charArray)
    {
        int pos = 0;
        int floorNumber = 0;

        for (int i = 0; i < charArray.Length; i++)
        {
            pos += 1;

            if (charArray[i] == '(')
            {
                floorNumber += 1;
            }
            else if (charArray[i] == ')')
            {
                floorNumber -= 1;
            }

            if (floorNumber == -1)
            {
                return pos;
            }
        }

        return -1;
    }
}