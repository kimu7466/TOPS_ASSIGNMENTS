#include <iostream>
#include <string>

using namespace std; 

class LectureDetails {
private:
    string lecturerName;
    string subjectName;
    string courseName;
    int numLectures;

public:
    LectureDetails() : numLectures(0) {}

    void assignInitialValues(const string& lecturer, const string& subject,
                             const string& course, int lectures) {
        lecturerName = lecturer;
        subjectName = subject;
        courseName = course;
        numLectures = lectures;
    }

    void addLectureDetails() {
        cout << "Enter Lecture Details:" << endl;
        cout << "Enter Lecturer's Name: ";
        cin >> lecturerName;
        cout << "Enter Subject Name: ";
        cin >> subjectName;
        cout << "Enter Course Name: ";
        cin >> courseName;
        cout << "Enter Number of Lectures: ";
        cin >> numLectures;
    }

    void displayDetails() {
        cout << "\nLecturer's Name: " << lecturerName << endl;
        cout << "Subject Name: " << subjectName << endl;
        cout << "Course Name: " << courseName << endl;
        cout << "Number of Lectures: " << numLectures << endl;
    }
};

int main() {
    LectureDetails lecture1, lecture2, lecture3, lecture4, lecture5;

    lecture1.addLectureDetails();
    lecture2.addLectureDetails();
    lecture3.addLectureDetails();
    lecture4.addLectureDetails();
    lecture5.addLectureDetails();

    cout << "\nLecture Details:" << endl;
    lecture1.displayDetails();
    lecture2.displayDetails();
    lecture3.displayDetails();
    lecture4.displayDetails();
    lecture5.displayDetails();

    return 0;
}

