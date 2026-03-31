[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NumericRevisionSettings Constructor (Int32, String, String)

---



|  |
| --- |
| [NumericRevisionSettings Class](3de46f00-fbf9-0c6b-b7fa-5d33052d0091.htm)   [See Also](#seeAlsoToggle) |

Constructs a NumericRevisionSettings object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public NumericRevisionSettings( 	int startNumber, 	string prefix, 	string suffix ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	startNumber As Integer, _ 	prefix As String, _ 	suffix As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: NumericRevisionSettings( 	int startNumber,  	String^ prefix,  	String^ suffix ) ``` |

#### Parameters

startNumber
:   Type:  System Int32    
     The start number for the sequence.

prefix
:   Type:  System String    
     The prefix string for each revision number in the sequence.

suffix
:   Type:  System String    
     The suffix string for each revision number in the sequence.

# Remarks

The starting number parameter accepts any non-negative integer, and the prefix and suffix strings are allowed to be empty.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for startNumber is negative. |

# See Also

[NumericRevisionSettings Class](3de46f00-fbf9-0c6b-b7fa-5d33052d0091.htm)

[NumericRevisionSettings Overload](397b3f73-7652-1ddc-a15b-0a22ad268d21.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)