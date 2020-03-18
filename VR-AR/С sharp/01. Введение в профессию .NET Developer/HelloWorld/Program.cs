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

            WriteLine("Привет, мир!");
            WriteLine("Hello world!");

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