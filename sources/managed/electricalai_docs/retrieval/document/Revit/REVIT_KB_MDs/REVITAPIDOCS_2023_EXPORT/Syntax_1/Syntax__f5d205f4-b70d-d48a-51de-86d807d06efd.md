[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ConduitSize Constructor

---



|  |
| --- |
| [ConduitSize Class](4271b827-6390-ab67-036a-305101a712b5.htm)   [See Also](#seeAlsoToggle) |

Constructs an object that stores the basic size information for conduit.

**Namespace:**   [Autodesk.Revit.DB.Electrical](212a1314-7843-2c6c-3322-363127e4059f.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public ConduitSize( 	double nominalDiameter, 	double innerDiameter, 	double outerDiameter, 	double bendRadius, 	bool usedInSizeLists, 	bool usedInSizing ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	nominalDiameter As Double, _ 	innerDiameter As Double, _ 	outerDiameter As Double, _ 	bendRadius As Double, _ 	usedInSizeLists As Boolean, _ 	usedInSizing As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: ConduitSize( 	double nominalDiameter,  	double innerDiameter,  	double outerDiameter,  	double bendRadius,  	bool usedInSizeLists,  	bool usedInSizing ) ``` |

#### Parameters

nominalDiameter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Nominal diameter. The value should be a valid, positive Revit length.

innerDiameter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Inner diameter. The value should be a valid, positive Revit length.

outerDiameter
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Outer diameter. The value should be a valid, positive Revit length.

bendRadius
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     Minimum bend radius. The value should be a valid, positive Revit length.

usedInSizeLists
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Whether it is used in size lists.

usedInSizing
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)    
     Whether is used in sizing.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | The given value for nominalDiameter must be greater than 0 and no more than 30000 feet. -or- The given value for innerDiameter must be greater than 0 and no more than 30000 feet. -or- The given value for outerDiameter must be greater than 0 and no more than 30000 feet. -or- The given value for bendRadius must be greater than 0 and no more than 30000 feet. |

# See Also

[ConduitSize Class](4271b827-6390-ab67-036a-305101a712b5.htm)

[Autodesk.Revit.DB.Electrical Namespace](212a1314-7843-2c6c-3322-363127e4059f.htm)