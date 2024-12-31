/*
Program.cs
----------------
Author: Nida Anis
Date: 31/12/2024
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Main program entry point with menu selection for Part 1 or Part 2
*/

using AdventOfCode2015;

class Program
{
    static void Main(string[] args)
    {
        bool exit = false;

        while(!exit)
        {
            Console.WriteLine("Advent of Code 2015 Day 1: Not Quite Lisp");
            Console.WriteLine("Please choose an option:");
            Console.WriteLine("1. Run Part 1");
            Console.WriteLine("2. Run Part 2");
            Console.WriteLine("3. Exit");
            Console.WriteLine("Enter your choice (1/2/3): ");

            string? choice = Console.ReadLine();
            if (choice != null)
            {
                switch (choice)
                {
                    case "1":
                        RunPart1();
                        break;
                    
                    case "2":
                        RunPart2();
                        break;
                    
                    case "3":
                        exit = true;
                        Console.WriteLine("Exiting the program...");
                        break;
                    
                    default:
                        Console.WriteLine("Invalid choice. Please enter 1, 2, or 3.");
                        break;
                }
            }

            Console.WriteLine(); // Blank line for readability
        }
    }

    /// <summary>
    /// Runs Part 1 of the program.
    /// </summary>
    static void RunPart1()
    {
        Console.WriteLine("Running Part 1...");
        char[] charArray = SharedFunctions.GetCharsFromFile();
        int floorNumber = Part1.GetFinalFloorNumber(charArray);
        Console.WriteLine("The instructions take Santa to Floor " + floorNumber + ".");
    }

    /// <summary>
    /// Runs Part 2 of the program.
    /// </summary>
    static void RunPart2()
    {
        Console.WriteLine("Running Part 2...");
        char[] charArray = SharedFunctions.GetCharsFromFile();
        int firstBasementPos = Part2.GetFirstBasementPos(charArray);
        Console.WriteLine("The position of the character that causes Santa to first enter the basement is " + firstBasementPos + ".");
    }
}