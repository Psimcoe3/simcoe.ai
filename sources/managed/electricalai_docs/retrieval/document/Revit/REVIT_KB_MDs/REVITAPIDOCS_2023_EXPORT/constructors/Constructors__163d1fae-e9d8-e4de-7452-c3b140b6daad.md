[✨ Located in SF Bay Area or LA? Get free Revit AI automation consulting from YC-backed AI engineers →](https://archilabs.ai/ca-revit-ai-pilot)



#### FilteredElementCollector Members

---



|  |
| --- |
| [FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)   [Constructors](#constructorTableToggle)   [Methods](#methodTableToggle)   [Properties](#propertyTableToggle)   [See Also](#seeAlsoToggle) |

The  [FilteredElementCollector](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)  type exposes the following members.

# Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [FilteredElementCollector(Document)](0635f1e4-652a-7e42-15af-94f24c4d8e8d.htm) | Constructs a new FilteredElementCollector that will search and filter the set of elements in a document. |
| Public method | [FilteredElementCollector(Document, ElementId)](6359776d-915e-f8a2-4147-b31024671ee1.htm) | Constructs a new FilteredElementCollector that will search and filter the visible elements in a view. |
| Public method | [FilteredElementCollector(Document, ICollection ElementId )](901f78a0-1f6c-217b-ea48-8b404324e88b.htm) | Constructs a new FilteredElementCollector that will search and filter a specified set of elements. |

# Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ContainedInDesignOption](92a2be0f-f632-2337-5bdd-ae3e832f3c33.htm) | Applies an ElementDesignOptionFilter to the collector. |
| Public method | [Dispose](c23c8781-f645-c059-7db5-d0cfd732dda1.htm) | Releases all resources used by the  [FilteredElementCollector](263cf06b-98be-6f91-c4da-fb47d01688f3.htm) |
| Public method | [Equals](http://msdn2.microsoft.com/en-us/library/bsc2ak47) | Determines whether the specified  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  is equal to the current  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  . (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [Excluding](80e23fdc-c005-163b-5643-38d84411a73d.htm) | Applies an ExclusionFilter to the collector. |
| Public method | [FirstElement](c8c1cae0-4ac8-a309-e915-6d491137d47e.htm) | Returns the first element to pass the filter(s). |
| Public method | [FirstElementId](b1b42ac5-e816-983a-f44d-5cf441ca1ad9.htm) | Returns the id of the first element to pass the filter(s). |
| Protected method | [GetBasicIEnumerator](07236f22-1721-1f6e-0fb6-f03709923430.htm) | Returns an enumerator that iterates through a collection. |
| Public method | [GetElementCount](886aabfd-ea87-e54c-d108-37d09a44d612.htm) | Gets the number of elements in your current filter. |
| Public method | [GetElementIdIterator](0b1cdbeb-21ce-a4c5-6cae-253595818085.htm) | Returns an element id iterator to the elements passing the filters. |
| Public method | [GetElementIterator](7113e21c-90f8-8f58-3b00-407fc1cd56e0.htm) | Returns an element iterator to the elements passing the filters. |
| Public method | [GetEnumerator](746ac65b-35c2-d0db-53d7-4fe0fd61ab1f.htm) | Returns an enumerator that iterates through a collection. |
| Public method | [GetHashCode](http://msdn2.microsoft.com/en-us/library/zdee4b3y) | Serves as a hash function for a particular type. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [GetType](http://msdn2.microsoft.com/en-us/library/dfwy45w9) | Gets the  [Type](http://msdn2.microsoft.com/en-us/library/42892f65)  of the current instance. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [IntersectWith](5b204fc8-7702-cf7e-346a-3a4c1767924b.htm) | Intersects the set of elements passing the filter in this collector with the set of elements passing the filter in another collector. |
| Public method Static member | [IsViewValidForElementIteration](9c7f3f9c-aa8a-8077-9235-ff1058c8b20b.htm) | Identifies if the particular element is valid for iteration of drawn elements. |
| Public method | [OfCategory](c3523c35-4a07-9723-3c28-de3cc47b2ad0.htm) | Applies an ElementCategoryFilter to the collector. |
| Public method | [OfCategoryId](63304108-73f8-844e-82fc-5b8fad9839b0.htm) | Applies an ElementCategoryFilter to the collector. |
| Public method | [OfClass](b0a5f22c-6951-c3af-cd29-1f28f574035d.htm) | Applies an ElementClassFilter to the collector. |
| Public method | [OwnedByView](54f2107a-bd87-41fe-dd00-385253ba5915.htm) | Applies an ElementOwnerViewFilter to the collector. |
| Public method | [ToElementIds](bfb8c8a2-aa2f-b1bc-7d57-7e3f7d39fcae.htm) | Returns the complete set of element ids that pass the filter(s). |
| Public method | [ToElements](732b4a0d-62d8-b86d-120b-8ea3d9713b34.htm) | Returns the complete set of elements that pass the filter(s). |
| Public method | [ToString](http://msdn2.microsoft.com/en-us/library/7bxwbwt2) | Returns a string that represents the current object. (Inherited from  [Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)  .) |
| Public method | [UnionWith](957cc5cb-5c7f-cac9-ec86-35afe824c432.htm) | Unites the set of elements passing the filter in this collector with the set of elements passing the filter in another collector. |
| Public method | [WhereElementIsCurveDriven](3f3269fc-367c-1fec-9ddb-d0b54ecc4f0e.htm) | Applies an ElementIsCurveDrivenFilter to the collector. |
| Public method | [WhereElementIsElementType](77793daa-5a26-b4d6-9019-4d998a55099e.htm) | Applies an ElementIsElementTypeFilter to the collector. |
| Public method | [WhereElementIsNotElementType](061cbbb9-26f1-a8f8-a4b2-3d7ff0105199.htm) | Applies an inverted ElementIsElementTypeFilter to the collector. |
| Public method | [WhereElementIsViewIndependent](38b15459-9ffe-204a-0193-47c3a1b5e6e2.htm) | Applies an ElementOwnerViewFilter to the collector. |
| Public method | [WherePasses](42d4eef3-55a1-2739-0ef8-6bc1d9fc2755.htm) | Applies an element filter to the collector. |

# Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsValidObject](259b95d7-5686-d69c-669f-904c3b08d6c8.htm) | Specifies whether the .NET object represents a valid Revit entity. |

# See Also

[FilteredElementCollector Class](263cf06b-98be-6f91-c4da-fb47d01688f3.htm)

[Autodesk.Revit.DB Namespace](87546ba7-461b-c646-cbb1-2cb8f5bff8b2.htm)