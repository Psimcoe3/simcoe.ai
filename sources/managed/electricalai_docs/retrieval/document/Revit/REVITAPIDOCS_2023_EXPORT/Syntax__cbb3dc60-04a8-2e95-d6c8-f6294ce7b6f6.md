[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetPanel Method

---



|  |
| --- |
| [CurtainGrid Class](5e0d5b7c-aaa1-d299-6fb8-2faa65b1857a.htm)   [See Also](#seeAlsoToggle) |

Get the specified panel located by the intersection of the grid lines.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Panel GetPanel( 	ElementId uGridLineId, 	ElementId vGridLineId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetPanel ( _ 	uGridLineId As ElementId, _ 	vGridLineId As ElementId _ ) As Panel ``` |

 

| Visual C++ |
| --- |
| ``` public: Panel^ GetPanel( 	ElementId^ uGridLineId,  	ElementId^ vGridLineId ) ``` |

#### Parameters

uGridLineId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of a grid line in the U-direction used to locate the panel.

vGridLineId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     The id of a grid line in the V-direction used to locate the panel.

#### Return Value

The panel, or    a null reference (  Nothing  in Visual Basic)  if the panel cannot be found at this intersection.

# See Also

[CurtainGrid Class](5e0d5b7c-aaa1-d299-6fb8-2faa65b1857a.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)