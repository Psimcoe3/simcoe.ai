[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Item Property

---



|  |
| --- |
| [BindingMap Class](4ce777fb-ab30-6d15-d019-5b430223ac62.htm)   [See Also](#seeAlsoToggle) |

The get\_Item method will get the binding item related to the input key.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public override Binding this[ 	Definition key ] { get; set; } ``` |

 

| Visual Basic |
| --- |
| ``` Public Overrides Property Item ( _ 	key As Definition _ ) As Binding 	Get 	Set ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual property Binding^ Item[Definition^ key] { 	Binding^ get (Definition^ key) override; 	void set (Definition^ key, Binding^ value) override; } ``` |

#### Parameters

key
:   Type:  [Autodesk.Revit.DB Definition](8fe04f37-04e1-9e93-ffdb-e3900908e42a.htm)    
     A parameter definition which can be an existing definition or one from a shared parameters file.

#### Field Value

The returned value of get\_Item is an InstanceBinding or TypeBinding object that contains the set of categories to which the parameter is bound. The input item is an InstanceBinding or TypeBinding object which contains the set of categories to which the parameter should be bound.

# Remarks

set\_Item is not permitted for this class. A Autodesk::Revit::Exceptions::InvalidOperationException will be thrown. Instead use Insert, Remove and ReInsert to modify the bindings in the document.

# See Also

[BindingMap Class](4ce777fb-ab30-6d15-d019-5b430223ac62.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)