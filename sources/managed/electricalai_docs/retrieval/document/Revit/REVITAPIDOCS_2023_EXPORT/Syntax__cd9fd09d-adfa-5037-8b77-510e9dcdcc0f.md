[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AsInteger Method

---



|  |
| --- |
| [FamilyType Class](7f15b213-c99b-db59-3622-3280757b82d9.htm)   [See Also](#seeAlsoToggle) |

Provides access to the integer number of the given family parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Nullable<int> AsInteger( 	FamilyParameter familyParameter ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AsInteger ( _ 	familyParameter As FamilyParameter _ ) As Nullable(Of Integer) ``` |

 

| Visual C++ |
| --- |
| ``` public: Nullable<int> AsInteger( 	FamilyParameter^ familyParameter ) ``` |

#### Parameters

familyParameter
:   Type:  [Autodesk.Revit.DB FamilyParameter](6175e974-870e-7fbc-3df7-46105f937a6e.htm)

#### Return Value

The integer value contained in the parameter. Returns    a null reference (  Nothing  in Visual Basic)  if the storage type of the input argument is not integer type or this parameter has no value.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-"familyParameter"-is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the input argument-"familyParameter"-is invalid, |

# See Also

[FamilyType Class](7f15b213-c99b-db59-3622-3280757b82d9.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)