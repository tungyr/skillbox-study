using static System.Console;
using System;

namespace Base_capabilities
{
    class variables
    {
        public static void variables_()
        {  //-=VARIABLES=-
            WriteLine("-=VARIABLES=-\n");

            WriteLine("Hello World!");

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
            WriteLine(chicken[2]);
            WriteLine($"one: {one}");
            string string1 = new string('-', 30);
            WriteLine(string1);
            var letter = string1[2];
        }
    }
}
