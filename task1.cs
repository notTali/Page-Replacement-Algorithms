using System;

public class Program
{
    public static void Main()
    {

        displayDetails();

    }

    static void displayDetails()
    {

        Console.Write("Enter your nickname: ");
        string nickname = Console.ReadLine();
        Console.Write("Enter your favourite series/movie: ");
        string movie = Console.ReadLine();

        Console.WriteLine("\nHello World");

        string details = "Name     : " + nickname + "\n";
        details = details + "Favourite: " + movie;

        Console.WriteLine(details);
    }
}