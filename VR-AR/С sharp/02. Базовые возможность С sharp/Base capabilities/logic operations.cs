using static System.Console;
using System;

namespace Base_capabilities
{
    class logic_operations
    {
        public static void logic_operations_()
        {  //-=LOGIC OPERATIONS=-
            WriteLine("-=LOGIC OPERATIONS=-\n");

            bool variable1 = true;
            bool variable2 = false;

            WriteLine("Инверсия");

            Console.WriteLine($"variable1 = {variable1}");
            Console.WriteLine($"!variable1 = {!variable1}\n");

            WriteLine("Коньюкция\n");

            Console.WriteLine($" {true} && {true} = {true && true}");
            Console.WriteLine($" {true} && {false} = {true && false}");
            Console.WriteLine($" {false} && {true} = {false && true}");
            Console.WriteLine($" {false} && {false} = {false && false}");

            WriteLine("\nДизьюнкция\n");

            Console.WriteLine($" {true} || {true} = {true || true}");
            Console.WriteLine($" {true} || {false} = {true || false}");
            Console.WriteLine($" {false} || {true} = {false || true}");
            Console.WriteLine($" {false} || {false} = {false || false}");

            WriteLine("\nРазделительная дизьюнкция\n");

            Console.WriteLine($" {true} ^ {true} = {true ^ true}");
            Console.WriteLine($" {true} ^ {false} = {true ^ false}");
            Console.WriteLine($" {false} ^ {true} = {false ^ true}");
            Console.WriteLine($" {false} ^ {false} = {false ^ false}");

            string s = "C#";
            bool flag = 28 != 90 && s != "C#"; 
            Console.WriteLine($"\nflag = {flag}");
        }
    }
}
