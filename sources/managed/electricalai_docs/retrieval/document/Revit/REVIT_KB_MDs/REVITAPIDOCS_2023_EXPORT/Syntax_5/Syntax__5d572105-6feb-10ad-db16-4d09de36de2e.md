[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### TransientElementCreationException Class

---



|  |
| --- |
| [Members](0a774137-1e3f-263e-433d-e6c68ab9e684.htm)   [See Also](#seeAlsoToggle) |

The exception that is thrown when TransientElementCreationScope is used incorrectly.

**Namespace:**   [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 16.0.0.0 (16.0.0.0)   
  **Since:**  2016

# Syntax

| C# |
| --- |
| ``` [SerializableAttribute] public class TransientElementCreationException : InvalidOperationException ``` |

 

| Visual Basic |
| --- |
| ``` <SerializableAttribute> _ Public Class TransientElementCreationException _ 	Inherits InvalidOperationException ``` |

 

| Visual C++ |
| --- |
| ``` [SerializableAttribute] public ref class TransientElementCreationException : public InvalidOperationException ``` |

# Remarks

The exception would be thrown in the following cases:

* An element that does not support TransientElementCreationScope is being created in the Scope.
* A TransientElementCreationScope is being created while another such scope is already active.

# Inheritance Hierarchy

[System Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)    
  [System Exception](http://msdn2.microsoft.com/en-us/library/c18k6c59)    
  [Autodesk.Revit.Exceptions ApplicationException](05012a96-16ea-ace7-6115-b45406dacead.htm)    
  [Autodesk.Revit.Exceptions InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm)    
  Autodesk.Revit.Exceptions TransientElementCreationException

# See Also

[TransientElementCreationException Members](0a774137-1e3f-263e-433d-e6c68ab9e684.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)