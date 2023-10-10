#include <iostream>
#include <vector>
#include <algorithm>

// Template function to sort an array of any data type
template <typename T>
void sortArray(T arr[], int size) {
    std::vector<T> vec(arr, arr + size); // Convert the array to a vector
    std::sort(vec.begin(), vec.end());   // Sort the vector
    std::copy(vec.begin(), vec.end(), arr); // Copy the sorted elements back to the array
}

int main() {
    int intArray[] = {5, 2, 9, 1, 5, 6};
    double doubleArray[] = {3.5, 1.2, 9.8, 2.7, 4.0};

    int intArraySize = sizeof(intArray) / sizeof(intArray[0]);
    int doubleArraySize = sizeof(doubleArray) / sizeof(doubleArray[0]);

    std::cout << "Before sorting intArray: ";
    for (int i = 0; i < intArraySize; i++) {
        std::cout << intArray[i] << " ";
    }
    std::cout << std::endl;

    // Sort intArray using the template function
    sortArray(intArray, intArraySize);

    std::cout << "After sorting intArray: ";
    for (int i = 0; i < intArraySize; i++) {
        std::cout << intArray[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "Before sorting doubleArray: ";
    for (int i = 0; i < doubleArraySize; i++) {
        std::cout << doubleArray[i] << " ";
    }
    std::cout << std::endl;

    // Sort doubleArray using the template function
    sortArray(doubleArray, doubleArraySize);

    std::cout << "After sorting doubleArray: ";
    for (int i = 0; i < doubleArraySize; i++) {
        std::cout << doubleArray[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}

