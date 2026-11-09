var myDirectories = Directory.GetDirectories(@"C:\");
foreach (var dir in myDirectories)
{
    Console.WriteLine(dir);
}