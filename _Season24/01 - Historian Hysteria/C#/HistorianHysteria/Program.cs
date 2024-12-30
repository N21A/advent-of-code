/*
Program.cs
----------------
Author: Nida Anis
Date: 30/12/2024
----------------
Description:
- Advent of Code 2024 Day 1: Historian Hysteria
- Main program entry point with menu selection for Part 1 or Part 2
*/

using AdventOfCode2024;

class Program
{
    static void Main(string[] args)
    {
        bool exit = false;

        while (!exit)
        {
            Console.WriteLine("Advent of Code 2024 Day 1: Historian Hysteria");
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

                Console.WriteLine(); // Blank line added for readability
            }
        }

    /// <summary>
    /// Runs Part 1 of the program.
    /// </summary>
    static void RunPart1()
    {
        Console.WriteLine("Running Part 1...");
        string[] lines = SharedFunctions.ReadInputFile();
        var lists = SharedFunctions.ParseInputFile(lines);
        int sumOfDistances = Part1.CalculateDistances(lists);
        Console.WriteLine("Sum of distances: " + sumOfDistances);
    }

    static void RunPart2()
    {
        string[] lines = SharedFunctions.ReadInputFile();
        var lists = SharedFunctions.ParseInputFile(lines);
        int sumOfSimilarityScores = Part2.CalculateSimilarityScores(lists);
        Console.WriteLine("Sum of similarity scores: " + sumOfSimilarityScores);

    }
}