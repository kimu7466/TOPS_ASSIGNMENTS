#include <iostream>
#include <string>

// Base class Students
class Students {
protected:
    int rollNumber;

public:
    // Constructor to initialize roll number
    Students(int roll) : rollNumber(roll) {}

    // Member function to display roll number
    void displayRollNumber() {
        std::cout << "Roll Number: " << rollNumber << std::endl;
    }
};

// Derived class Test from Students
class Test : public Students {
protected:
    int subject1Marks;
    int subject2Marks;

public:
    // Constructor to initialize subject marks
    Test(int roll, int marks1, int marks2) : Students(roll), subject1Marks(marks1), subject2Marks(marks2) {}

    // Member function to display test marks
    void displayTestMarks() {
        std::cout << "Subject 1 Marks: " << subject1Marks << std::endl;
        std::cout << "Subject 2 Marks: " << subject2Marks << std::endl;
    }
};

// Derived class Result from Test
class Result : public Test {
public:
    // Constructor to initialize roll number and subject marks
    Result(int roll, int marks1, int marks2) : Test(roll, marks1, marks2) {}

    // Member function to calculate and display total marks
    void displayTotalMarks() {
        int totalMarks = subject1Marks + subject2Marks;
        std::cout << "Total Marks: " << totalMarks << std::endl;
    }
};

int main() {
    // Create a Result object with roll number and subject marks
    Result studentResult(101, 85, 92);

    // Display roll number, test marks, and total marks
    std::cout << "Student Information:" << std::endl;
    studentResult.displayRollNumber();
    studentResult.displayTestMarks();
    studentResult.displayTotalMarks();

    return 0;
}

