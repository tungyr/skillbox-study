using static System.Console;
using System;

namespace Base_capabilities
{
    class formatted_output
    {
        public static void formatted_output_()
        {
            //-=FORMATTED OUTPUT=-

            string name = "Victor";
            string secondg_name = "Belkov";
            byte age = 34;
            ulong year_of_birth = 1985;

            WriteLine("Name: {0}; Family name: {1}; Age: {2}; Year of birth: {3};",
                name,
                secondg_name,
                age,
                year_of_birth);

            string pattern = "Name: {0}; \nFamily name: {1}; \nAge: {2}; \nYear of birth: {3};";
            WriteLine(pattern,
                        name,
                        secondg_name,
                        age,
                        year_of_birth);

            string fName = "Anna";
            string lName = "Lovelace";
            byte anna_age = 37;
            ulong anna_year = 1993;

            WriteLine(pattern,
                fName,
                lName,
                anna_age,
                anna_year
                );

            WriteLine($"\n Victor's Credentials \n" +
                $"Name: {name}; Family name: {secondg_name}; Age: {age}; Year of birth: {year_of_birth}");

            int hundred = 100;
            int two_hundred = 200;
            WriteLine($"{hundred} + {two_hundred} = {300}");

            string name1 = "Anna", last_name1 = "Lebedeva";
            string name2 = "Maria", last_name2 = "Vinokurova";
            string name3 = "Alex", last_name3 = "Popova";
            string name4 = "Polina", last_name4 = "Kalinina";
            string name5 = "Anastasia", last_name5 = "Ivanova";

            WriteLine($"{name1,10} {last_name1,15}");
            WriteLine($"{name2,10} {last_name2,15}");
            WriteLine($"{name3,10} {last_name3,15}");
            WriteLine($"{name4,10} {last_name4,15}");
            WriteLine($"{name5,10} {last_name5,15}");


            string separator = new string('-', 60);
            WriteLine('\n' + separator + '\n');


            double d = 123456.654321;
            WriteLine("d: " + d);

            string dFormatted = d.ToString("#.###");
            WriteLine("dFormatted: " + dFormatted);

            WriteLine("dFormatted separated: " + d.ToString("## ## ##.## ## ## ## ##"));

            WriteLine("dFormatted separated: " + "{0:000 000 000.000 000 000}", d);

            string separator2 = new string('-', 60);
            WriteLine('\n' + separator + '\n');

            var date = new DateTime(2025, 09, 28, 01, 30, 59);
            WriteLine(date);

            WriteLine($"{date:HH:mm}");
            WriteLine($"{date:yyyy-MM-dd}");
            WriteLine($"{date:yy.MM.dd}");
            WriteLine($"{date:dd.MM.yyy}");
        }
    }
}
