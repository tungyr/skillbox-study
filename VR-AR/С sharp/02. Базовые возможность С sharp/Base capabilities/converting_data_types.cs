using static System.Console;
using System;

namespace Base_capabilities
{
    class converting_data_types
    {
        public static void converting_data_types_()
        { //-=CONVERTING DATA TYPES=-
          WriteLine("-=CONVERTING DATA TYPES=-\n");
            char c = 'a';
            int d = c;
            WriteLine($"int of d char: {d}\n");

            int i = 330;
            byte j = (byte)i;
            WriteLine($"int i = {i} -> byte j => {j}\n");

            double db = 1.2;
            byte bt = (byte)d;
            WriteLine($"double db = {db} -> byte bt => {bt}\n");

            int h = (int)db;
            WriteLine($"double db = {db} -> int h => {h}\n");

            string input_str = "2029";
            int intValue = int.Parse(input_str);
            WriteLine($"string input_str {input_str} -> " +
                $"int intValue => {intValue}\n");

            //will be error:
            //byte byteValue = byte.Parse(input_str);

            int intValue2 = Convert.ToInt32(input_str);
           
            long l = Convert.ToInt64(input_str);
            WriteLine($"string input_str {input_str} -> " +
               $"long l => {l}\n");




        }   
        
    }
}
