[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Equals Method

---



|  |
| --- |
| [GeometryObject Class](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)   [See Also](#seeAlsoToggle) |

Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override bool Equals( 	Object obj ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Function Equals ( _ 	obj As Object _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Equals( 	Object^ obj ) override ``` |

#### Parameters

obj
:   Type:  [System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
     Another object.

# Remarks

This compares the internal identifiers of the geometry, and doesn't compare them geometrically.

# See Also

[GeometryObject Class](e0f15010-0e19-6216-e2f0-ab7978145daa.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)