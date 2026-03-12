#include <iostream>
using namespace std;

class Employee {
public:
    int roll;
    int salary;

    void input(int index) {
        cout << "Enter Roll of Employee [" << index << "]: ";
        cin >> roll;
        cout << "Enter Salary of Employee [" << index << "]: ";
        cin >> salary;
    }

    void display(int index) const {
        cout << "[" << index << "] Roll No: " << roll
             << " Salary: " << salary << endl;
    }
};

int main() {
    int n;
    cout << "Enter the number of employees: ";
    cin >> n;
    Employee emp[100];
    for (int i = 0; i < n; i++) {
        emp[i].input(i + 1);
    }

    int choice;
    do {
        cout << "\nMenu:\n";
        cout << "1. Display all employees\n";
        cout << "2. Show employees with the highest salary\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            cout << "\nEmployee Data:\n";
            for (int i = 0; i < n; i++) {
                emp[i].display(i + 1);
            }
        }
        else if (choice == 2) {
            int maxSalary = emp[0].salary;

            for (int i = 1; i < n; i++) {
                if (emp[i].salary > maxSalary) {
                    maxSalary = emp[i].salary;
                }
            }

            cout << "\nEmployees with the highest salary (" 
                 << maxSalary << "):\n";

            for (int i = 0; i < n; i++) {
                if (emp[i].salary == maxSalary) {
                    cout << "Roll No: " << emp[i].roll
                         << " Salary: " << emp[i].salary << endl;
                }
            }
        }
        else if (choice == 3) {
            cout << "Exiting program.\n";
        }
        else {
            cout << "Invalid choice!\n";
        }

    } while (choice != 3);

    return 0;
}