[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, Element, IList(Curve), Boolean, ElementId, ElementId, ElementId, ElementId, ElementId)

---



|  |
| --- |
| [PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)   [See Also](#seeAlsoToggle) |

Creates a new PathReinforcement object from an array of curves and given Rebar Shape id.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public static PathReinforcement Create( 	Document document, 	Element hostElement, 	IList<Curve> curveArray, 	bool flip, 	ElementId pathReinforcementTypeId, 	ElementId rebarBarTypeId, 	ElementId startRebarHookTypeId, 	ElementId endRebarHookTypeId, 	ElementId rebarShapeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	hostElement As Element, _ 	curveArray As IList(Of Curve), _ 	flip As Boolean, _ 	pathReinforcementTypeId As ElementId, _ 	rebarBarTypeId As ElementId, _ 	startRebarHookTypeId As ElementId, _ 	endRebarHookTypeId As ElementId, _ 	rebarShapeId As ElementId _ ) As PathReinforcement ``` |

 

| Visual C++ |
| --- |
| ``` public: static PathReinforcement^ Create( 	Document^ document,  	Element^ hostElement,  	IList<Curve^>^ curveArray,  	bool flip,  	ElementId^ pathReinforcementTypeId,  	ElementId^ rebarBarTypeId,  	ElementId^ startRebarHookTypeId,  	ElementId^ endRebarHookTypeId,  	ElementId^ rebarShapeId ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

hostElement
:   Type:  [Autodesk.Revit.DB Element](eb16114f-69ea-f4de-0d0d-f7388b105a16.htm)    
     The element that will host the PathReinforcement. The host can be a Structural Floor, Structural Wall, Structural Slab, or a Part created from a structural layer belonging to one of those element types.

curveArray
:   Type:  System.Collections.Generic IList   [Curve](400cc9b6-9ff7-de85-6fd8-c20002209d25.htm)    
     An array of curves that will define the outline of the PathReinforcement.

flip
:   Type:  System Boolean    
     A flag controlling the bars relative to the curves.

pathReinforcementTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the PathReinforcementType.

rebarBarTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the RebarBarType.

startRebarHookTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the RebarHookType for the start of the bar. If this parameter is InvalidElementId, it means to create a rebar with no start hook.

endRebarHookTypeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the RebarHookType for the end of the bar. If this parameter is InvalidElementId, it means to create a rebar with no end hook.

rebarShapeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of the RebarShape element that defines the shape of the rebars in the object.

#### Return Value

The newly created PathReinforcement.

# Remarks

The method sets Rebar Shape of primary bars only.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The input curveArray is empty. -or- The input curveArray contains at least one helical curve and is not supported for this operation. -or- The element hostElement was not found in the given document. -or- the host Element is not a valid host for Area Reinforcement, Path Reinforcement, Fabric Area or Fabric Sheet. -or- The structural rebar is not within area and path reinforcement. -or- curves in curveArray are not continuous and open. -or- pathReinforcementTypeId should refer to an Path Reinforcement Type element. -or- rebarBarTypeId should refer to an RebarBarType element. -or- startRebarHookTypeId should be invalid or refer to an RebarHookType element. -or- endRebarHookTypeId should be invalid or refer to an RebarHookType element. -or- rebarShapeId should refer to two dimensional Rebar Shape element with segments forming only right angles. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | startRebarHookTypeId cannot be set for given rebar shape. -or- endRebarHookTypeId cannot be set for given rebar shape. |
| [Autodesk.Revit.Exceptions DisabledDisciplineException](3693dcdf-67fb-0128-3be8-cad150e9498e.htm) | None of the following disciplines is enabled: Structural. |
| [Autodesk.Revit.Exceptions ForbiddenForDynamicUpdateException](c5b911f6-1e8f-2cd4-6965-286f41221fe0.htm) | This method may not be called during dynamic update. |

# See Also

[PathReinforcement Class](1593a849-b883-73d4-7c02-a2522877d71d.htm)

[Create Overload](073bd440-fbd7-5185-994c-224e7c52b172.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)