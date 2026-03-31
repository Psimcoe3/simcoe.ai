[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### SetDocumentation Method

---



|  |
| --- |
| [SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)   [See Also](#seeAlsoToggle) |

Sets the documentation string for the Schema.

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public SchemaBuilder SetDocumentation( 	string documentation ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function SetDocumentation ( _ 	documentation As String _ ) As SchemaBuilder ``` |

 

| Visual C++ |
| --- |
| ``` public: SchemaBuilder^ SetDocumentation( 	String^ documentation ) ``` |

#### Parameters

documentation
:   Type:  System String    
     The documentation string.

#### Return Value

The SchemaBuilder object may be used to add more settings.

# Remarks

While Entities may be hidden using access levels, Schemas and Fields are visible to clients and other developers. In the interest of clarity and interoperability, you are very strongly encouraged to provide good documentation with your Schemas. Explain the intent of the data and how it is meant to be interpreted. It is not useful to repeat information that can be observed directly (e.g. types and units). Note that documentation, like all other contents of Schemas and Fields is immutable once the add-in using the Schema is published.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The SchemaBuilder has already finished building the Schema. |

# See Also

[SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)