[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddDefinitionType Method

---



|  |
| --- |
| [DirectShapeLibrary Class](07489bae-ab9f-e2a8-0ac1-0a4d70cea458.htm)   [See Also](#seeAlsoToggle) |

Add a definition to be reused by instances. Adding a definition type will change how the instances are created. When asked to create a definition, the library object will look for a corresponding type object. If one is found, it will create an instance of geometry stored in the type object. If it is not found, the library will look for a list of geometry objects stored as definition, and will copy and transform these to create an instance.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public void AddDefinitionType( 	string id, 	ElementId typeId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub AddDefinitionType ( _ 	id As String, _ 	typeId As ElementId _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void AddDefinitionType( 	String^ id,  	ElementId^ typeId ) ``` |

#### Parameters

id
:   Type:  System String    
     ID of the definition to be added. Must be unique.

typeId
:   Type:  [Autodesk.Revit.DB ElementId](44f3f7b1-3229-3404-93c9-dc5e70337dd6.htm)    
     Element id of the DirectShapeType element that will be used as a definition.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[DirectShapeLibrary Class](07489bae-ab9f-e2a8-0ac1-0a4d70cea458.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)