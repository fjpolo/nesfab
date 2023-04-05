#ifndef STMT_HPP
#define STMT_HPP

#include <string>
#include <type_traits>
#include <limits>

#include "pstring.hpp"
#include "mods.hpp"
#include "asm.hpp"
#include "ast.hpp"

// stmts form a crude IR that is generated by the parser and 
// sent to the SSA IR builder.

struct stmt_ht : handle_t<stmt_ht, std::uint32_t, ~0> {};
struct stmt_mods_ht : handle_t<stmt_mods_ht, std::uint16_t, ~0> {};

#define STMT_XENUM \
    X(STMT_END_FN,     0)\
    X(STMT_IF,         true)\
    X(STMT_ELSE,       0)\
    X(STMT_END_IF,     0)\
    X(STMT_WHILE,      true)\
    X(STMT_END_WHILE,  0)\
    X(STMT_FOR,        true)\
    X(STMT_FOR_EFFECT, true)\
    X(STMT_END_FOR,    0)\
    X(STMT_EXPR,       true)\
    X(STMT_DO_WHILE,   0)\
    X(STMT_END_DO_WHILE, true)\
    X(STMT_DO_FOR,     0)\
    X(STMT_END_DO_FOR, true)\
    X(STMT_RETURN,     true)\
    X(STMT_BREAK,      0)\
    X(STMT_CONTINUE,   0)\
    X(STMT_LABEL,      0)\
    X(STMT_GOTO,       0)\
    X(STMT_GOTO_MODE,  true)\
    X(STMT_NMI,        0)\
    X(STMT_IRQ,        true)\
    X(STMT_FENCE,      0)\
    X(STMT_SWITCH,     true)\
    X(STMT_END_SWITCH, true)\
    X(STMT_CASE,       true)\
    X(STMT_DEFAULT,    0)\
    X(STMT_SWAP_FIRST, true)\
    X(STMT_SWAP_SECOND,true)


// Negative values represent var inits, where the negated value 
// holds the bitwise negated index of the fn variable.
// (See 'get_local_i')
enum stmt_name_t : std::int16_t
{
    STMT_MIN_VAR_DECL = std::numeric_limits<std::int16_t>::min(),
    STMT_MAX_VAR_DECL = -1,
#define X(x, e) x,
    STMT_XENUM
#undef X
};

bool has_expression(stmt_name_t stmt);

std::string to_string(stmt_name_t);

constexpr bool is_var_init(stmt_name_t stmt_name)
{
    return std::underlying_type_t<stmt_name_t>(stmt_name) < 0;
}

constexpr unsigned get_local_i(stmt_name_t stmt_name)
{
    assert(is_var_init(stmt_name));
    return ~static_cast<unsigned>(stmt_name);
}

struct stmt_t
{
    stmt_name_t name;
    stmt_mods_ht mods;
    stmt_ht link; // A stmt index, used to speed-up interpreters
    pstring_t pstring;
    union
    {
        ast_node_t const* expr;
        unsigned use_count; // Used for labels
    };
};

std::string to_string(stmt_name_t stmt_name);

#endif
