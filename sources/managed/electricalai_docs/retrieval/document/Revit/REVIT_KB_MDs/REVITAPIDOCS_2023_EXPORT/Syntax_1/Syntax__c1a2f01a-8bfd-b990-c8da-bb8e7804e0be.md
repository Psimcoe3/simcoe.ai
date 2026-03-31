[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsEqual Method

---



|  |
| --- |
| [AlphanumericRevisionSettings Class](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.htm)   [See Also](#seeAlsoToggle) |

Determines whether a specified AlphanumericRevisionSettings is the same as 'this'.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool IsEqual( 	AlphanumericRevisionSettings other ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsEqual ( _ 	other As AlphanumericRevisionSettings _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsEqual( 	AlphanumericRevisionSettings^ other ) ``` |

#### Parameters

other
:   Type:  [Autodesk.Revit.DB AlphanumericRevisionSettings](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.htm)    
     The AlphanumericRevisionSettings object to be compared with 'this'.

#### Return Value

True, if two AlphanumericRevisionSettings are the same.

# Remarks

The two AlphanumericRevisionSettings are regarded as the same only if they have the same revision numbering sequence, and the same prefix and suffix strings.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[AlphanumericRevisionSettings Class](ee27c0eb-9f9b-b59c-728d-24b2654a2bc2.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)