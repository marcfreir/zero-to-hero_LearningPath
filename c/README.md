# <div align="center"> Writing a C Compiler </div>

    * Week 1: Integers

      [return_2.c]
```c
int main()
{
    return 2;
}
```
    Verifying that the compiler works correctly. Compiling a program, running it, and checking its return code:

```bash
$ ./g++ return_2.c # compile the source file shown above
$ ./gcc -m32 return_2.s -o return_2 # assemble it into an executable
$ ./return_2 # run the executable you just compiled
$ echo $? # check the return code; it should be 2
2
```