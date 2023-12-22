import ctypes

# โหลด DLL
example_dll = ctypes.CDLL('./EXAMPLEDLL.dll')
# example_dll = ctypes.CDLL('./main.dll')
# เรียกใช้ฟังก์ชัน Add
result = example_dll.add(3, 4)

# extern "C" __declspec(dllexport) int add(int a, int b) {
#     return a + b;
# }
print(f'Result from DLL: {result}')