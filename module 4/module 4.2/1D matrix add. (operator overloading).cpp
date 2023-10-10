//this programm is working in online compiler but not working in dev c++
#include <iostream>
#include <vector>

class Matrix {
private:
    std::vector<int> data;  // Use a vector to store the matrix data

public:
    // Constructor to initialize the matrix with data
    Matrix(const std::vector<int>& input) : data(input) {}

    // Overload the '+' operator for matrix addition
    Matrix operator+(const Matrix& other) const {
        if (data.size() != other.data.size()) {
            std::cerr << "Matrix sizes are not compatible for addition." << std::endl;
            return Matrix(std::vector<int>());
        }

        std::vector<int> resultData;
        resultData.reserve(data.size());

        for (size_t i = 0; i < data.size(); i++) {
            resultData.push_back(data[i] + other.data[i]);
        }

        return Matrix(resultData);
    }

    // Member function to display the matrix
    void display() const {
        for (int value : data) {
            std::cout << value << " ";
        }
        std::cout << std::endl;
    }
};

int main() {
    // Input values for the first matrix
    std::vector<int> matrix1Data = {1, 2, 3, 4, 5};

    // Input values for the second matrix
    std::vector<int> matrix2Data = {6, 7, 8, 9, 10};

    // Create Matrix objects from the input data
    Matrix matrix1(matrix1Data);
    Matrix matrix2(matrix2Data);

    // Perform matrix addition using operator overloading
    Matrix result = matrix1 + matrix2;

    // Display the matrices and the result
    std::cout << "Matrix 1:" << std::endl;
    matrix1.display();

    std::cout << "Matrix 2:" << std::endl;
    matrix2.display();

    std::cout << "Result of Matrix Addition:" << std::endl;
    result.display();

    return 0;
}

