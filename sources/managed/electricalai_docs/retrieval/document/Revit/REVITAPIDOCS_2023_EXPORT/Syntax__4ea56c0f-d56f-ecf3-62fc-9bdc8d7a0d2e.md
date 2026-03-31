[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### DissolveForms Method (Document, ICollection(ElementId), ICollection(ElementId))

---



|  |
| --- |
| [FormUtils Class](fe80084f-2b75-cc39-bf64-866bc2c27bb1.htm)   [See Also](#seeAlsoToggle) |

Dissolves a collection of form elements into their defining elements.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public static ICollection<ElementId> DissolveForms( 	Document ADoc, 	ICollection<ElementId> elements, 	out ICollection<ElementId> ProfileOriginPointSet ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function DissolveForms ( _ 	ADoc As Document, _ 	elements As ICollection(Of ElementId), _ 	<OutAttribute> ByRef ProfileOriginPointSet As ICollection(Of ElementId) _ ) As ICollection(Of ElementId) ``` |

 

| Visual C++ |
| --- |
| ``` public: static ICollection<ElementId^>^ DissolveForms( 	Document^ ADoc,  	ICollection<ElementId^>^ elements,  	[OutAttribute] ICollection<ElementId^>^% ProfileOriginPointSet ) ``` |

#### Parameters

ADoc
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document

elements
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     A collection of element IDs of Forms and GeomCombinations that contain Forms that will be dissolved.

ProfileOriginPointSet
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)   %    
     A collection of the point element ids that represent the 'origin' of the profiles

#### Return Value

A collection of curve element ids from the profiles and paths of the dissolved forms.

# Remarks

Profile origin points define the workplane of form profiles and paths and their curves. The profile origin point represents a coordinate system with an origin (reference point) which can be manipulated to move the curves of a profile together as a unit after dissolve. Profile origin points may themselves be constrained to other parts of the model or parts of the form, based on how the form was created/constructed. This is done through the reference point hosting mechanism.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The elements do not include Forms that can be dissolved. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FormUtils Class](fe80084f-2b75-cc39-bf64-866bc2c27bb1.htm)

[DissolveForms Overload](9a152dc3-04f7-aaf2-91a3-2715652ed95d.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)