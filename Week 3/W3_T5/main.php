<?php

class Person {
    public $first_name;
    public $last_name;
    private $age;

    public function __construct($fname, $lname, $age) {
        $this->first_name = $fname;
        $this->last_name = $lname;
        $this->age = $age;
    }

    public function getAge() {
        return $this->age;
    }

    public function ageUp() {
        $this->age += 1;
    }

    public function getFullname() {
        return $this->first_name . " " . $this->last_name;
    }

    public function printFullname() {
        echo $this->first_name . " " . $this->last_name . PHP_EOL;
    }
}

class Main {

    public function __construct() {
        echo "Program starting." . PHP_EOL;
        echo "Creating person..." . PHP_EOL;

        $person = new Person("John", "Doe", 30);

        echo "Person created." . PHP_EOL;

        echo "Name: " . $person->getFullname() . PHP_EOL;
        echo "Age: " . $person->getAge() . PHP_EOL;

        echo "Person has now birthday..." . PHP_EOL;

        $person->ageUp();
        $age = $person->getAge();

        echo "New age: " . $age . PHP_EOL;

        echo "Program ending." . PHP_EOL;
    }
}

// start program
new Main();

?>