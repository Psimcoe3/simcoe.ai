[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### ParameterGroup Property

---



|  |
| --- |
| [InternalDefinition Class](97f42435-3067-622e-7a34-919f42f6ab97.htm)   [See Also](#seeAlsoToggle) |

Id of a built-in parameter group to which the parameter defined by this definition belongs.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 17.0.0.0 (17.0.1090.0)

# Syntax

| C# |
| --- |
| ``` public override BuiltInParameterGroup ParameterGroup { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Property ParameterGroup As BuiltInParameterGroup 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property BuiltInParameterGroup ParameterGroup { 	BuiltInParameterGroup get () override; 	void set (BuiltInParameterGroup value) override; } ``` |

# Remarks

The parameter group can be changed, but only for parameters that are not built in. In other words: Modifying the value of this property is only valid for parameter definitions whose BuiltInParameter property returns BuiltInParameter.INVALID, e.g. Global Parameters.

# See Also

[InternalDefinition Class](97f42435-3067-622e-7a34-919f42f6ab97.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)