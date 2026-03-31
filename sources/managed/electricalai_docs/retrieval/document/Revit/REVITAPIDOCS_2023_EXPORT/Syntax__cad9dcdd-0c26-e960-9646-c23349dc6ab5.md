[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### Create Method (Document, ThermalAsset)

---



|  |
| --- |
| [PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.htm)   [See Also](#seeAlsoToggle) |

Creates a new PropertySetElement to contain the given asset.

**Namespace:**   [Autodesk.Revit.DB](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2012

# Syntax

| C# |
| --- |
| ``` public static PropertySetElement Create( 	Document document, 	ThermalAsset thermalAsset ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Function Create ( _ 	document As Document, _ 	thermalAsset As ThermalAsset _ ) As PropertySetElement ``` |

 

| Visual C++ |
| --- |
| ``` public: static PropertySetElement^ Create( 	Document^ document,  	ThermalAsset^ thermalAsset ) ``` |

#### Parameters

document
:   Type:  [Autodesk.Revit.DB Document](db03274b-a107-aa32-9034-f3e0df4bb1ec.htm)    
     The document in which to create the PropertySetElement.

thermalAsset
:   Type:  [Autodesk.Revit.DB ThermalAsset](c4dac7e3-96e2-bc6c-1299-f696a253e879.htm)    
     The thermal asset containing the values that will be present in the PropertySetElement.

#### Return Value

The new PropertySetElement.

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the name of the asset is empty, contains prohibited characters, or is not unique |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[PropertySetElement Class](dd2c8fbb-98ec-7249-87f0-542401f490dd.htm)

[Create Overload](a0689820-dbba-1e72-d1cc-f31b32969efd.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)