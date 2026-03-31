[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [PipeSegment Class](a295ca1d-66f2-f788-5079-4d91554a4223.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of a PipeSegment and adds it to the document.

**Namespace:**   [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static PipeSegment Create( 	Document ADocument, 	ElementId MaterialId, 	ElementId ScheduleId, 	ICollection<MEPSize> sizeSet ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	ADocument As Document, _ 	MaterialId As ElementId, _ 	ScheduleId As ElementId, _ 	sizeSet As ICollection(Of MEPSize) _ ) As PipeSegment ``` |

 

| Visual C++ |
| --- |
| ``` public: static PipeSegment^ Create( 	Document^ ADocument,  	ElementId^ MaterialId,  	ElementId^ ScheduleId,  	ICollection<MEPSize^>^ sizeSet ) ``` |

#### Parameters

ADocument
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document where the PipeSegment will be created and added.

MaterialId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ElementId of the MaterialElem of the pipe segment.

ScheduleId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The ElementId of the PipeScheduleType of the pipe segment.

sizeSet
:   Type:  System.Collections.Generic ICollection   [MEPSize](475cd9a4-e87a-6f9f-7e75-c079ac004166.htm)    
     A set of one or more sizes.

#### Return Value

The newly created pipe segment element.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The size list is empty. -or- The MaterialId and ScheduleId was already used by another pipe segment. Please use a new Material, a new Schedule/Type, or both. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Mechanical Electrical Piping. |

# See Also

[PipeSegment Class](a295ca1d-66f2-f788-5079-4d91554a4223.htm)

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)