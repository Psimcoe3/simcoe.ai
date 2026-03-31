[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPlainText Method (String)

---



|  |
| --- |
| [FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)   [See Also](#seeAlsoToggle) |

Sets the entire text with the given text in a plain text form.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public void SetPlainText( 	string plainText ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPlainText ( _ 	plainText As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPlainText( 	String^ plainText ) ``` |

#### Parameters

plainText
:   Type:  System String    
     The given text in a plain text form.

# Remarks

Any individual formatting present before will be lost after applying this function and the text will have uniform formatting. If the text does not end with a carriage return character ('\r') one will be added. An empty string is allowed. The given text should have no more than 30,000 characters, not counting a terminating carriage return character ('\r'). Newline characters ('\n') are not allowed.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | plainText (excluding a carriage return character ('\r') at the end) has more than 30,000 characters. -or- plainText contains invalid characters such as a newline character. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormattedText Class](79a92343-2342-8325-1b51-f12c4fb05481.htm)

[SetPlainText Overload](cedf3c38-5769-89ea-b785-7eb47623b198.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)