class Person {
    public first_name: string;
    public last_name: string;
    private age: number;

    constructor(fname: string, lname: string, age: number) {
        this.first_name = fname;
        this.last_name = lname;
        this.age = age;
    }

    public getAge(): number {
        return this.age;
    }

    public ageUp(): void {
        this.age += 1;
    }

    public getFullname(): string {
        return this.first_name + " " + this.last_name;
    }

    public printFullname(): void {
        console.log(this.first_name + " " + this.last_name);
    }
}

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
        const age: number = person.getAge();

        console.log("New age: " + age);

        console.log("Program ending.");
    }
}

// start program
new Main();