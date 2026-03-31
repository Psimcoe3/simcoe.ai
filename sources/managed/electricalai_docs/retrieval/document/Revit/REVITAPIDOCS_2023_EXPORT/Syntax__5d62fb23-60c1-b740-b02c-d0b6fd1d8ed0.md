[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### RotateElements Method

---



|  |
| --- |
| [ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)   [See Also](#seeAlsoToggle) |

Rotates a set of elements about the given axis and angle.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static void RotateElements( 	Document document, 	ICollection<ElementId> elementsToRotate, 	Line axis, 	double angle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub RotateElements ( _ 	document As Document, _ 	elementsToRotate As ICollection(Of ElementId), _ 	axis As Line, _ 	angle As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void RotateElements( 	Document^ document,  	ICollection<ElementId^>^ elementsToRotate,  	Line^ axis,  	double angle ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document that owns the elements.

elementsToRotate
:   Type:  System.Collections.Generic ICollection   [ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The set of elements to rotate.

axis
:   Type:  [Autodesk.Revit.DB Line](e7329450-434a-918b-661c-65e15e0585a5.htm)    
     The axis of rotation.

angle
:   Type:  System Double    
     The angle of rotation in radians.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given element id set is empty. -or- One or more elements in elementsToRotate do not exist in the document. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[ElementTransformUtils Class](82e737d5-fda4-bc10-6099-88999cd51300.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)