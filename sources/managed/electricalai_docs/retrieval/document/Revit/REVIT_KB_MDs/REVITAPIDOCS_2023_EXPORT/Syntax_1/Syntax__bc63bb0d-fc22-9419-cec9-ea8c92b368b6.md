[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransactionGroup Constructor (Document, String)

---



|  |
| --- |
| [TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)   [See Also](#seeAlsoToggle) |

It constructs a transaction group object

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public TransactionGroup( 	Document document, 	string transGroupName ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	document As Document, _ 	transGroupName As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: TransactionGroup( 	Document^ document,  	String^ transGroupName ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document for which this transaction group is being used.

transGroupName
:   Type:  System String    
     Name of the group. The name will be used only for a group that is  [assimilated](158471e4-5554-16ed-f9bf-f7499b86309c.htm)  at the end.

# Remarks

The group does not start until its Start method is called.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[TransactionGroup Class](f1113d30-4c36-7844-1537-aad7f095cea0.htm)

[TransactionGroup Overload](34d0ec0c-037e-3604-2ec4-845e80237192.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)