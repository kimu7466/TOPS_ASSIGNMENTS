#include<iostream>
using namespace std;

class person{
    public:
        
    // data member/ attribute
    string name;
    int age;

    // member function/method
    string speak(){
        return "I can speak";
    }
};

int main(){
    person b; // object
    b.name = "birjesh";
    b.age = 27;
    cout<<b.name<<endl<<b.age<<endl;
    cout<<b.speak()<<endl;

    person r; // object
    r.name = "raj";
    r.age = 25;
    cout<<r.name<<endl<<r.age<<endl;
    cout<<r.speak()<<endl;
    return 0;
}


# constructor and destructor 
#include<iostream>
using namespace std;

class person{
    private:
    // data member/ attribute
    string name;
    int age;

    public:
    person(string n, int a){
        name = n;
        age = a;
    }
    // member function/method
    string speak(){
        return "I can speak";
    }

    int display(){
        cout<<"Person information : "<<endl;
        cout<<"Name :"<<name<<endl;
        cout<<"Age : "<<age<<endl;
        cout<<speak()<<endl;
    }

    ~person(){
        cout<<"I am destructor"<<endl;
    }
};

int main(){

    person b("brijesh", 27);
    b.display();
    person r("raj", 25);
    r.display();
    return 0;
}

