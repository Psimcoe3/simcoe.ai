[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsValidAccuracy Method (ForgeTypeId, Double)

---



|  |
| --- |
| [FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)   [See Also](#seeAlsoToggle) |

Checks whether an accuracy is valid for a given unit.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static bool IsValidAccuracy( 	ForgeTypeId unitTypeId, 	double accuracy ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function IsValidAccuracy ( _ 	unitTypeId As ForgeTypeId, _ 	accuracy As Double _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool IsValidAccuracy( 	ForgeTypeId^ unitTypeId,  	double accuracy ) ``` |

#### Parameters

unitTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     Identifier of the unit.

accuracy
:   Type:  System Double    
     The accuracy to check.

#### Return Value

True if the accuracy is valid, false otherwise.

# Remarks

See the  [Accuracy](bbba6604-8961-3a26-4e1f-73c2a2169464.htm)  property for details on valid accuracy values.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | unitTypeId is not a unit identifier. See UnitUtils.IsUnit(ForgeTypeId) and UnitUtils.GetUnitTypeId(DisplayUnitType). |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormatOptions Class](70f78207-1109-3906-8e67-cd27df1f0ae8.htm)

[IsValidAccuracy Overload](03bdea18-989e-f971-6a7f-32a6643b6d9b.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)