[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### AddElementsToCustomConnection Method

---



|  |
| --- |
| [StructuralConnectionHandlerType Class](e948a909-1b00-8789-6302-b46015c9cb47.htm)   [Example](#exampleToggle)   [See Also](#seeAlsoToggle) |

Modifies StructuralConnectionHandlerType of input StructuralConnectionHandler by adding representors of input elements or subelements.

**Namespace:**   [Autodesk.Revit.DB.Structure](d586b341-f687-9d90-e96d-255806b7d4fc.htm)    
  **Assembly:**   RevitAPI  (in RevitAPI.dll) Version: 22.0.0.0 (22.1.0.0)   
  **Since:**  2017

# Syntax

| C# |
| --- |
| ``` public static void AddElementsToCustomConnection( 	StructuralConnectionHandler structuralConnectionHandler, 	IList<Reference> references ) ``` |

 

| Visual Basic |
| --- |
| ``` Public Shared Sub AddElementsToCustomConnection ( _ 	structuralConnectionHandler As StructuralConnectionHandler, _ 	references As IList(Of Reference) _ ) ``` |

 

| Visual C++ |
| --- |
| ``` public: static void AddElementsToCustomConnection( 	StructuralConnectionHandler^ structuralConnectionHandler,  	IList<Reference^>^ references ) ``` |

#### Parameters

structuralConnectionHandler
:   Type:  [Autodesk.Revit.DB.Structure StructuralConnectionHandler](78653026-36f1-6ab3-f2c0-728692c99b3c.htm)    
     The existing StructuralConnectionHandler having custom StructuralConnectionHandlerType which is about to be modified.

references
:   Type:  System.Collections.Generic IList   [Reference](d28155ae-817b-1f31-9c3f-c9c6a28acc0d.htm)    
     References to elements or subelements which are to be used to modify custom StructuralConnectionHandlerType by adding their representors.

# Remarks

Elements or subelements added to a custom connection are deleted and transformed in subelements of the connection. They could be:

* FamilyInstance (structural beams and columns).
* StructuralConnectionHandler elements associated to the connection.
* Specific steel connection elements (bolts, anchors, plates, etc). These connection elements will be of type element but with categories related to structural connections, for example:
  + OST\_StructConnectionWelds
  + OST\_StructConnectionHoles
  + OST\_StructConnectionModifiers
  + OST\_StructConnectionShearStuds
  + OST\_StructConnectionBolts
  + OST\_StructConnectionAnchors
  + OST\_StructConnectionPlates

You cannot add: elements connected by any connection handler, generic connections, holes and modifiers that are not on the connected elements.

# Examples

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/CopyCode.gif) Copy  C#

```
   // Select elements to add to connection.
   IList<Reference> refs = Utilities.Functions.SelectConnectionElementsCustom(activeDoc);

   if (refs.Count() <= 0)
   {
      return Result.Failed;
   }

   // Start transaction
   trans.Start();
   // Adding the elements to the custom connection, using Revit's StructuralConnectionHandlerType class
   StructuralConnectionHandlerType.AddElementsToCustomConnection(conn, refs);
   // Commit the transaction
   ts = trans.Commit();

   if (ts != TransactionStatus.Committed)
   {
      message = "Failed to commit the current transaction !";
      trans.RollBack();
      return Result.Failed;
   }              
}
```

# Exceptions

| Exception | Condition |
| --- | --- |
| [Autodesk.Revit.Exceptions ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Input StructuralConnectionHandler must have custom type. -or- All the input Elements should be of the following structural categories: framings, columns, profiles, plates, bolts, anchors, shear studs, welds or structural connections. -or- Total number of different input elements of input StructuralConnectionHandlers must be lower or equal to 3. |
| [Autodesk.Revit.Exceptions ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non-optional argument was null |

# See Also

[StructuralConnectionHandlerType Class](e948a909-1b00-8789-6302-b46015c9cb47.htm)

[Autodesk.Revit.DB.Structure Namespace](d586b341-f687-9d90-e96d-255806b7d4fc.htm)