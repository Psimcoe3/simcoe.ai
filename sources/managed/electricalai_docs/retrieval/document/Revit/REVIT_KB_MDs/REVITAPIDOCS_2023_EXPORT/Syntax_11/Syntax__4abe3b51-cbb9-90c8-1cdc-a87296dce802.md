[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### NewXYZ Method (Double, Double, Double)

---



|  |
| --- |
| [Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)   [See Also](#seeAlsoToggle) |

Creates a XYZ object representing coordinates in 3-space with supplied values.

**Namespace:**   [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public XYZ NewXYZ( 	double x, 	double y, 	double z ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function NewXYZ ( _ 	x As Double, _ 	y As Double, _ 	z As Double _ ) As XYZ ``` |

 

| Visual C++ |
| --- |
| ``` public: XYZ^ NewXYZ( 	double x,  	double y,  	double z ) ``` |

#### Parameters

x
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The first coordinate.

y
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The second coordinate.

z
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The third coordinate.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when setting an infinite number to the X, Y or Z property. |

# See Also

[Application Class](5e11e5bf-82da-ae9b-1c52-95d0e9f28c96.htm)

[NewXYZ Overload](7d468115-a775-92da-7c1d-46b99bc86b19.htm)

[Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)