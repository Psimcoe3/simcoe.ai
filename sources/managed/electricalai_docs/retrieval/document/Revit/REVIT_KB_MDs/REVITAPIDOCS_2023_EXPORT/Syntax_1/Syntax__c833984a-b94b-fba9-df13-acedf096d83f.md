[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ProjectPosition Constructor

---



|  |
| --- |
| [ProjectPosition Class](249111cc-c1f3-d3e1-e7bf-dc791327fd4c.htm)   [See Also](#seeAlsoToggle) |

Construct a new ProjectPosition with the specified East/West offset, North/South offset, elevation offset, and angle of rotation.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 18.0.0.0 (18.2.0.0)

# Syntax

| C# |
| --- |
| ``` public ProjectPosition( 	double ew, 	double ns, 	double elevation, 	double angle ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	ew As Double, _ 	ns As Double, _ 	elevation As Double, _ 	angle As Double _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ProjectPosition( 	double ew,  	double ns,  	double elevation,  	double angle ) ``` |

#### Parameters

ew
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     East/West offset

ns
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     North/South offset

elevation
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Elevation offset

angle
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Rotation from true north, in radians

# Remarks

The angle parameter must be in the range of -PI to PI. If the parameter value is outside that range, it will be shifted by 2\*PI until it falls into range.

# See Also

[ProjectPosition Class](249111cc-c1f3-d3e1-e7bf-dc791327fd4c.htm)

[ProjectPosition Overload](c4c981f5-3e50-38c2-7d22-936664ff23a8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)