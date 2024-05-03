#include <iostream>
#include <string>

// Base class Person
class Person {
protected:
    std::string name;
    int age;

public:
    // Default constructor
    Person() : name(""), age(0) {}

    // Parameterized constructor to initialize data
    Person(const std::string& _name, int _age) : name(_name), age(_age) {}

    // Member function to read data
    void readData() {
        std::cout << "Enter Name: ";
        std::cin.ignore(); // Clear any previous newline character
        std::getline(std::cin, name);
        std::cout << "Enter Age: ";
        std::cin >> age;
    }

    // Member function to display data
    void displayData() {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Age: " << age << " years" << std::endl;
    }
};

// Derived class Student
class Student : public Person {
protected:
    double percentage;

public:
    // Default constructor
    Student() : percentage(0.0) {}

    // Parameterized constructor to initialize data
    Student(const std::string& _name, int _age, double _percentage)
        : Person(_name, _age), percentage(_percentage) {}

    // Member function to read student-specific data
    void readStudentData() {
        std::cout << "Enter Percentage: ";
        std::cin >> percentage;
    }

    // Member function to display student-specific data
    void displayStudentData() {
        std::cout << "Percentage: " << percentage << "%" << std::endl;
    }
};

// Derived class Teacher
class Teacher : public Person {
protected:
    double salary;

public:
    // Default constructor
    Teacher() : salary(0.0) {}

    // Parameterized constructor to initialize data
    Teacher(const std::string& _name, int _age, double _salary)
        : Person(_name, _age), salary(_salary) {}

    // Member function to read teacher-specific data
    void readTeacherData() {
        std::cout << "Enter Salary: $";
        std::cin >> salary;
    }

    // Member function to display teacher-specific data
    void displayTeacherData() {
        std::cout << "Salary: $" << salary << std::endl;
    }
};

int main() {
    Student student;
    Teacher teacher;

    // Read data for a student
    std::cout << "Enter Student Information:" << std::endl;
    student.readData();
    student.readStudentData();

    // Read data for a teacher
    std::cout << "\nEnter Teacher Information:" << std::endl;
    teacher.readData();
    teacher.readTeacherData();

    // Display student and teacher information
    std::cout << "\nStudent Information:" << std::endl;
    student.displayData();
    student.displayStudentData();

    std::cout << "\nTeacher Information:" << std::endl;
    teacher.displayData();
    teacher.displayTeacherData();

    return 0;
}

