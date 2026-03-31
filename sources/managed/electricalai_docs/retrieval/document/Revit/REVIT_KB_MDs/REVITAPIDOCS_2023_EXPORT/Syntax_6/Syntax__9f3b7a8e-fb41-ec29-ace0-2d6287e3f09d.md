[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Inequality Operator

---



|  |
| --- |
| [GeometryObject Class](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)   [See Also](#seeAlsoToggle) |

Determines whether two GeometryObjects are different.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public static bool operator !=( 	GeometryObject first, 	GeometryObject second ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Operator <> ( _ 	first As GeometryObject, _ 	second As GeometryObject _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool operator !=( 	GeometryObject^ first,  	GeometryObject^ second ) ``` |

#### Parameters

first
:   Type:  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
     The first GeometryObject.

second
:   Type:  [Autodesk.Revit.DB GeometryObject](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)    
     The second GeometryObject.

#### Return Value

True if the GeometryObjects are different; otherwise, false.

# Remarks

This compares the internal identifiers of the geometry, and doesn't compare them geometrically.

# See Also

[GeometryObject Class](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)