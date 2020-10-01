using System;
using System.Collections.Generic;
using static System.Console;

namespace practice
{
    class Program
    {
        static void Main(string[] args)
        {
            Random random_digit = new Random();

            //int digit = random_digit.Next(1, 11);
            //double dble = random_digit.NextDouble();
            //double dble2 = random_digit.NextDouble() * 10;
            //double randomDoubleResult = random_digit.NextDouble() + random_digit.Next(100);


            //WriteLine($"digit: {digit}, dble: {dble}, dble2: {dble2}, {randomDoubleResult}");

            //int small_big = 0;

            //small_big = (digit < 5) ? 0 : 1;

            //var value = (small_big == 0) ? "SMALL" : "BIG";

            //WriteLine($"small_big: {digit} - {small_big} - {value}");

            //Random rand = new Random();
            //int thousand = rand.Next(0, 11);
            //bool odd_even = (thousand % 2 == 0) ? true : false;
            //var label = (odd_even) ? "even" : "odd";
            //WriteLine($"digit {thousand} is {label}");

            //bool compare = (digit > thousand) ? true : false;
            //var winner = (compare) ? "digit wins" : "thousand wins";
            //WriteLine($"Results: digit {digit} against thousand {thousand} => {winner}");


            //int day = random_digit.Next(0, 7);

            //switch (day)
            //{
            //    case 0:
            //        WriteLine("Monday");
            //        break;
            //    case 1:
            //        WriteLine("Tuesday");
            //        break;
            //    case 2:
            //        WriteLine("Wednesday");
            //        break;
            //    case 3:
            //        WriteLine("Thursday");
            //        break;
            //    case 4:
            //        WriteLine("Friday");
            //        break;
            //    case 5:
            //        WriteLine("Saturday");
            //        break;
            //    default:
            //        WriteLine("Sunday");
            //        break;
            //}

            //int three = random_digit.Next(1, 4);

            //switch (three)
            //{
            //    case 1:
            //        WriteLine("Scissors!");
            //        break;
            //    case 2:
            //        WriteLine("Stone!");
            //        break;
            //    default:
            //        WriteLine("Paper!");
            //        break;
            //}

            //switch (odd_even)
            //{
            //    case true:
            //        WriteLine("It's even!");
            //        break;
            //    default:
            //        WriteLine("It's odd!");
            //        break;
            //}

            //if (day == 0) WriteLine("Monday");
            //else if (day == 1) WriteLine("Tuesday");
            //else if (day == 2) WriteLine("Wednesday");
            //else WriteLine("Thursday");

            //int a = 1;
            //int b = 2;

            //if (a > b) a = a + b; else a = b - a;


            //for (int i = 0; i < 10; i++)
            //{
            //    Write(i);
            //}

            //WriteLine();
            //for (int j = 0; j < 10; j++)
            //{
            //    Write(10 - j);
            //}

            //WriteLine();
            //for (int n = -5; n < 5; n++)
            //{
            //    Write(n);
            //}

            //WriteLine();
            //for (int m = 10; m > 0; m--)
            //{
            //    Write(m);
            //}

            //WriteLine();
            //for (int k = 2; k < 100; k+=2)
            //{
            //    Write($"{k}, ");
            //}

            //int num = 1;

            //for (; ; )
            //{
            //    int s = num * 2;
            //    if (s > 1000)
            //    {
            //        break;
            //    }
            //    Write(s);
            //    num++;
            //}

            //-----------------------------------
            //GUESS GAME

            //Random digit = new Random();
            //int secret = digit.Next(1, 101);
            //int turn = 1;
            //int last_guess = 0;
            //int guess = secret;
            //bool less = true;
            //int max = 1001;
            //int min = 0;

            //for (; ; )
            //{
            //    if (turn % 2 != 0)
            //    {
            //        WriteLine("Human:");
            //        guess = int.Parse(ReadLine());
            //    }
            //    else
            //    {
            //    WriteLine("Computer:");
            //    guess = digit.Next(min+1 , max);
            //    WriteLine($"{guess} \n");
            //    }

            //    turn++;

            //    if (guess > secret)
            //    {
            //        less = true;
            //        WriteLine("--------------");
            //        WriteLine("LESS!");
            //        if (max > guess) max = guess;
            //    }
            //    else if (guess < secret)
            //    {
            //        less = false;
            //        WriteLine("--------------");
            //        WriteLine("MORE!");
            //        if (min < guess) min = guess;
            //    }

            //    else
            //    {
            //        WriteLine("Winner!");
            //        break;
            //    }
            //    WriteLine($"{min}-{max} \n");
            //}


            //-----------------------------------

            int counter = 0;
            Random rand = new Random();
            int compare1;
            int compare2;

            do
            {
                WriteLine($"{compare1 = rand.Next(-100, -1)} > {compare2 = rand.Next(-100, -1)}: {compare1 > compare2}");
                counter++;
            }
            while (counter < 1);
    }
}
}
