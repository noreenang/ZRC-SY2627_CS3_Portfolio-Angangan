# Q2 Computer Science - Encapsulation Activities

## Activity 1: Access Modifiers & Attribute Declarations

| # | Situation / Class & Attribute | Access Level | Python Statement inside `__init__()` |
|---|---|---|---|
| **1** | A `GameCharacter` class has a `username` that can be displayed and accessed by anyone. | **Public** | `self.username = username` |
| **2** | A `BankAccount` class has a `balance` that should **NOT** be accessed directly outside the class. | **Private** | `self.__balance = balance` |
| **3** | A `Vehicle` class has an `engineCode` that should only be accessed within the class and its subclasses. | **Protected** | `self._engineCode = engineCode` |
| **4** | A `Student` class has a `schoolName` that is safe for everyone to view and modify. | **Public** | `self.schoolName = schoolName` |
| **5** | A `VotingSystem` class has a `voterID` that must be hidden for security reasons. | **Private** | `self.__voterID = voterID` |

