[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Insert Method (Definition, Binding)

---



|  |
| --- |
| [BindingMap Class](4ce777fb-ab30-6d15-d019-5b430223ac62.htm)   [See Also](#seeAlsoToggle) |

Creates a new parameter binding between a parameter and a set of categories.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override bool Insert( 	Definition key, 	Binding item ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Function Insert ( _ 	key As Definition, _ 	item As Binding _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual bool Insert( 	Definition^ key,  	Binding^ item ) override ``` |

#### Parameters

key
:   Type:  [Autodesk.Revit.DB Definition](8fe04f37-04e1-9e93-ffdb-e3900908e42a.htm)    
     A parameter definition which can be an existing definition or one from a shared parameters file.

item
:   Type:  [Autodesk.Revit.DB Binding](47f6ad6f-8d00-af57-995e-dc6db1255f58.htm)    
     An InstanceBinding or TypeBinding object which contains the set of categories to which the parameter should be bound.

# Remarks

Note the type of the binding object dictates whether the parameter is bound to all instances or just types. A parameter definition cannot be bound to both instances and types. If the parameter binding already exists, post an error and return false.

# See Also

[BindingMap Class](4ce777fb-ab30-6d15-d019-5b430223ac62.htm)

[Insert Overload](3dee6805-87a1-390c-d467-64eca33dbb11.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)