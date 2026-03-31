[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, ElementId, LinkElementId, Reference)

---



|  |
| --- |
| [NumberSystem Class](5c027e93-1dff-9a6e-8602-5b3a3da60ada.htm)   [See Also](#seeAlsoToggle) |

Creates a new instance of a NumberSystem associated to a host element and a view.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2018

# Syntax

| C# |
| --- |
| ``` public static NumberSystem Create( 	Document document, 	ElementId viewId, 	LinkElementId numberedElementId, 	Reference referenceCurve ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	viewId As ElementId, _ 	numberedElementId As LinkElementId, _ 	referenceCurve As Reference _ ) As NumberSystem ``` |

 

| Visual C++ |
| --- |
| ``` public: static NumberSystem^ Create( 	Document^ document,  	ElementId^ viewId,  	LinkElementId^ numberedElementId,  	Reference^ referenceCurve ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document.

viewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The view in which the NumberSystem will be created.

numberedElementId
:   Type:  [Autodesk.Revit.DB LinkElementId](6e18abde-8787-9906-8576-ab0c9c5432c6.htm)    
     The host id on which the NumberSystem will be created.

referenceCurve
:   Type:  [Autodesk.Revit.DB Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     The reference curve along which the NumberSystem will be created. It is suggested to get the new reference via GetNumberSystemReference() from the host element.

#### Return Value

The created NumberSystem.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | viewId is not valid for placement of a NumberSystem (only floor plan views and elevation views are permitted). -or- numberedElementId is not valid as a host for NumberSystem (only StairsRun elements are permitted in this release). -or- The referenceCurve is not valid for NumberSystem on numberedElementId. -or- The numberedElementId already has a NumberSystem. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[NumberSystem Class](5c027e93-1dff-9a6e-8602-5b3a3da60ada.htm)

[Create Overload](e56310b2-3357-dadf-7f42-2ccac6045e70.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)