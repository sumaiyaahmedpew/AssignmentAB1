
### **Problem 1 – Inventory Management System**

Building a small shop’s inventory program.

* Store product data as a **dictionary** where `key = product_id` (int) and `value = tuple (name, price, quantity)`.
* Add at least 5 products manually.
* Implement the following features:

  1. **Add Product** (Check if product\_id already exists, if yes → reject)
  2. **Update Quantity** (Add or reduce quantity)
  3. **Find Products in Price Range** (Using list comprehension)
  4. **Sort Products by Price** (Ascending)
* Print final inventory.


### **Problem 2 – Student Result Processing (Advanced)**

Given a list:

```python
data = [
    ("Sumaiya", 101, [80, 75, 90]),
    ("Ahmed", 102, [60, 70, 65]),
    ("Pew", 103, [90, 95, 92]),
    ("Rew", 104, [55, 48, 60])
]
```

* Convert into a dictionary:
  `key = roll`, `value = {"name":..., "marks":..., "total":..., "avg":..., "grade":...}`
* Grade system:

  * avg ≥ 85 → A
  * avg ≥ 70 → B
  * avg ≥ 50 → C
  * else → F
* Find top 3 students by total marks.
* Find students who failed (`grade = F`).


### **Problem 3 – Sports Tournament Tracker**

* Teams are stored in a **list of dictionaries**, each having: `{"name":..., "played":..., "won":..., "lost":..., "points":...}`
* After each match, update stats:

  * Winning team: `played += 1`, `won += 1`, `points += 3`
  * Losing team: `played += 1`, `lost += 1`
* Allow user to enter match results until they type `"stop"`.
* Display leaderboard sorted by points.


### **Problem 4 – Employee Salary Analyzer**

* Input a dictionary where `key = employee_name`, `value = monthly_salary`.
* Calculate yearly salary for each employee and store in a **tuple** along with name.
* Find:

  1. Employee with highest yearly salary
  2. Average yearly salary
  3. Employees earning above average


### **Problem 5 – Set Operations in Social Media App**

* Users follow each other. Given:

```python
followers_A = {"Rakhi", "Ramisa", "Sumaiya", "Liza"}
followers_B = {"Ramisa", "Sumaiya", "Jui"}
```

* Find:

  1. Common followers
  2. Followers unique to A
  3. Followers unique to B
  4. All followers combined (without duplicates)


---

### **Problem 6 – Library Catalog Search**

* Store books as a list of tuples: `(book_id, title, author, year)`.
* Implement:

  1. Search by author name (case-insensitive)
  2. Search by year range
  3. Sort by title alphabetically



### **Problem 7 – Number Cruncher (Operators + Logic)**

* Ask user for two integers.
* Perform and print results for:

  * Addition, Subtraction, Multiplication, Division, Modulus, Power
  * `>` `<` `==` comparisons
  * Bitwise AND, OR, XOR
  * Check if numbers are even or odd using bitwise operator.


### **Problem 8 – Data Cleanup Tool**

Given a list of mixed data types:

```python
items = [1, "apple", 3.5, "banana", True, 42, "cherry", 2.7]
```

* Separate into **lists**: integers, floats, strings, booleans.
* Remove duplicates using sets (where applicable).
* Print counts of each type.


### **Problem 9 – Tuple Performance Test**

* Create a list and a tuple of 1 million integers.
* Measure iteration speed over each (5 runs) and print average time.
* Explain why tuple is slightly faster.


### **Problem 10 – Mini Project: Contact Book CLI**

* Store contacts as a dictionary where `key = phone_number` (string), `value = {"name":..., "email":..., "address":...}`
* Menu options:

  1. Add contact (no duplicate phone)
  2. View all contacts
  3. Search by name
  4. Delete by phone
  5. Exit
* Use while loop for menu until exit.

### **Problem 11 – Scientific Calculator with Modes**

A **menu-driven scientific calculator** with two modes:

1. **Basic Mode**

   * Perform arithmetic operations (`+ - * / // % **`)
   * Handle divide by zero
   * Option to **swap numbers** before calculation

2. **Advanced Mode**

   * **Number System Conversion**: Decimal → Binary, Octal, Hex; Binary → Decimal
   * **Bitwise Calculator**: AND, OR, XOR, NOT (\~)
   * **Geometry Calculator**:

     * Circle area & circumference
     * Square root of area
     * Trigonometric functions (sin, cos, tan)


###  **Problem 12 – Student Report Card Generator**

A program to generate a **student report card**:

* Input: name, roll number, marks in 5 subjects
* Calculates:

  * Total and average marks
  * Grade (A+, A, B, C, D, Fail) using if-elif-else
  * Even/Odd roll check using bitwise operator
* Output Options:

  * **Normal Mode** → Print directly
  * **Encoded Mode** → Roll converted to binary, Grade shown as ASCII codes
* Bonus Feature: **Swap roll and average marks** using Python multiple assignment


### **Problem 13 – Secure Login & Utility Program**

A **secure login system** followed by a **multi-utility program**:

* **Login System**

  * Username/Password authentication
  * Maximum 3 attempts allowed

* **Utility Menu**

  1. Number System Converter (Decimal ↔ Binary/Octal/Hex)
  2. Bitwise Operations (AND, OR, XOR, NOT)
  3. Trigonometry Calculator (sin, cos, tan)
  4. Grade Calculator (marks → grade + even/odd check)
  5. Exit

## Topics Covered Today

* Variables & Multiple Assignment (Swapping)
* User Input & Command-Line Interaction
* If-Elif-Else Conditionals
* Number System Conversion (binary, octal, hex)
* Bitwise Operators (AND, OR, XOR, NOT)
* Math Module (`math.pi`, `math.sqrt`, `math.radians`, `math.sin`, etc.)
* Loops & Menu-Driven Programs
* Login Authentication Logic



