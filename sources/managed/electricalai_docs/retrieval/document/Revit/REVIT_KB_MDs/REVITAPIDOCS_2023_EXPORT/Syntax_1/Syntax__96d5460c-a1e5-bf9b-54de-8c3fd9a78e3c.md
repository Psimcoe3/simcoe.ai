[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetBarIndexFromReference Method

---



|  |
| --- |
| [RebarInSystem Class](c0bd03fa-78f4-eb67-54e8-e28368e94beb.htm)   [See Also](#seeAlsoToggle) |

Given a reference that represents a part of a bar, this method will return the bar index.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2022

# Syntax

| C# |
| --- |
| ``` public int GetBarIndexFromReference( 	Reference barReference ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetBarIndexFromReference ( _ 	barReference As Reference _ ) As Integer ``` |

 

| Visual C++ |
| --- |
| ``` public: int GetBarIndexFromReference( 	Reference^ barReference ) ``` |

#### Parameters

barReference
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The Reference of the RebarInSystem element.

#### Return Value

The bar index the reference refers to.

# Remarks

The method returns an index between 0 and NumberOfBarPositions - 1 if it the given reference represents a part of a bar. Otherwise will return -1.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RebarInSystem Class](c0bd03fa-78f4-eb67-54e8-e28368e94beb.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)