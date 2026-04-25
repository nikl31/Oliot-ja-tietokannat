import 'person.dart';

void main() {
  print("Program starting.");
  print("Creating person...");

  var person = Person("John", "Doe", 30);

  print("Person created.");

  print("Name: " + person.getFullname());
  print("Age: " + person.getAge().toString());

  print("Person has now birthday...");

  person.ageUp();
  var age = person.getAge();

  print("New age: " + age.toString());

  print("Program ending.");
}