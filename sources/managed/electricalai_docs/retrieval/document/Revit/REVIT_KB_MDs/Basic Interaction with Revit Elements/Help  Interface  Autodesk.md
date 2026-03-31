---
created: 2026-01-28T20:50:22 (UTC -05:00)
tags: []
source: https://help.autodesk.com/view/RVT/2023/ENU/?guid=Revit_API_Revit_API_Developers_Guide_Basic_Interaction_with_Revit_Elements_Collections_Interface_html
author: 
---

# Help | Interface | Autodesk

> ## Excerpt
> The following sections discuss interface-related collection types.

---
The following sections discuss interface-related collection types.

### IEnumerable

The IEnumerable interface is in the System.Collections namespace. It exposes the enumerator, which supports a simple iteration over a non-generic collection. The GetEnumerator() method gets an enumerator that implements this interface. The returned [IEnumerator](http://msdn2.microsoft.com/en-us/library/system.collections.ienumerator.aspx) object is iterated throughout the collection. The GetEnumerator() method is used implicitly by foreach loops in C#.

### IEnumerator

The IEnumerator interface is in the System.Collections namespace. It supports a simple iteration over a non-generic collection. IEnumerator is the base interface for all non-generic enumerators. The foreach statement in C# hides the enumerator's complexity.

Note: Using foreach is recommended instead of directly manipulating the enumerator.

Enumerators are used to read the collection data, but they cannot be used to modify the underlying collection. Use IEnumerator as follows:

-   Initially, the enumerator is positioned in front of the first element in the collection. However, it is a good idea to always call Reset() when you first obtain the enumerator.
    -   The Reset() method moves the enumerator back to the original position. At this position, calling the Current property throws an exception.
    -   Call the MoveNext() method to advance the enumerator to the collection's first element before reading the current iterator value.
-   The Current property returns the same object until either the MoveNext() method or Reset() method is called. The MoveNext() method sets the current iterator to the next element.
-   If MoveNext passes the end of the collection, the enumerator is positioned after the last element in the collection and MoveNext returns false.
    -   When the enumerator is in this position, subsequent calls to the MoveNext also return false.
    -   If the last call to the MoveNext returns false, calling the Current property throws an exception.
    -   To set the current iterator to the first element in the collection again, call the Reset() method followed by MoveNext().
-   An enumerator remains valid as long as the collection remains unchanged.
    -   If changes are made to the collection, such as adding, modifying, or deleting elements, the enumerator is invalidated and the next call to the MoveNext() or the Reset() method throws an InvalidOperationException.
    -   If the collection is modified between the MoveNext and the current iterator, the Current property returns to the specified element, even if the enumerator is already invalidated.

Note: All calls to the Reset() method must result in the same state for the enumerator. The preferred implementation is to move the enumerator to the collection beginning, before the first element. This invalidates the enumerator if the collection is modified after the enumerator was created, which is consistent with the MoveNext() and the Current properties.
