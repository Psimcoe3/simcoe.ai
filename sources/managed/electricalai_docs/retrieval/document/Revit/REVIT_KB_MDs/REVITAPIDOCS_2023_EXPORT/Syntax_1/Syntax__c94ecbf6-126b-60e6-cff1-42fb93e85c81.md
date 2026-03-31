[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetApplicationGUID Method

---



|  |
| --- |
| [SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)   [See Also](#seeAlsoToggle) |

Sets the GUID of the application or add-in that may access entities of this Schema under the Application acess level.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public SchemaBuilder SetApplicationGUID( 	Guid applicationGUID ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetApplicationGUID ( _ 	applicationGUID As Guid _ ) As SchemaBuilder ``` |

 

| Visual C++ |
| --- |
| ``` public: SchemaBuilder^ SetApplicationGUID( 	Guid applicationGUID ) ``` |

#### Parameters

applicationGUID
:   Type:  [System Guid](http://msdn2.microsoft.com/en-us/library/cey1zx63)    
     The application id.

#### Return Value

The SchemaBuilder object may be used to add more settings.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The SchemaBuilder has already finished building the Schema. |

# See Also

[SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)