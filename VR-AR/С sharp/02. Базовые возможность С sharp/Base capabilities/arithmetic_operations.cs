using static System.Console;
using System;

namespace Base_capabilities
{
    class arithmetic_operations
    {
        public static void arithmetic_operations_()
        { //-=ARITHMETIC OPERATIONS=-
            int valA = 2_140_000_000; int valB = 2_140_000_000;
            double valC = (double)valA + (double)valB;

            WriteLine($"valC: {valC}");

        // integer division

            int a = 5;
            int b = 2;
            int c = 5 / 2;
            WriteLine($"с: {c}");

            a = a + b;
            a += b;

            a = 10;

            a++;
            WriteLine($"a++: {a}");

            a--;
            WriteLine($"a-- {a}");

            ++a;
            --a;

            a = 0;
            //will show 0, because priority of WriteLine higher, than ++
            WriteLine(a++);









        }   
        
    }
}
