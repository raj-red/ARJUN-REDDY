class parent
{
    int a=10+3;
    void display()
    {
        system.out.println("parent class");
    }
}
class child1
{
    int b=20+3;
    void show()
    {
        system.out.println("child class 1");
    }
}
class child2
{
    int d=30+3;
    void frog()
    {
        system.out.println("child class 2")
    }
}
class rajesh
{
    public static void main(string arg[])
    {
    child2 c=new child2();
    system.out.println(c.child2);
    c.frog();
    c.display();
    child1 p=new child1();
    system.out.println(p.child1);
    p.show();
    p.display();
    }
}