[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetPresenceOfSegments Method

---



|  |
| --- |
| [RebarShapeMultiplanarDefinition Class](47a3135c-ce53-c041-f551-0795767eaa41.htm)   [See Also](#seeAlsoToggle) |

Simultaneously set the presence of all 3D segments.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public void SetPresenceOfSegments( 	bool isDuplicateShapePresent, 	bool isStartConnectorPresent, 	bool isEndConnectorPresent ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Sub SetPresenceOfSegments ( _ 	isDuplicateShapePresent As Boolean, _ 	isStartConnectorPresent As Boolean, _ 	isEndConnectorPresent As Boolean _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: void SetPresenceOfSegments( 	bool isDuplicateShapePresent,  	bool isStartConnectorPresent,  	bool isEndConnectorPresent ) ``` |

#### Parameters

isDuplicateShapePresent
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)

isStartConnectorPresent
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)

isEndConnectorPresent
:   Type:  [System Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentsInconsistentException](05972c68-fa6d-3a83-d720-ad84fbc4780f.htm) | The shape is disconnected or forms a complete loop: If the duplicate shape is present, exactly one of the connectors must be present. |

# See Also

[RebarShapeMultiplanarDefinition Class](47a3135c-ce53-c041-f551-0795767eaa41.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)