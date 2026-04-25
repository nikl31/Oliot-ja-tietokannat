class Person {
    constructor(fname, lname, age) {
        this.first_name = fname;
        this.last_name = lname;
        this.#age = age;
    }

    #age;

    getAge() {
        return this.#age;
    }

    ageUp() {
        this.#age += 1;
    }

    getFullname() {
        return this.first_name + " " + this.last_name;
    }

    printFullname() {
        console.log(this.first_name + " " + this.last_name);
    }
}

module.exports = Person;