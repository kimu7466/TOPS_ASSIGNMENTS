#include <iostream>
#include <vector>
using namespace std;

class Matrix {
    private:
        vector<int> data;  

    public:
        
        Matrix(const vector<int>& input) : data(input) {}        
        Matrix operator+(const Matrix& other) const {
            if (data.size() != other.data.size()) {
                cerr << "Matrix sizes are not compatible for addition." << endl;
                return Matrix(vector<int>());
            }

            vector<int> resultData;
            resultData.reserve(data.size());

            for (size_t i = 0; i < data.size(); i++) {
                resultData.push_back(data[i] + other.data[i]);
            }
            return Matrix(resultData);
        }
        
        void display() const {
            for (int value : data) {
                cout << value << " ";
            }
            cout << endl;
        }
};

int main() {
    
    vector<int> matrix1Data = {1, 2, 3, 4, 5};
    
    vector<int> matrix2Data = {6, 7, 8, 9, 10};

    Matrix matrix1(matrix1Data);
    Matrix matrix2(matrix2Data);
    
    Matrix result = matrix1 + matrix2;
    
    cout << "Matrix 1:" << endl;
    matrix1.display();

    cout << "Matrix 2:" << endl;
    matrix2.display();

    cout << "Result of Matrix Addition:" << endl;
    result.display();

    return 0;
}

