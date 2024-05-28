#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

template <typename T>
void sortArray(T arr[], int size) {
    vector<T> vec(arr, arr + size); 
    sort(vec.begin(), vec.end());   
    copy(vec.begin(), vec.end(), arr); 
}

int main() {
    int intArray[] = {5, 2, 9, 1, 5, 6};
    double doubleArray[] = {3.5, 1.2, 9.8, 2.7, 4.0};

    int intArraySize = sizeof(intArray) / sizeof(intArray[0]);
    int doubleArraySize = sizeof(doubleArray) / sizeof(doubleArray[0]);

    cout << "Before sorting intArray: ";
    for (int i = 0; i < intArraySize; i++) {
        cout << intArray[i] << " ";
    }
    cout << endl;

    sortArray(intArray, intArraySize);

    cout << "After sorting intArray: ";
    for (int i = 0; i < intArraySize; i++) {
        cout << intArray[i] << " ";
    }
    cout << endl;

    cout << "Before sorting doubleArray: ";
    for (int i = 0; i < doubleArraySize; i++) {
        cout << doubleArray[i] << " ";
    }
    cout << endl;

    sortArray(doubleArray, doubleArraySize);

    cout << "After sorting doubleArray: ";
    for (int i = 0; i < doubleArraySize; i++) {
        cout << doubleArray[i] << " ";
    }
    cout << endl;

    return 0;
}

