[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetDefaultRepeatingReferenceSource Method

---



|  |
| --- |
| [RepeatingReferenceSource Class](c1a3887e-0272-7dcb-bed3-85c807ec39a0.htm)   [See Also](#seeAlsoToggle) |

Returns the default repeating reference source for a given element.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public static RepeatingReferenceSource GetDefaultRepeatingReferenceSource( 	Document document, 	ElementId elementId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function GetDefaultRepeatingReferenceSource ( _ 	document As Document, _ 	elementId As ElementId _ ) As RepeatingReferenceSource ``` |

 

| Visual C++ |
| --- |
| ``` public: static RepeatingReferenceSource^ GetDefaultRepeatingReferenceSource( 	Document^ document,  	ElementId^ elementId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that contains the element.

elementId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the element.

#### Return Value

The default repeating reference source of the given element.

# Remarks

The element must support repeating references. Use HasRepeatingReferenceSource() to find out whether an element has any repeating references.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element elementId does not exist in the document -or- The element does not have any repeating reference sources. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[RepeatingReferenceSource Class](c1a3887e-0272-7dcb-bed3-85c807ec39a0.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)