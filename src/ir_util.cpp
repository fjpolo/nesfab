#include "ir_util.hpp"

#include "globals.hpp"

bool io_pure(ssa_node_t const& ssa_node)
{
    if(ssa_flags(ssa_node.op()) & SSAF_IO_IMPURE)
        return false;
    if(ssa_node.op() == SSA_fn_call)
        return get_fn(ssa_node)->ir_io_pure();
    if(ssa_node.op() == SSA_read_ptr)
    {
        using namespace ssai::rw_ptr;
        return !ssa_node.input(BANK);
    }
    return true;
}

bool pure(ssa_node_t const& ssa_node)
{
    if(!io_pure(ssa_node))
       return false;
    if(ssa_node.op() == SSA_fn_call)
        return get_fn(ssa_node)->ir_writes().all_clear();
    return true;
}
