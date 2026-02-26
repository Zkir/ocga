# OCGA Language Reference

This document describes the OCGA (OpenStreetMap Computer Generated Architecture) language, its syntax, and supported operations.

## 1. Language Syntax

OCGA is a declarative shape grammar language used to define rules for generating 3D building models from 2D OpenStreetMap data.

### Program Structure

An OCGA program (`.ocga` file) generally follows this structure:

```ocga
ocga <VERSION_NUMBER>
const <CONSTANT_NAME> = <expression>
...
const <ANOTHER_CONSTANT_NAME> = <expression>
...
rule <RULE_NAME> :
    <operator1>
    <operator2>
    ...
rule <ANOTHER_RULE_NAME> :
    <operatorN>
    ...
```

*   **`ocga <VERSION_NUMBER>`**: The program must start with an `ocga` keyword followed by a version number.
*   **`const <CONSTANT_NAME> = <expression>`**: (Optional) Defines a constant that can be used in expressions.
*   **`rule <RULE_NAME> :`**: Defines a rule. A rule is a named block of one or more operators. Execution starts from a default rule (often implicitly defined or the first rule in the file).
    *   `<RULE_NAME>`: An identifier for the rule (e.g., `Start`, `MainWall`, `Window`).

### Conditional Statements

OCGA supports `if-then-else` conditional logic:

```ocga
if <logical_expression> then
    <operator1>
    <operator2>
else
    <operator3>
endif
```

*   **`if <logical_expression> then ... endif`**: Executes operators if the `logical_expression` is true.
*   **`else ...`**: (Optional) Executes operators if the `logical_expression` is false.

### Expressions

*   **`expr` (Arithmetic Expression)**: Can include numbers, literals, constants, relative numbers, and basic arithmetic operations (`+`, `-`, `*`, `/`, `%`).
    *   **Relative Numbers**: Numbers prefixed with an apostrophe (e.g., `'0.5`) are treated as relative values, often calculated based on the current object's scope dimensions.
*   **`lexpr` (Logical Expression)**: Used in `if` statements. Supports comparisons (`<`, `>`, `<=`, `>=`, `==`, `!=`), `not`, `and`, `or`.
*   **`list`**: A list of numbers enclosed in square brackets (e.g., `[0, 1, 5]`), typically used to specify indices of edges or nodes.

### Split Patterns

Used with `split_x`, `split_y`, `split_z` operators to define how an object is subdivided and which rule applies to each subdivision.

```ocga
<split_selector> : <rule_name> | <split_selector> : <rule_name> | <split_selector> : <rule_name>
```

*   **`<split_selector>`**:
    *   A number (e.g., `10`, `'0.3`) indicating a fixed size or a relative proportion.
    *   `~<NUMBER>`: An "approximately" size, where the number acts as a weight, and the actual size is calculated proportionally based on remaining space.
*   **`<rule_name>`**: The rule to apply to the newly created object (subdivision).
*   **Compound Split Patterns**: `(<split_pattern>) * <NUMBER>` can be used for repeating sections of a split pattern.

### Comments

Single-line comments start with `#`.

## 2. Supported Operations

Operations manipulate the current 3D object (a `T3DObject`). Many operations produce new objects, which are then added to the processing queue.

### Attributes (Tagging)

*   **`tag <key>, <value>`**: Sets an OpenStreetMap tag (`key=value`) on the current object.
*   **`colour <value>`**: Sets the `building:colour` tag. Hexadecimal values can be prefixed with `&` (e.g., `&RRGGBB`).
*   **`material <value>`**: Sets the `building:material` tag.
*   **`roof_colour <value>`**: Sets the `roof:colour` tag.
*   **`roof_material <value>`**: Sets the `roof:material` tag.
*   **`roof_direction <value>`**: Sets the `roof:direction` tag, typically an angle in degrees.

### Scope Operations

*   **`align_scope ('geometry' | 'x_to_longer_side')`**: Aligns the object's local coordinate system (scope).
    *   `'geometry'`: Aligns to the geometry's bounding box.
    *   `'x_to_longer_side'`: Rotates the scope so its X-axis aligns with the longer side of the object.
*   **`rotate_scope <angle_z>`**: Rotates the object's local coordinate system around the Z-axis by `angle_z` degrees.

### Geometry Creation

*   **`outer_rectangle <rule_name>`**: Replaces the current object's geometry with its outer bounding rectangle, then applies `rule_name` to this new shape.
*   **`primitive_cylinder <radius>` / `primitive_cylinder <radius>, [<nVertices>]` / `primitive_cylinder <radius>, [<nVertices>], [<pattern>]`**: Replaces the current object's geometry with a circular/cylindrical shape.
    *   `radius`: The radius of the circle.
    *   `nVertices`: (Optional) Number of vertices for the approximation of the circle (default 12).
    *   `pattern`: (Optional) Pattern for angular distribution of vertices.
*   **`primitive_halfcylinder <radius>, [<nVertices>]`**: Replaces the current object's geometry with a half-circular/half-cylindrical shape.
*   **`create_roof <roof_shape>, <roof_height>`**: Sets `roof:shape` and `roof:height` tags for the current object. `roof_height` can be relative to the object's current Z-scope.

### Geometry Subdivision

These operations split the current object into multiple new objects, typically applying a rule to each new part. The original object is often 'nil'-ed (removed) after the split.

*   **`split_x <split_pattern>`**: Splits the object along its local X-axis according to the `split_pattern`.
*   **`split_y <split_pattern>`**: Splits the object along its local Y-axis according to the `split_pattern`.
*   **`split_z <split_pattern>`**: Splits the object along its local Z-axis (height) according to the `split_pattern`. Handles roof preservation.
*   **`comp_border <distance>, <rule_name>`**: Creates new objects representing an offset border around the current object, then applies `rule_name`. Designed for symmetrical shapes.
*   **`comp_edges <distance>, <rule_name>`**: Creates new objects, each representing a "band" along an edge of the current object (similar to `comp_border` but for each edge individually), then applies `rule_name`.
*   **`comp_roof <rule_name>`**: Creates a new object that represents the roof of the current object (with adjusted `min_height` and `height`), then applies `rule_name`.

### Transformations

These operations modify the scale, position, or rotation of the current object.

*   **`scale <sx>, <sy>, [<sz>]`**: Scales the current object along its local X, Y, and optionally Z axes. `sx`, `sy`, `sz` can be relative.
*   **`translate <dx>, <dy>, [<dz>]`**: Translates (moves) the current object along its local X, Y, and optionally Z axes. `dx`, `dy`, `dz` can be relative.
*   **`rotate <angle_z>`**: Rotates the current object around its local Z-axis by `angle_z` degrees.

### Geometry Modifications

*   **`bevel <radius>, [<node_list>]`**: Applies a bevel (rounding or chamfering of corners) to the current object.
    *   `radius`: The radius of the bevel.
    *   `node_list`: (Optional) A list of node indices to apply the bevel to. Only works for closed polygons.
*   **`insert2 <a_param>, <b_param>, [<edge_list>]`**: Inserts new geometry into the current object's edges. Creates new nodes along the edges, potentially pushing them inwards or outwards.
    *   `a_param`: Controls the distance along the edge where new nodes are inserted.
    *   `b_param`: Controls the offset distance (e.g., inwards/outwards) from the edge.
    *   `edge_list`: (Optional) A list of edge indices to apply the operation to. Only works for closed polygons.

### Flow Control Operations

*   **`massModel <rule_name>`**: For a building outline, it applies a `split_z` operation to generate a mass model part and then applies `rule_name` to it.
*   **`continue <rule_name>`**: Continues processing with the specified `rule_name` on the current object. Not allowed for top-level buildings.
*   **`nope`**: A no-operation, effectively doing nothing. Can be useful as a placeholder.
*   **`restore`**: Ensures the current object remains in the list of active objects, useful if it was previously removed (e.g., by a `split` operation).
*   **`nil`**: Removes the current object from the list of active objects. Useful for creating holes.
*   **`print <expression>`**: Prints the value of the expression to the console (for debugging).
