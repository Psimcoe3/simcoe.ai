[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SplitStraight Method

---



|  |
| --- |
| [FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)   [See Also](#seeAlsoToggle) |

Splits the straight into two at the passed in point.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017 Subscription Update

# Syntax

| C# |
| --- |
| ``` public ElementId SplitStraight( 	Document document, 	ElementId partId, 	XYZ position ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SplitStraight ( _ 	document As Document, _ 	partId As ElementId, _ 	position As XYZ _ ) As ElementId ``` |

 

| Visual C++ |
| --- |
| ``` public: ElementId^ SplitStraight( 	Document^ document,  	ElementId^ partId,  	XYZ^ position ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

partId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Id of the straight to split.

position
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The position to split in the straight.

#### Return Value

Returns the ElementId of the new straight.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The part is not a straight. -or- The position is not on the straight. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationPart Class](c9b86162-c105-696a-a919-49a7a7938cc4.htm)

[SplitStraight Overload](a24bd95a-25d1-88fd-d33a-2d9f9cd9fabd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)