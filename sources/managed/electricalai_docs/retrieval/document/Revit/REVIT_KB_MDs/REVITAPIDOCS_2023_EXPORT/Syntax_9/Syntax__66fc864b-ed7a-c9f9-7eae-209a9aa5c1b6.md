[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### VendorIdIsValid Method

---



|  |
| --- |
| [SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)   [See Also](#seeAlsoToggle) |

Checks whether the given vendor ID string is valid. A valid vendor ID string: 1. Has a length of at least 4 characters and no more than 253 characters, and 2. Contains only letters, digits, or any of the following special characters: ! " # & \ ( ) + , . - : ; < = > ? \_ ` | ~

**Namespace:**   [Autodesk.Revit.DB.ExtensibleStorage](79486a74-376c-9555-c873-45d5a750f051.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static bool VendorIdIsValid( 	string vendorId ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function VendorIdIsValid ( _ 	vendorId As String _ ) As Boolean ``` |

 

| Visual C++ |
| --- |
| ``` public: static bool VendorIdIsValid( 	String^ vendorId ) ``` |

#### Parameters

vendorId
:   Type:  System String    
     The vendor ID to check.

#### Return Value

True if the vendor ID is valid.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[SchemaBuilder Class](e74f9357-cc3c-558e-73b8-38ce6d247869.htm)

[Autodesk.Revit.DB.ExtensibleStorage Namespace](79486a74-376c-9555-c873-45d5a750f051.htm)