const char output[] __attribute__((section("__TEXT,__text"))) = ""; //put shellcode here

typedef int (*funcPtr)();

int main(int argc, char **argv)
{
    funcPtr ret = (funcPtr) output;
    (*ret)();

    return 0;
}
