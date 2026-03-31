[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### IsCompatibleWith Method

---



|  |
| --- |
| [FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)   [See Also](#seeAlsoToggle) |

Check whether the service is broadly interchangable with another one without affecting part geometry. The services must have the same fabrication system template and specification.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` public bool IsCompatibleWith( 	FabricationService otherService ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function IsCompatibleWith ( _ 	otherService As FabricationService _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: bool IsCompatibleWith( 	FabricationService^ otherService ) ``` |

#### Parameters

otherService
:   Type:  [Autodesk.Revit.DB FabricationService](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)

#### Return Value

Returns true if the services are compatible.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[FabricationService Class](e29ecbb2-7de0-c341-0db0-9f77bd0f5543.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)