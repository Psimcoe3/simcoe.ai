[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetNormalAtVerticalProjectionPoint Method

---



|  |
| --- |
| [Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)   [See Also](#seeAlsoToggle) |

Return a surface normal on either the top or bottom face of a floor slab at a point corresponding to the vertical projection of an arbitrary point in project space.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ GetNormalAtVerticalProjectionPoint( 	XYZ modelLocation, 	FloorFace floorFace ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function GetNormalAtVerticalProjectionPoint ( _ 	modelLocation As XYZ, _ 	floorFace As FloorFace _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ GetNormalAtVerticalProjectionPoint( 	XYZ^ modelLocation,  	FloorFace floorFace ) ``` |

#### Parameters

modelLocation
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     A point in project coordinates whose vertical projection will determine the location at which the normal will be taken.

floorFace
:   Type:  [Autodesk.Revit.DB FloorFace](7a34e4cb-0a5d-5299-813b-edfbe364953b.htm)    
     A flag determining whether the top or bottom face of the floor should be used.

#### Return Value

Normal vector on the slab at the projection point.

# Remarks

If the floor is shape edited, the floor location at which we attempt to take the normal must be within the boundaries of a face on the slab. Otherwise the method will return    a null reference (  Nothing  in Visual Basic)  .

# See Also

[Floor Class](96cc6685-003d-ff90-1c5b-c25a4830f0f7.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)