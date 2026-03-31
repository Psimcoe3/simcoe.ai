[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### GetObjectData Method

---



|  |
| --- |
| [FunctionId Class](f510babd-969e-98fd-530e-c58fe4c9e5ca.htm)   [See Also](#seeAlsoToggle) |

Retrieves data needed to serialize the target object.

**Namespace:**   [Autodesk.Revit.Exceptions](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 2015.0.0.0 (2015.0.0.0)

# Syntax

| C# |
| --- |
| ``` public virtual void GetObjectData( 	SerializationInfo info, 	StreamingContext context ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Overridable Sub GetObjectData ( _ 	info As SerializationInfo, _ 	context As StreamingContext _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: virtual void GetObjectData( 	SerializationInfo^ info,  	StreamingContext context ) ``` |

#### Parameters

info
:   Type:  [System.Runtime.Serialization SerializationInfo](http://msdn2.microsoft.com/en-us/library/a9b6042e)    
     Data needed to serialize or deserialize the object.

context
:   Type:  [System.Runtime.Serialization StreamingContext](http://msdn2.microsoft.com/en-us/library/t16abws5)    
     The destination of the serialized stream.

#### Implements

 [ISerializable GetObjectData(SerializationInfo, StreamingContext)](http://msdn2.microsoft.com/en-us/library/27cxsdk6)

# See Also

[FunctionId Class](f510babd-969e-98fd-530e-c58fe4c9e5ca.htm)

[Autodesk.Revit.Exceptions Namespace](e3bbc463-dccb-6964-e8ef-697c9ed07a27.htm)