/*
Program.cs
----------------
Author: Nida Anis
Date created: 21/02/2025
----------------
Description:
- Advent of Code 2015 Day 1: Not Quite Lisp
- Main program entry point with menu selection
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
                switch(choice)
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

    static void RunPart1()
    {
        Console.WriteLine("Running Part 1...");
        char[] map = SharedFunctions.GetCharsFromFile();
        int floorNumber = Part1.GetFinalFloorNumber(map);
        Console.WriteLine("The instructions take Santa to Floor " + floorNumber + ".");
    }

    static void RunPart2()
    {
        Console.WriteLine("Running Part 2...");
        char[] map = SharedFunctions.GetCharsFromFile();
        int firstBasementPos = Part2.GetFirstBasementPos(map);
        Console.WriteLine("The position of the first character that causes Santa to enter the basement is " + firstBasementPos + ".");
    }
}