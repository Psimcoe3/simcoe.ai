[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewArea Method

---



|  |
| --- |
| [Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)   [See Also](#seeAlsoToggle) |

Creates a new area

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Area NewArea( 	ViewPlan areaView, 	UV point ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewArea ( _ 	areaView As ViewPlan, _ 	point As UV _ ) As Area ``` |

 

| Visual C++ |
| --- |
| ``` public: Area^ NewArea( 	ViewPlan^ areaView,  	UV^ point ) ``` |

#### Parameters

areaView
:   Type:  [Autodesk.Revit.DB ViewPlan](0520580a-74ec-ed8c-35ea-5274c42276a3.htm)    
     The view of area element.

point
:   Type:  [Autodesk.Revit.DB UV](1724be37-059b-91ff-aa74-d1508082f76d.htm)    
     The point which lies in the enclosed region of AreaBoundaryLines to put the new created Area

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown if the area view does not exist in the given document. |

# See Also

[Document Class](ab1718f9-45fb-b3d3-827e-32ff81cf929c.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)