This application allows users to input an EAN-13 number and verify its validity.
The user enters the number in a text field and clicks the “Check EAN-13” button.
The application calculates the checksum using the EAN-13 algorithm and displays whether the number is correct or not.

Formula: The checksum is calculated by summing the digits of the EAN-13 number, with every second digit multiplied by 3. The check digit is the smallest number that, when added to this sum, results in a multiple of 10. The formula is:
Check_Digit = (10 − (Summod10)) mod 10
