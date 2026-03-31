[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddMacro Method

---



|  |
| --- |
| [MacroModule Class](d604a3cb-4f41-78a8-6353-270c566ac661.htm)   [See Also](#seeAlsoToggle) |

Adds a macro to the module.

**Namespace:**   [Autodesk.Revit.DB.Macros](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)    
  **Assembly:**   RevitAPIMacros  (in RevitAPIMacros.dll) Version: 23.0.0.0 (23.1.0.0)   
  **Since:**  2014

# Syntax

| C# |
| --- |
| ``` public Macro AddMacro( 	string name, 	string description, 	string code ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Function AddMacro ( _ 	name As String, _ 	description As String, _ 	code As String _ ) As Macro ``` |

 

| Visual C++ |
| --- |
| ``` public: Macro^ AddMacro( 	String^ name,  	String^ description,  	String^ code ) ``` |

#### Parameters

name
:   Type:  System String    
     The macro name.

description
:   Type:  System String    
     The description.

code
:   Type:  System String    
     The code string, which should be the lines between the main bounding brackets of a method.

#### Return Value

The new macro.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |
| [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Cannot add the Macro due to no permission. |

# See Also

[MacroModule Class](d604a3cb-4f41-78a8-6353-270c566ac661.htm)

[Autodesk.Revit.DB.Macros Namespace](8b8f9876-f4c2-abff-fc5b-79e337d84e01.htm)