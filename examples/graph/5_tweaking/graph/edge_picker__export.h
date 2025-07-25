#pragma once

#include "edge_picker__tstub.h"

#include "edge__tstub.h"
#include "node__tstub.h"

struct graph$edge_picker$$Controller$$stub graph$edge_picker$$get_controller();

struct graph$node$$Node$$stub *graph$edge_picker$$pick_next(struct graph$edge_picker$$Controller$$stub *c, struct graph$node$$Node$$stub *n);
