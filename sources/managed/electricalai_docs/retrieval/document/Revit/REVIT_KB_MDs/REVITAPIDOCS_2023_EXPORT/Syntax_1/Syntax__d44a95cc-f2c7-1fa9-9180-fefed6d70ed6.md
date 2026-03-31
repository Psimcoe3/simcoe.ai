[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetReferenceByName Method

---



|  |
| --- |
| [FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)   [See Also](#seeAlsoToggle) |

Gets the family instance reference corresponding to the named reference plane in the instance's family.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public Reference GetReferenceByName( 	string name ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetReferenceByName ( _ 	name As String _ ) As Reference ``` |

 

| Visual C++ |
| --- |
| ``` public: Reference^ GetReferenceByName( 	String^ name ) ``` |

#### Parameters

name
:   Type:  System String    
     The name of the reference plane in the family.

#### Return Value

Returns the family instance reference corresponding to the named reference plane in the instance's family. Returns null if there is no reference plane with this name in the family, or if the plane exists but its "Is Reference" property is "Not a Reference", or if the input string is empty.

# Remarks

If there is a reference plane in the instance's family that has the given name, and the plane's "Is Reference" property is not "Not a Reference", there will be a corresponding reference in the family's instance. This function returns that reference.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FamilyInstance Class](0d2231f8-91e6-794f-92ae-16aad8014b27.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)