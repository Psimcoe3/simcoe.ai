[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConcatenateChangeTypes Method

---



|  |
| --- |
| [ChangeType Class](bf7c5e20-b639-da97-4586-4a0bc0010705.htm)   [See Also](#seeAlsoToggle) |

Creates a ChangeType that is a union of the two input ChangeTypes

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2011

# Syntax

| C# |
| --- |
| ``` public static ChangeType ConcatenateChangeTypes( 	ChangeType changeType1, 	ChangeType changeType2 ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function ConcatenateChangeTypes ( _ 	changeType1 As ChangeType, _ 	changeType2 As ChangeType _ ) As ChangeType ``` |

 

| Visual C++ |
| --- |
| ``` public: static ChangeType^ ConcatenateChangeTypes( 	ChangeType^ changeType1,  	ChangeType^ changeType2 ) ``` |

#### Parameters

changeType1
:   Type:  [Autodesk.Revit.DB ChangeType](bf7c5e20-b639-da97-4586-4a0bc0010705.htm)    
     First input ChangeType to be concatenated

changeType2
:   Type:  [Autodesk.Revit.DB ChangeType](bf7c5e20-b639-da97-4586-4a0bc0010705.htm)    
     Second input ChangeType to be concatenated

#### Return Value

A new ChangeType that is a concatenation/union of the input change types

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ChangeType Class](bf7c5e20-b639-da97-4586-4a0bc0010705.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)