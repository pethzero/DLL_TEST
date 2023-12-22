# PROJECT
EXAMPLEDLL

# TIHS CODE C++
extern "C" __declspec(dllexport) int add(int a, int b) {
    return a + b;
}

# TERMINAL 
cd D:\PROJECT\DLL\

cl /LD main.cpp