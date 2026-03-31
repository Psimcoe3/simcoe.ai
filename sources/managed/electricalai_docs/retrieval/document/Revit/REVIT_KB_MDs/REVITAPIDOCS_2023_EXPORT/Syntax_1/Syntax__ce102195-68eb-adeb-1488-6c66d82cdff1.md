[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AlphanumericRevisionSettings Constructor (IList(String), String, String)

---



|  |
| --- |
| [AlphanumericRevisionSettings Class](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.htm)   [See Also](#seeAlsoToggle) |

Constructs an AlphanumericRevisionSettings object.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public AlphanumericRevisionSettings( 	IList<string> sequence, 	string prefix, 	string suffix ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	sequence As IList(Of String), _ 	prefix As String, _ 	suffix As String _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: AlphanumericRevisionSettings( 	IList<String^>^ sequence,  	String^ prefix,  	String^ suffix ) ``` |

#### Parameters

sequence
:   Type:  System.Collections.Generic IList   String    

    The custom sequence to be used as numbers for revisions with the Alphanumeric RevisionNumberType.

    If there are more alphanumeric revisions than there are strings in the sequence, subsequent alphanumeric revisions will be assigned duplicated characters. For example, if the sequence provided were ["X", "Y"], the first alphanumeric revision would be shown as "X", the second as "Y", the third as "XX", then "YY", "XXX", etc.

prefix
:   Type:  System String    
     The prefix string for each revision number in the sequence.

suffix
:   Type:  System String    
     The suffix string for each revision number in the sequence.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Input sequence contains invalid entries. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AlphanumericRevisionSettings Class](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.htm)

[AlphanumericRevisionSettings Overload](48da20f1-0e3d-875e-4789-f9923c654238.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)