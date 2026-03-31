[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetName Method

---



|  |
| --- |
| [TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)   [See Also](#seeAlsoToggle) |

Sets the transaction group's name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public void SetName( 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetName ( _ 	name As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetName( 	String^ name ) ``` |

#### Parameters

name
:   Type:  System String    
     A name for the transaction group.

# Remarks

Transaction group only needs a name if it is going to be assimilated at the end.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)