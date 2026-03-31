[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ReplaceParameter Method (FamilyParameter, ExternalDefinition, ForgeTypeId, Boolean)

---



|  |
| --- |
| [FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)   [See Also](#seeAlsoToggle) |

Replace a family parameter with a shared parameter.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)

# Syntax

| C# |
| --- |
| ``` public FamilyParameter ReplaceParameter( 	FamilyParameter currentParameter, 	ExternalDefinition familyDefinition, 	ForgeTypeId groupTypeId, 	bool isInstance ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function ReplaceParameter ( _ 	currentParameter As FamilyParameter, _ 	familyDefinition As ExternalDefinition, _ 	groupTypeId As ForgeTypeId, _ 	isInstance As Boolean _ ) As FamilyParameter ``` |

 

| Visual C++ |
| --- |
| ``` public: FamilyParameter^ ReplaceParameter( 	FamilyParameter^ currentParameter,  	ExternalDefinition^ familyDefinition,  	ForgeTypeId^ groupTypeId,  	bool isInstance ) ``` |

#### Parameters

currentParameter
:   Type:  [Autodesk.Revit.DB FamilyParameter](6175e974-870e-7fbc-3df7-46105f937a6e.htm)    
     The current family parameter.

familyDefinition
:   Type:  [Autodesk.Revit.DB ExternalDefinition](a3e84415-b88e-a8e0-4e11-64795d92da0e.htm)    
     The definition of the loaded shared parameter.

groupTypeId
:   Type:  [Autodesk.Revit.DB ForgeTypeId](d9fcf276-9566-de83-2b0b-d89b65ccc8af.htm)    
     The identifier of the group to which the new shared parameter belongs.

isInstance
:   Type:  System Boolean    
     Indicates if the new parameter is instance or type.

#### Return Value

If replacement was successful the new shared parameter is returned, otherwise an exception with failure information will be thrown.

# Remarks

This operation is invalid for Built-in Parameters. The formulas and labels which in reference to this parameter will be updated to the new parameter.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument-"familyParameter" or "name"-is    a null reference (  Nothing  in Visual Basic)  . |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the input argument-"familyParameter"-is invalid, or the input parameter group cannot be assigned to the new parameter, or the input name string contains illegal characters, or duplicated with existing parameter name. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when trying to replace a built-in parameter. |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when replacement failed, because the replacement would cause a formula error. Or trying to replace with an instance parameter of image type. |

# See Also

[FamilyManager Class](1cc4fe6c-0e9f-7439-0021-32d2e06f4c33.htm)

[ReplaceParameter Overload](dee9a8dc-d1fb-812a-778d-9c4b1bb840e8.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)