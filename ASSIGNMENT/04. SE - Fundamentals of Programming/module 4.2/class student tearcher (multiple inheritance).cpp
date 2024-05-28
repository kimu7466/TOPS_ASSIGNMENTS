#include <iostream>
#include <string>
using namespace std;

class Person {
protected:
    string name;
    int age;

public:
    Person() : name(""), age(0) {}
    
    Person(const string& _name, int _age) : name(_name), age(_age) {}    
    
    void readData() {
        cout << "Enter Name: ";
        cin.ignore();  
        getline(cin, name);
        cout << "Enter Age: ";
        cin >> age;
    }
    
    void displayData() const {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << " years" << endl;
    }
};

class Student : public Person {
protected:
    double percentage;

public:    
    Student() : percentage(0.0) {}

    Student(const string& _name, int _age, double _percentage)
        : Person(_name, _age), percentage(_percentage) {}
    
    void readStudentData() {
        cout << "Enter Percentage: ";
        cin >> percentage;
    }
    
    void displayStudentData() const {
        cout << "Percentage: " << percentage << "%" << endl;
    }
};

class Teacher : public Person {
protected:
    double salary;

public:    
    Teacher() : salary(0.0) {}

    Teacher(const string& _name, int _age, double _salary)
        : Person(_name, _age), salary(_salary) {}
    
    void readTeacherData() {
        cout << "Enter Salary: $";
        cin >> salary;
    }
    
    void displayTeacherData() const {
        cout << "Salary: $" << salary << endl;
    }
};

int main() {
    Student student;
    Teacher teacher;
        
    cout << "Enter Student Information:" << endl;
    student.readData();
    student.readStudentData();
    
    cout << "\nEnter Teacher Information:" << endl;
    teacher.readData();
    teacher.readTeacherData();
    
    cout << "\nStudent Information:" << endl;
    student.displayData();
    student.displayStudentData();

    cout << "\nTeacher Information:" << endl;
    teacher.displayData();
    teacher.displayTeacherData();

    return 0;
}
