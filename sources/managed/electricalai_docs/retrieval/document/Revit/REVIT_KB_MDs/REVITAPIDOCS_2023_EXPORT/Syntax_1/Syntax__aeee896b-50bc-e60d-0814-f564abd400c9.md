[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsAlmostEqualTo Method (UV)

---



|  |
| --- |
| [UV Class](1724be37-059b-91ff-aa74-d1508082f76d.htm)   [See Also](#seeAlsoToggle) |

Determines whether this 2-D vector and the specified 2-D vector are the same within the tolerance (1.0e-09).

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public bool IsAlmostEqualTo( 	UV source ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsAlmostEqualTo ( _ 	source As UV _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsAlmostEqualTo( 	UV^ source ) ``` |

#### Parameters

source
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The vector to compare with this vector.

#### Return Value

True if the vectors are the same; otherwise, false.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when left is    a null reference (  Nothing  in Visual Basic)  . |

# See Also

[UV Class](1724be37-059b-91ff-aa74-d1508082f76d.htm)

[IsAlmostEqualTo Overload](a13f66b1-584a-f561-c34f-5b050d04de20.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)