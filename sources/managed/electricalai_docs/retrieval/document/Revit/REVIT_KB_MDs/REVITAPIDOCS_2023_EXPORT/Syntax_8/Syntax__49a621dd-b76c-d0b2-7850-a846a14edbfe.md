[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CanDefineRevitGeometry Method

---



|  |
| --- |
| [Frame Class](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.htm)   [See Also](#seeAlsoToggle) |

Tests whether the supplied Frame object may be used to define a Revit curve or surface. In order to satisfy the requirements the Frame must be orthonormal and its origin is expected to lie within the Revit design limits  [IsWithinLengthLimits(XYZ)](ac2171af-4250-8a30-faa7-4d7030d29a03.htm)  .

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static bool CanDefineRevitGeometry( 	Frame frameOfReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function CanDefineRevitGeometry ( _ 	frameOfReference As Frame _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool CanDefineRevitGeometry( 	Frame^ frameOfReference ) ``` |

#### Parameters

frameOfReference
:   Type:  [Autodesk.Revit.DB Frame](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.htm)    
     Frame to be validated.

#### Return Value

True if this Frame may be used as a local frame of reference, false otherwise.

# Remarks

Certain Revit curve and surface types are defined using a local frame of reference.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[Frame Class](d44b3fd1-34d0-bfd0-55f6-de24235edf2e.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)