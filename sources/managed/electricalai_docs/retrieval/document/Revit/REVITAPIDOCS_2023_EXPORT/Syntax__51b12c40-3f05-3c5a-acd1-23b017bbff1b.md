[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ScaleProfile Method

---



|  |
| --- |
| [Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)   [See Also](#seeAlsoToggle) |

Scale a profile of the form, by a specified origin and scale factor.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void ScaleProfile( 	int profileIndex, 	double factor, 	XYZ origin ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub ScaleProfile ( _ 	profileIndex As Integer, _ 	factor As Double, _ 	origin As XYZ _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void ScaleProfile( 	int profileIndex,  	double factor,  	XYZ^ origin ) ``` |

#### Parameters

profileIndex
:   Type:  [System Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)    
     Index to specify the profile.

factor
:   Type:  [System Double](http://msdn2.microsoft.com/en-us/library/643eft0t)    
     The scale factor, it should be large than zero.

origin
:   Type:  [Autodesk.Revit.DB XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm)    
     The origin where scale happens.

# See Also

[Form Class](49f6ae4c-1629-98ef-d9a9-799bb1fd43ec.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)