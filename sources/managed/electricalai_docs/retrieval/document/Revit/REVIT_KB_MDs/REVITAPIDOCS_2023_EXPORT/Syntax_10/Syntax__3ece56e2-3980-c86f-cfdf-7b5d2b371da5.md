[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method

---



|  |
| --- |
| [Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)   [See Also](#seeAlsoToggle) |

Creates a new parameter definition using specified options.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2015

# Syntax

| C# |
| --- |
| ``` public Definition Create( 	ExternalDefinitionCreationOptions option ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function Create ( _ 	option As ExternalDefinitionCreationOptions _ ) As Definition ``` |

 

| Visual C++ |
| --- |
| ``` public: Definition^ Create( 	ExternalDefinitionCreationOptions^ option ) ``` |

#### Parameters

option
:   Type:  [Autodesk.Revit.DB ExternalDefinitionCreationOptions](1cd9e425-23a3-04f8-c130-4d4a799abd13.htm)    
     The options used to create the new parameter definition.

#### Return Value

If successful a reference to the new parameter definition is returned, otherwise    a null reference (  Nothing  in Visual Basic)  .

# Remarks

This method only supports creation of new external definitions (shared parameters).

# See Also

[Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)