using System.Linq;

char optionSelected;
char[] validOptions = { 'S', 'A', 'R', 'E' }; // not needed - handled by switch
List<string> tasksTODO = new List<string>();

Console.WriteLine("Hello!");

do 
{
    Console.WriteLine("\nWhat do you want to do?");
    Console.WriteLine("[S]ee all TODOs");
    Console.WriteLine("[A]dd a TODO");
    Console.WriteLine("[R]emove a TODO");
    Console.WriteLine("[E]xit");

    // Validate choice
    bool isChar = char.TryParse(Console.ReadLine(), out optionSelected);
    optionSelected = Char.ToUpper(optionSelected);

    switch (optionSelected)
    {
        case 'S':
            bool success = printTasks(tasksTODO);
            break;

        case 'A':
            addToDo(tasksTODO);
            break;

        case 'R':
            removeToDO(tasksTODO);
            break;
                
        case 'E':
            Environment.Exit(0);
            break;
        
        default:
            Console.WriteLine("Incorrect input");
            break;
    }

} while (optionSelected != 'E'); // not needed - handled by switch


static bool printTasks(List<string> tasksTODO)
{
    if (tasksTODO.Count == 0)
        {
            Console.WriteLine("No TODOs have been added yet.");
            return false;
        }
        
    // See all TODOs in order
    for (int i = 0; i < tasksTODO.Count; i++)
        Console.WriteLine($"{i+1}. {tasksTODO[i]}.");
    return true;
}   


static void addToDo(List<string> tasksTODO)
{
    while (true)
    {
        Console.WriteLine("Enter the TODO description:");
        var newTask = Console.ReadLine();

        if (string.IsNullOrEmpty(newTask))
            Console.WriteLine("The description cannot be empty.");
        else if (tasksTODO.Contains(newTask))
            Console.WriteLine("The description must be unique.");
        else
        {
            tasksTODO.Add(newTask);
            Console.WriteLine($"TODO successfully added: {newTask}");
            break;
        }
    }
}


static void removeToDO(List<string> tasksTODO)
{
    int selectedIndex;

    // Get valid indices starting from 1
    List<int> validIndices = new List<int>();
    for (int i = 1; i <= tasksTODO.Count; i++)
        validIndices.Add(i);

    // Choose item to remove
    while (true)
    {
        Console.WriteLine("Select the index of the TODO you want to remove:");
        bool success = printTasks(tasksTODO);

        if (!success)
            break;
        
        bool isInt = int.TryParse(Console.ReadLine(), out selectedIndex);
        if (selectedIndex == 0)
            Console.WriteLine("Selected index cannot be empty");
        else if (!validIndices.Contains(selectedIndex))
            Console.WriteLine("The given index is not valid.");
        else
            {
                // List indices displayed as +1
                Console.WriteLine($"TODO removed: {tasksTODO[selectedIndex-1]}");
                tasksTODO.RemoveAt(selectedIndex-1);
                break;
            }
    }
}









