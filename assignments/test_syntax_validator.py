import unittest
import syntax_validator

class test_syntax_validator(unittest.TestCase):

    def test_is_valid_username_returns_true_given_valid_input_1(self):
        self.assertTrue(syntax_validator.is_valid_username('Abcdefg1'))#exactly 8 letters with first capital and atleast one digit
        
    def test_is_valid_username_returns_true_given_valid_input_2(self):
        self.assertTrue(syntax_validator.is_valid_username('Abcdefg123N'))# more than 8 but less than 12 charcters 
        
    def test_is_valid_username_returns_true_given_valid_input_3(self):
        self.assertTrue(syntax_validator.is_valid_username('Abcdef25ghij'))#exactly 12 characters 
        
    def test_is_valid_username_returns_true_given_valid_input_4(self):
        self.assertTrue(syntax_validator.is_valid_username('ABCDEFGHI14'))#All capital letters and digits
        
    def test_is_valid_username_returns_true_given_valid_input_5(self):
        self.assertTrue(syntax_validator.is_valid_username('A12345614'))#capital letter and digit
        #Bug found: should return TRUE, but returning FALSE
    
    
        
    def test_is_valid_username_returns_false_given_invalid_input_1(self):
        self.assertFalse(syntax_validator.is_valid_username('Abcd234'))#less than 8 characters(7 characters)
        
    def test_is_valid_username_returns_false_given_invalid_input_2(self):
        self.assertFalse(syntax_validator.is_valid_username('Abcdefghijkl2'))# more than characters 12, (13 characters)
    
        
    def test_is_valid_username_returns_false_given_invalid_input_3(self):
        self.assertFalse(syntax_validator.is_valid_username('abCdefg12'))#first letter is not capital  
        
    def test_is_valid_username_returns_false_given_invalid_input_4(self):
        self.assertFalse(syntax_validator.is_valid_username('123456789'))# first letter must be capital letter
        
        
    def test_is_valid_username_returns_false_given_invalid_input_5(self):
        self.assertFalse(syntax_validator.is_valid_username('@Abcdefghi1'))#First letter must be capital ,not any special character should be included
        
        
    def test_is_valid_username_returns_false_given_invalid_input_6(self):
        self.assertFalse(syntax_validator.is_valid_username('Abcdefghj'))#atleast one digit is required 
        
        
    def test_is_valid_username_returns_false_given_invalid_input_7(self):
        self.assertFalse(syntax_validator.is_valid_username(''))#empty string
        
        
    def test_is_valid_username_returns_false_given_invalid_input_8(self):
        self.assertFalse(syntax_validator.is_valid_username('Abcdef fg1'))#space is not allowed
        
    def test_is_valid_username_returns_false_given_invalid_input_9(self):  
        self.assertFalse(syntax_validator.is_valid_username('Abcd_efgkl12'))#special character is not allowed
        
    
   
        
    def test_is_valid_us_zip_code_returns_true_given_valid_input_1(self):
        self.assertTrue(syntax_validator.is_valid_us_zip_code('12345'))#exactly 5 digits
        
    def test_is_valid_us_zip_code_returns_true_given_valid_input_2(self):
        self.assertTrue(syntax_validator.is_valid_us_zip_code('12345-1234'))#exactly 5 - 4 digits
        
        
    

    def test_is_valid_us_zip_code_returns_false_given_invalid_input_1(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('1234'))#less than 5 digits
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_2(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('123456'))#more than  5 digits
        #Bug Foung: should return FALSE, but returning  TRUE
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_3(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('1234-1234'))# less than 5 digits (first part)
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_4(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('123456-1234'))# more than 5 digits (first part)
        #Bug Foung: should return FALSE, but returning  TRUE
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_5(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-123'))# less than 4 digits (second part)
        #Bug Foung: should return FALSE, but returning  TRUE
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_6(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-12345'))# more than 4 digits  in second digit
        #Bug Foung: should return FALSE, but returning  TRUE
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_7(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('1 2 345'))#space is not allowed
        
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_8(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-1 2 34'))#space is not allowed 
        #Bug Foung: should return FALSE, but returning  TRUE
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_9(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('1A234'))#letters are not allowed
        
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_10(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-1A23'))#letters are not allowed  
        #Bug Foung: should return FALSE, but returning  TRUE
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_11(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('1234.5'))#special characters are not allowed
        
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_12(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-123.4'))#special characters are not allowed  
        #Bug Foung: should return FALSE, but returning  TRUE
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_13(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code(''))# empty string
        
    def test_is_valid_us_zip_code_returns_false_given_invalid_input_14(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('12345-'))# empty string(second part)
        #Bug Foung: should return FALSE, but returning  TRUE

   

