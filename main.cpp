#include <iostream>
#include <Windows.h>

extern "C" __declspec(dllexport) int add(int a, int b) {
    return a + b;
}
