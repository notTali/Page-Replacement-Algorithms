using System;

public class Program
{
    public static void Main()
    {
        Console.Write("Enter the length of the room:");
        double length = Convert.ToDouble(Console.ReadLine());

        Console.Write("Enter the width of the room:");
        double width = Convert.ToDouble(Console.ReadLine());



        Console.WriteLine("The estimated amount is: " + calcCost(length, width).ToString("N2")); // N2 is for rounding to 2 decimal place.
    }

    static double calcCost(double length, double width)
    {

        double cost = 20 * (2 * 2.6 * length + 2 * 2.6 * width);
        return cost;
    }


}