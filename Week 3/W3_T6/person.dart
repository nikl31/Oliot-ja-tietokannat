class Person {
  String first_name;
  String last_name;
  int _age;

  Person(String fname, String lname, int age)
      : first_name = fname,
        last_name = lname,
        _age = age;

  int getAge() {
    return _age;
  }

  void ageUp() {
    _age += 1;
  }

  String getFullname() {
    return first_name + " " + last_name;
  }

  void printFullname() {
    print(first_name + " " + last_name);
  }
}