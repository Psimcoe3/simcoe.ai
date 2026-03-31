[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AreElementsNotConnectedInSeries Method

---



|  |
| --- |
| [MechanicalEquipmentSet Class](ce3c8e90-566c-bb8e-57f7-06f10dac5b7c.htm)   [See Also](#seeAlsoToggle) |

Checks if the elements are not serially connected.

**Namespace:**   [Autodesk.Revit.DB.Mechanical](0eafd899-5912-56fd-94b1-d286156e26fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2019

# Syntax

| C# |
| --- |
| ``` public static bool AreElementsNotConnectedInSeries( 	Document document, 	ISet<ElementId> elemIds ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function AreElementsNotConnectedInSeries ( _ 	document As Document, _ 	elemIds As ISet(Of ElementId) _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool AreElementsNotConnectedInSeries( 	Document^ document,  	ISet<ElementId^>^ elemIds ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document of these elements.

elemIds
:   Type:  System.Collections.Generic ISet   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The element ids to be tested.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[MechanicalEquipmentSet Class](ce3c8e90-566c-bb8e-57f7-06f10dac5b7c.htm)

[Autodesk.Revit.DB.Mechanical Namespace](0eafd899-5912-56fd-94b1-d286156e26fc.htm)