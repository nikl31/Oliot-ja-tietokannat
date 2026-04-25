#ifndef PERSON_H
#define PERSON_H

#include <string>
#include <sstream>

class Person {
public:
    std::string first_name;
    std::string last_name;
    int age;

    Person(std::string fname, std::string lname, int age) {
        this->first_name = fname;
        this->last_name = lname;
        this->age = age;
    }

    int getAge() {
        return this->age;
    }

    void ageUp() {
        this->age += 1;
    }

    std::string getFullname() {
        std::ostringstream oss;
        oss << this->first_name << " " << this->last_name;
        return oss.str();
    }

    void printFullname() {
        std::cout << this->first_name << " " << this->last_name << std::endl;
    }
};

#endif