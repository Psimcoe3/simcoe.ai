[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### OverrideTypeParams Property

---



|  |
| --- |
| [StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)   [See Also](#seeAlsoToggle) |

Allow or disallow connection's type parameters to be overridden.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 21.0.0.0 (21.1.1.109)   
  **Since:**  2020

# Syntax

| C# |
| --- |
| ``` public bool OverrideTypeParams { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Property OverrideTypeParams As Boolean 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: property bool OverrideTypeParams { 	bool get (); 	void set (bool value); } ``` |

# Remarks

When set to true, a set of instance parameters is created for this connection by copying the type parameter set and the user can change this instance parameters in order to make this connection different from the others of the same type. Any further modification on type parameters will not affect this instance (until the "override" is turned back off). When set to false the connection instance parameters are discarded and the type parameters are used again. The default value of this parameter is false.

# See Also

[StructuralConnectionHandler Class](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)