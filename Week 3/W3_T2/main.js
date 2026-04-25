const Person = require('./person');

class Main {
    constructor() {
        console.log("Program starting.");
        console.log("Creating person...");

        const person = new Person("John", "Doe", 30);

        console.log("Person created.");

        console.log("Name: " + person.getFullname());
        console.log("Age: " + person.getAge());

        console.log("Person has now birthday...");

        person.ageUp();
        let age = person.getAge();

        console.log("New age: " + age);

        console.log("Program ending.");
    }
}

new Main();