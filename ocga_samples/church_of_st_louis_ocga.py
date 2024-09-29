"""
Set of rules to generate church of St Louis of France, Moscow
(c) Zkir 2020
"""
CREATE_CORNICE = False


def checkRulesMy(ctx):
    if ctx.getTag("building") != "":

        # guess height
        if ctx.getTag("building:levels") != "" and ctx.getTag("height") == 0:
            ctx.tag("height", str(float(ctx.getTag("building:levels")) * 4))

        ctx.tag("roof:material","metal")
        ctx.tag("roof:colour", "#202020")

        # align local coordinates so that X matches the longest dimension, and oriented east
        ctx.align_scope("geometry")
        ctx.alignXToLongerScopeSide()
        ctx.rotate_scope(180)

        # we will start from the rectangle and will rebuild the form
        # basing of this very algorithm
        ctx.outer_rectangle("mass_model")


    elif ctx.getTag("building:part") == "mass_model":
        #ctx.scale("'0.99", "'0.99")
        ctx.split_x(((3, "parvise_block"),("4.4", "entrance_block"), ("~5", "main_block"), ("~1", "apse_block")))

    elif ctx.getTag("building:part") == "parvise_block":
        ctx.tag("roof:material", "brick")
        ctx.tag("roof:colour", "#202020")
        ctx.scale("'1", "'0.9","1.5")
        ctx.split_y(((4.4, "parvise"), ("~5", "parvise_steps_pre"), (4.4, "parvise")))

    elif ctx.getTag("building:part") == "parvise_steps_pre":
        ctx.scale(ctx.scope_sx()-0.5,"'1")
        ctx.translate(-0.25, 0,0)
        ctx.tag("building:part", "steps")
        ctx.tag("roof:shape","skillion")
        ctx.tag("roof:height", ctx.getTag("height")-0.1)
        azimuth = (360 + 90 - ctx.scope_rz()) % 360  # from mathematical angle to geographical azimuth.
        # geographical azimuth is counted from north clockwise

        ctx.tag("roof:direction", (360+180+azimuth)%360)

    elif ctx.getTag("building:part") == "entrance_block":
        ctx.scale("'1", "'0.9")
        ctx.split_y(((ctx.scope_sx(), "bell_tower"), ("~5", "portico"), (ctx.scope_sx(), "bell_tower")))

    #bell towers
    elif ctx.getTag("building:part") == "bell_tower":
        ctx.scale("'1","'1","11")
        ctx.split_z_preserve_roof(( 
                                   ("~0.5", "bell_tower_dome_pre"),
                                   ("3.8", "bell_tower_layer_2"),
                                   ("7.0", "bell_tower_layer_1")
                                   ))

    elif ctx.getTag("building:part") == "bell_tower_layer_1":
        if CREATE_CORNICE:
         ctx.split_z_preserve_roof((
                                       ("0.01","roof"),
                                       ("0.20","cornice"),
                                       ("~1","bell_tower_layer_1a")
                                       ))

    elif ctx.getTag("building:part") == "cornice":
        ctx.scale(ctx.scope_sx()+0.75,ctx.scope_sy()+0.75)

    elif ctx.getTag("building:part") == "bell_tower_layer_2":
        ctx.scale(ctx.scope_sx()-0.5, ctx.scope_sy()-0.5)
        ctx.tag("roof:shape", "pyramidal")
        ctx.tag("roof:height", "0.75")
        ctx.tag("height", ctx.getTag("height")+0.75)

    elif ctx.getTag("building:part") == "bell_tower_dome_pre":
        ctx.scale(ctx.scope_sx() - 1, ctx.scope_sy() - 1,(ctx.scope_sy() - 1)/2*1.2)
        ctx.tag("roof:shape", "dome")
        ctx.tag("roof:height", ctx.scope_sy()/2 )
        ctx.primitive_cylinder("'1") #"bell_tower_dome"

    # portico
    elif ctx.getTag("building:part") == "portico":
        ctx.scale(ctx.scope_sx() + 0.5,"'1", 7+1.5) # +0.2
        ctx.translate(-0.25, 0)
        ctx.tag("roof:shape", "gabled")
        ctx.tag("roof:orientation", "across")
        ctx.tag("roof:height", "1.5")
        ctx.split_z_preserve_roof((
                                  ("0.2", "portico_top"),
                                  ("1.5", "portico_entablement"),
                                  ("~5", "portico_columns_block"),
                                  ("1.5", "portico_stilobate"),
                                  ))

    elif ctx.getTag("building:part") == "portico_stilobate":
        pass

    elif ctx.getTag("building:part") == "portico_columns_block":
        ctx.split_x((("~1", "portico_columns"), ("~2", "NIL")))

    elif ctx.getTag("building:part") == "portico_columns":
        ctx.split_y((("~1", "porch_column_pre"), ("~0.7", "NIL"),
                     ("~1", "porch_column_pre"), ("~0.7", "NIL"),
                     ("~1", "porch_column_pre"), ("~0.7", "NIL"),
                     ("~1", "porch_column_pre"),("~0.7", "NIL"),
                     ("~1", "porch_column_pre"),("~0.7", "NIL"),
                     ("~1", "porch_column_pre")))

    elif ctx.getTag("building:part") == "porch_column_pre":
        ctx.split_z_preserve_roof((("0.25", "porch_column_top_pre"),("~1", "porch_column_main")))

    elif ctx.getTag("building:part") == "porch_column_top_pre":
        top_size = min(ctx.scope_sx(), ctx.scope_sy()) / 1.0
        ctx.scale(top_size, top_size)
        ctx.tag("building:part", "porch_column_top")

    elif ctx.getTag("building:part") == "porch_column_main":
        # osmObject.osmtags["building:colour"] = "green"
        ctx.primitive_cylinder(min(ctx.scope_sx(), ctx.scope_sy()) / 3) # "porch_column"

    elif ctx.getTag("building:part") == "portico_top":
        ctx.scale (ctx.scope_sx()+0.5, ctx.scope_sy()+1.0)
        ctx.translate(-0.25,0,0)

    # main block
    elif ctx.getTag("building:part") == "main_block":
        ctx.split_y((("~1", "main_side_part_pre"),
                     ("~2", "main_main"),
                     ("~1", "main_side_part_pre")))

    elif ctx.getTag("building:part") == "main_main":
        ctx.scale("'1", "'1", "13")
        ctx.tag("roof:shape", "hipped")
        ctx.tag("roof:height", "1.5")
        ctx.split_x((("~1", "dormer_base_main"),))
        ctx.restore()
        if CREATE_CORNICE:
            ctx.split_z_preserve_roof((("0.01","roof"),
                                       ("0.2", "cornice"),
                                       ("~1", "main_main_part")))

    elif ctx.getTag("building:part") == "main_side_part_pre":
        ctx.scale("'1","'1","8.5")
        ctx.tag("roof:shape", "skillion")
        ctx.tag("roof:height", "1.5")
        azimuth =(360+90-ctx.scope_rz())%360 # from mathematical angle to geographical azimuth.
                                             # geographical azimuth is counted from north clockwise

        if ctx.current_object.relative_Oy > 0:
            # "undocumented" experimenal function
            # skillion roof should have upper edge from "inside" and lower from "outside"
            # we try to define what is inside and what is outside by relative location of the split parts (relative to parent)
            azimuth = (360+azimuth-90) % 360
        else:
            azimuth = (360+azimuth+90) % 360
        ctx.tag("roof:direction", azimuth)
        ctx.split_x((("~1", "dormer_base_side"),))
        ctx.restore()
        if CREATE_CORNICE:
            ctx.split_z_preserve_roof((
                                       ("0.01","roof"),
                                       ("0.2", "cornice"),
                                       ("~1", "main_side_part")
                                       ))

    elif ctx.getTag("building:part") == "dormer_base_side":
        min_height=ctx.getTag("height")-ctx.getTag("roof:height")
        ctx.tag("roof:height","")
        ctx.tag("roof:direction", "")
        ctx.tag("roof:orientation", "")

        ctx.tag("min_height", min_height)
        ctx.scale("'1", "'0.9", "1.1")
        ctx.split_x((("~2.5", "NIL"),("2", "dormer"),
                     ("~1", "NIL"), ("2", "dormer"),
                     ("~1", "NIL"), ("2", "dormer"),
                     ("~1", "NIL"), ("2", "dormer"),
                     ("~2.5", "NIL")))

    elif ctx.getTag("building:part") == "dormer_base_main":
        min_height=ctx.getTag("height")-ctx.getTag("roof:height")
        ctx.tag("roof:height","")
        ctx.tag("roof:direction", "")
        ctx.tag("roof:orientation", "")

        ctx.tag("min_height", min_height)
        ctx.scale("'1", "'0.9", "1.1")
        ctx.split_x((("~2.5", "NIL"),("2", "dormer"),
                     ("~3", "NIL"), ("2", "dormer"),
                     ("~2.5", "NIL")))

    elif ctx.getTag("building:part") == "dormer":
        ctx.tag("roof:shape", "round")
        ctx.tag("roof:height", "1.0")

    #apse block
    elif ctx.getTag("building:part") == "apse_block":
        ctx.split_y((("~1", "side_part_1_pre"),
                     ("1", "NIL"),
                     ("~2", "apse_pre"),
                     ("0.5", "NIL"),
                     ("~1", "side_part_2_pre")))

    elif ctx.getTag("building:part") == "apse_pre":
        ctx.tag("height",10)
        ctx.tag("roof:shape", "half-dome")
        ctx.tag("roof:height", "3")
        ctx.primitive_halfcylinder("'1",8)


    elif ctx.getTag("building:part") == "side_part_1_pre":
        ctx.split_x((("~1.5", "side_apse"), ("~1", "NIL")))
    elif ctx.getTag("building:part") == "side_part_2_pre":
        ctx.split_x((("~3", "side_apse"), ("~1", "NIL")))

    elif ctx.getTag("building:part") == "side_apse":
        ctx.scale("'1","'1","6.5")
        ctx.tag("roof:shape", "pyramidal")
        ctx.tag("roof:height", "1")

    elif ctx.getTag("building:part") == "NIL":
        ctx.nil()
