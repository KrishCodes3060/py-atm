# PyATM Software

## Overview
The PyATM Application is a simple GUI-based program that simulates an ATM system. Users can authenticate with a PIN, perform transactions such as withdrawing and depositing money, and check their account balance. This project is built using Python and `tkinter` for the graphical user interface.

## Features
- **User Authentication**: Securely log in using a 4-digit PIN.
- **Withdraw Funds**: Withdraw money from your account.
- **Deposit Funds**: Deposit money into your account.
- **Check Balance**: View your current account balance.
- **Clear and Cancel**: Clear input fields or cancel ongoing transactions.
- **Instructions**: Access detailed instructions for using the application.

## Installation

### Prerequisites
- Python 3.x

### Install Dependencies
Make sure you have the required libraries installed. You can install them using pip:
```bash
pip install tkinter
```

### Clone the Repository
Clone this repository to your local machine:
```bash
git clone <repository-url>
cd <project-directory>
```

## Usage

### Running the Software
To start the software, run the `main.py` file:
```bash
python main.py
```
Note– Make sure that `main.py` file is in the same directory where the terminal is located.
You can locate terminal by using the following command:
```bash
cd path/to/your/project
```

### Interacting with the software
You can refer to INSTRUCTIONS.md for this

## Configuration

### Data File
The user data and account information are stored in `atm_data.json`. It is located in data/ from the root directory of PyATM. Ensure it follows following format:
```json
{
    "users": {
        "1234": {
            "name": "ABC",
            "balance": 5000.0
        }
    }
}
```

## Troubleshooting
- **Software Does Not Start**: Verify Python installations and ensure required libraries are installed.
- **PIN Authentication Issues**: Confirm that the PIN you are using exists in `atm_data.json`.
- **Transaction Errors**: Ensure the amounts entered are valid and you have sufficient balance for withdrawals.

## Contributing
Contributions are welcome! Please submit pull requests or open issues for any bugs or feature requests.
You can refer to `CONTRIBUTING.md` for more information.

## License
This project is licensed under the custom MIT license.
See the [LICENSE](../LICENSE/LICENSE) file for details.

## Contact
For any questions or support, please contact [krishpandya30062011@gmail.com](https://gmail.com/krishpandya30062011@gmail.com).

Thanks for using PyATM<br>
Krish Pandya,<br>
The developer<br>
