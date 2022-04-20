using System;

public class Program
{
    public static void Main()
    {

        Console.Write("Enter your nickname: ");
        string nickname = Console.ReadLine();
        Console.Write("Enter your favourite series/movie: ");
        string movie = Console.ReadLine();

        Console.WriteLine("\nHello World\n" + displayDetails(nickname, movie) + "\n");

    }

    static string displayDetails(string nickname, string movie)
    {
        string details = "Name     : " + nickname + "\n";
        details = details + "Favourite: " + movie;

        return details;
    }
}