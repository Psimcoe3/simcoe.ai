[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### CreateReferenceSection Method

---



|  |
| --- |
| [ViewSection Class](fcc75682-bd99-a97d-5a4d-0f8eb9e92ab5.htm)   [See Also](#seeAlsoToggle) |

Creates a new reference section.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2013

# Syntax

| C# |
| --- |
| ``` public static void CreateReferenceSection( 	Document document, 	ElementId parentViewId, 	ElementId viewIdToReference, 	XYZ headPoint, 	XYZ tailPoint ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub CreateReferenceSection ( _ 	document As Document, _ 	parentViewId As ElementId, _ 	viewIdToReference As ElementId, _ 	headPoint As XYZ, _ 	tailPoint As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void CreateReferenceSection( 	Document^ document,  	ElementId^ parentViewId,  	ElementId^ viewIdToReference,  	XYZ^ headPoint,  	XYZ^ tailPoint ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document to which the reference section will be added.

parentViewId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The view in which the new reference section marker will appear. Reference sections can be created in FloorPlan, CeilingPlan, StructuralPlan, Section, Elevation, Drafting, and Detail views.

viewIdToReference
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Detail, Drafting and Section views can be referenced. The ViewFamilyType of the referenced view will be used by the new reference section.

headPoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Determines the location of the section marker's head in the parent view.

tailPoint
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     Determines the location of the section marker's tail in the parent view.

# Remarks

The reference section will assume the ViewFamilyType of the view it references.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The ElementId viewIdToReference does not correspond to a View. -or- The ElementId parentViewId does not correspond to a View. -or- The parent view and the referenced view must be different views. -or- Can't create a new reference sections in parentViewId. Parent views must be FloorPlan, CeilingPlan, StructuralPlan, Section, Elevation, Drafting, or Detail views. -or- The viewIdToReference cannot be referenced by reference sections. Only Detail, Drafting and Section views can be referenced. -or- headPoint and tailPoint do not differ when projected onto a plane perpendicular to the view direction. -or- Reference section view creation is not allowed in this family. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed, and Revit requires the user to either cancel the operation or fix the problem (usually by deleting certain elements). -or- The document is being loaded, or is in the midst of another sensitive process. |
| [Autodesk.Revit.Exceptions ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

# See Also

[ViewSection Class](fcc75682-bd99-a97d-5a4d-0f8eb9e92ab5.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)