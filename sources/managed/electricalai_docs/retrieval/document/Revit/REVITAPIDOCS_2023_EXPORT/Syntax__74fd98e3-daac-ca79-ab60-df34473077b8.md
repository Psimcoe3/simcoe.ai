[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)   [See Also](#seeAlsoToggle) |

Retrieves a definition by a given name.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public Definition this[ 	string name ] { get; } ``` |

 

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Item ( _ 	name As String _ ) As Definition 	Get ``` |

 

| Visual C++ |
| --- |
| ``` public: property Definition^ Item[String^ name] { 	Definition^ get (String^ name); } ``` |

#### Parameters

name
:   Type:  [System String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)    
     The name of the parameter definition for which to search.

# Remarks

If the definition is not found then    a null reference (  Nothing  in Visual Basic)  will be returned.

# See Also

[Definitions Class](5ff217ff-215d-9d1a-6555-3f45b34a5517.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)