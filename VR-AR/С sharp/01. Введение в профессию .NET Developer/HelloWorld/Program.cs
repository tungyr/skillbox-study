//using System;
using static System.Console;

namespace HelloWorld
{
    class Program
    {
    
        /// <summary>
        /// Если набрать три /// перед функцией, автоматом создается комментарий
        /// </summary>
        /// <param name="args">Здесь пишутся параметры</param>
        static void Main(string[] args) // Это главная функция или точка входа
        {
            // If no "using System;" or "using static System.Console;" on the top you have to write it everywhere:

            //System.Console.WriteLine("Привет, мир!");
            //System.Console.WriteLine("Hello world!");

            //System.Console.ReadKey();

            // Otherwise you can write "using System.Console" on top and go on:
            var a = 28;
            var b = 84.5;
            var с = "example";

            sbyte int8 = 127;
            short int16 = 1;
            int int32 = 0;
            long int64 = -1;

            int hexNumber = 0x7C6;

            float one = 1.1234567890f;
            double two = 1.123456789123456789D;
            decimal three = 1.123456789m;
            string s = "skillbox";
            var result = "result: " + s + " " + с;
            WriteLine(result);
            WriteLine(one);
            WriteLine(two);
            string chicken = "chicken";
            WriteLine(chicken[2]) ;
            WriteLine($"one: {one}");
            WriteLine("Hello world!");
            string string1 = new string('-', 30);
            WriteLine(string1);
            var letter = string1[2];

            
            ReadKey();
            


        }
    }
}

// This is simple comment
 /*
  * This is
  * multi
  * line
  * comment
  */