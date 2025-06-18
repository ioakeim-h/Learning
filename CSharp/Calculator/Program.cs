// Basic calculator

Console.WriteLine("Input the first number:");
var firstInput = Console.ReadLine();
bool isValidFirstInput = int.TryParse(firstInput, out int firstNumber);

Console.WriteLine("Input the second number:");
var secondInput = Console.ReadLine();
bool isValidSecondInput = int.TryParse(secondInput, out int secondNumber);

if (!isValidFirstInput || !isValidSecondInput)
    Console.WriteLine("Calculations cannot occur on non-integer values.");
else
{
    // Choose an option
    Console.WriteLine("What do you want to do?");
    Console.WriteLine("[A]dd numbers");
    Console.WriteLine("[S]ubstract number");
    Console.WriteLine("[M]ultiply numbers");

    var option = Console.ReadLine();
    option = option.ToUpper();
    bool isAnOption = ValidateOption(option);

    if (!isAnOption)
        Console.WriteLine("Invalid option.");
    else
    {
        if (option == "A")
            Console.WriteLine($"{firstNumber} + {secondNumber} = {firstNumber + secondNumber}");
        else if (option == "S")
            Console.WriteLine($"{firstNumber} - {secondNumber} = {firstNumber - secondNumber}");
        else
            Console.WriteLine($"{firstNumber} * {secondNumber} = {firstNumber * secondNumber}");
    }
}

static bool ValidateOption(string option)
{
    if (option != "A" && option != "S" && option != "M")
        return false;
    return true;
}

Console.ReadKey();






