using System;
using static System.Console;

namespace practice
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random_digit = new Random();

            int digit = random_digit.Next(1, 11);
            double dble = random_digit.NextDouble();
            double dble2 = random_digit.NextDouble() * 10;
            double randomDoubleResult = random_digit.NextDouble() + random_digit.Next(100);


            WriteLine($"digit: {digit}, dble: {dble}, dble2: {dble2}, {randomDoubleResult}");

            int small_big = 0;

            small_big = (digit < 5) ? 0 : 1;

            var value = (small_big == 0) ? "SMALL" : "BIG";

            WriteLine($"small_big: {digit} - {small_big} - {value}");

            Random rand = new Random();
            int thousand = rand.Next(0, 11);
            bool odd_even = (thousand % 2 == 0) ? true : false;
            var label = (odd_even) ? "even" : "odd";
            WriteLine($"digit {thousand} is {label}");

            bool compare = (digit > thousand) ? true : false;
            var winner = (compare) ? "digit wins" : "thousand wins";
            WriteLine($"Results: digit {digit} against thousand {thousand} => {winner}");


            int day = random_digit.Next(0, 7);

            switch (day)
            {
                case 0:
                    WriteLine("Monday");
                    break;
                case 1:
                    WriteLine("Tuesday");
                    break;
                case 2:
                    WriteLine("Wednesday");
                    break;
                case 3:
                    WriteLine("Thursday");
                    break;
                case 4:
                    WriteLine("Friday");
                    break;
                case 5:
                    WriteLine("Saturday");
                    break;
                default:
                    WriteLine("Sunday");
                    break;
            }

            int three = random_digit.Next(1, 4);

            switch (three)
            {
                case 1:
                    WriteLine("Scissors!");
                    break;
                case 2:
                    WriteLine("Stone!");
                    break;
                default:
                    WriteLine("Paper!");
                    break;
            }

            switch (odd_even)
            {
                case true:
                    WriteLine("It's even!");
                    break;
                default:
                    WriteLine("It's odd!");
                    break;
            }

            if (day == 0) WriteLine("Monday");
            else if (day == 1) WriteLine("Tuesday");
            else if (day == 2) WriteLine("Wednesday");
            else WriteLine("Thursday");
        }
    }
}
